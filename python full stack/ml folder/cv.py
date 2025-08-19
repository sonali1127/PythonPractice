import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

# Start video capture
video = cv2.VideoCapture(0)  # Use 0 for the default webcam

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Perform object detection
    bbox, label, conf = cv.detect_common_objects(frame)

    # Draw bounding boxes and labels
    output_image = draw_bbox(frame, bbox, label, conf)

    # Show the result
    cv2.imshow("Object Detection", output_image)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release video capture and close windows
video.release()
cv2.destroyAllWindows()
