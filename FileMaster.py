import os
import shutil

def organize_files(source_folder):
    # Get a list of all files in the source folder
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    # Organize files based on their formats
    for file in files:
        # Get the file extension (format)
        _, file_extension = os.path.splitext(file)

        # Create a folder for the format if it doesn't exist
        format_folder = os.path.join(source_folder, file_extension[1:].upper())
        os.makedirs(format_folder, exist_ok=True)

        # Move the file to the corresponding format folder
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(format_folder, file)
        shutil.move(source_path, destination_path)
        print(f"Moved '{file}' to '{format_folder}'.")

if __name__ == "__main__":
    # Specify the path to the folder you want to organize
    source_folder = "C:\\Users\\chaud\\Desktop\\Random"

    # Call the organize_files function
    organize_files(source_folder)
