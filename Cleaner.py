import os
import shutil

def delete_files_in_folder(folder_path):
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Could not delete {file_path}. Reason: {e}")
    except Exception as e:
        print(f"Could not access folder {folder_path}. Reason: {e}")

def delete_temp_files():
    temp_folders = [
        r"C:\Windows\Prefetch",
        r"C:\Windows\Temp"
    ]

    for folder in temp_folders:
        print(f"Deleting files in: {folder}")
        delete_files_in_folder(folder)

if __name__ == "__main__":
    delete_temp_files()
    print("Cleanup complete!")
