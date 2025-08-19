import os 
folder="/Users/User/OneDrive/Documents/python/python full stack/oops/project/folders"
c=1
files=os.listdir(folder)
c=1
for file in files:
    if file.endswith(".png"):
        old_file_path = os.path.join(folder, file)
        new_file_path = os.path.join(folder, f"{c}.png")
        try:
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{old_file_path}' to '{new_file_path}'.")
        except Exception as e:
            print(f"Error renaming '{old_file_path}': {e}")
        c=c+1