import os
import shutil

def delete_directory(dir_path):
    try:
        shutil.rmtree(dir_path)
        print(f"OpenVR deleted successfully.")
    except FileNotFoundError:
        print(f"OpenVR not found.")
    except PermissionError:
        print(f"No permission to delete the directory '{dir_path}'.")
    except Exception as e:
        print(f"Error occurred: {e}")

# Path to openvr, might not be C drive
dir_path = 'C:\\Users\\YOUR_USERNAME_HERE\\AppData\\Local\\openvr'
delete_directory(dir_path)