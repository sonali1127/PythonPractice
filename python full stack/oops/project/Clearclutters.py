import os
import shutil

def folderCreation(folder_path):
    try:
        os.makedirs(folder_path, exist_ok=True)
        print(f"Folder '{folder_path}' created successfully or already exists.")
    except Exception as e:
        print(f"An error occurred while creating folder: {e}")

def rename_file(old_name, source_folder):
    base, ext = os.path.splitext(old_name)
    ext_folder = os.path.join(source_folder, ext[1:])  # Remove the dot from extension
    folderCreation(ext_folder)
    
    new_full_name = os.path.join(source_folder, "1" + ext)
    old_full_name = os.path.join(source_folder, old_name)
    
    try:
        os.rename(old_full_name, new_full_name)
        print(f"File '{old_name}' renamed to '{new_full_name}'.")
    except Exception as e:
        print(f"An error occurred while renaming file: {e}")
    
    move_file(new_full_name, ext_folder)

def move_file(source, destination_folder):
    if not os.path.exists(destination_folder):
        folderCreation(destination_folder)
    
    filename = os.path.basename(source)
    destination_path = os.path.join(destination_folder, filename)
    
    if os.path.exists(destination_path):
        base, ext = os.path.splitext(filename)
        counter = 2
        while True:
            new_filename = f"{base}_{counter}{ext}"
            new_destination = os.path.join(destination_folder, new_filename)
            if not os.path.exists(new_destination):
                shutil.move(source, new_destination)
                print(f"File moved and renamed to: {new_destination}")
                break
            counter += 1
    else:
        shutil.move(source, destination_path)
        print(f"File moved to: {destination_path}")

# Main execution
folder_path = "/Users/User/OneDrive/Documents/python12"
files = os.listdir(folder_path)
for file in files:
    rename_file(file, folder_path)