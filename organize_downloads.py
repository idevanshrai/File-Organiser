import os
import shutil
from pathlib import Path

#Path
DOWNLOADS_FOLDER = str(Path.home() / "Downloads")

# FILE EXTENSION
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".md"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".webm"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Programs": [".exe", ".dmg", ".pkg", ".sh", ".app"],
    "Others": []
}

def create_folders():
    """Create category folders if they don't exist."""
    for category in FILE_CATEGORIES.keys():
        folder_path = os.path.join(DOWNLOADS_FOLDER, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


def organize_files():
    """Move files into their respective category folders."""
    for file_name in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, file_name)

        
        if os.path.isdir(file_path):
            continue

        #File's category based on extension
        file_extension = os.path.splitext(file_name)[1].lower()
        category_found = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                target_folder = os.path.join(DOWNLOADS_FOLDER, category)
                shutil.move(file_path, target_folder)
                category_found = True
                break

        #others folder 
        if not category_found:
            other_folder = os.path.join(DOWNLOADS_FOLDER, "Others")
            shutil.move(file_path, other_folder)


def main():
    create_folders()
    organize_files()
    print("Files have been organized successfully!")

if __name__ == "__main__":
    main()
