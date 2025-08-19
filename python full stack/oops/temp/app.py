from flask import Flask, request, jsonify, render_template, send_file
from werkzeug.utils import secure_filename
import boto3
import os
import json
import io
from botocore.exceptions import NoCredentialsError

app = Flask(__name__)

# AWS Configuration
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME", "secureshare7")
AWS_REGION = os.getenv("AWS_REGION", "eu-north-1")

# Initialize S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

# Allowed file extensions
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif", "pem"}

# Password storage file (replace with DB in production)
PASSWORD_STORE_FILE = "file_passwords.json"

# Load or initialize password storage
if os.path.exists(PASSWORD_STORE_FILE):
    with open(PASSWORD_STORE_FILE, "r") as f:
        FILE_PASSWORDS = json.load(f)
else:
    FILE_PASSWORDS = {}

# Helper function to check file extensions
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to handle file uploads
@app.route("/upload", methods=["POST"])
def upload_file():
    """Handle file uploads with password protection."""
    try:
        if "file" not in request.files or "password" not in request.form:
            return jsonify({"error": "File and password are required"}), 400

        file = request.files["file"]
        password = request.form["password"]

        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400

        if not allowed_file(file.filename):
            return jsonify({"error": "File type not allowed"}), 400

        # Sanitize the filename
        file_name = secure_filename(file.filename)

        # Upload the file to S3
        s3_client.upload_fileobj(
            file,
            AWS_BUCKET_NAME,
            file_name,
            ExtraArgs={"ContentType": file.content_type}
        )

        # Store password securely
        FILE_PASSWORDS[file_name] = password
        with open(PASSWORD_STORE_FILE, "w") as f:
            json.dump(FILE_PASSWORDS, f)

        # Generate the file URL (not exposed to users directly)
        file_url = f"https://{AWS_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{file_name}"
        return jsonify({"message": "File uploaded successfully", "url": file_url})
    except NoCredentialsError:
        return jsonify({"error": "AWS credentials not found"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to list uploaded files
@app.route("/list-uploaded-files", methods=["GET"])
def list_uploaded_files():
    """Fetch the list of uploaded files from S3."""
    try:
        response = s3_client.list_objects_v2(Bucket=AWS_BUCKET_NAME)
        files = [item["Key"] for item in response.get("Contents", [])]
        return jsonify({"files": files})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to proxy file downloads with password protection
@app.route("/proxy", methods=["GET"])
def proxy():
    """Proxy requests to S3 to validate password before allowing downloads."""
    file_name = request.args.get("file_name")
    password = request.args.get("password")

    if not file_name or not password:
        return jsonify({"error": "File name and password are required"}), 400

    # Validate the password
    stored_password = FILE_PASSWORDS.get(file_name)
    if not stored_password or stored_password != password:
        return jsonify({"error": "Invalid password"}), 403

    try:
        # Fetch the file from S3
        response = s3_client.get_object(Bucket=AWS_BUCKET_NAME, Key=file_name)
        file_data = response["Body"].read()

        # Send file as an attachment (triggers browser download)
        return send_file(
            io.BytesIO(file_data),
            mimetype=response["ContentType"],
            as_attachment=True,
            download_name=file_name
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    """Render the homepage."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
