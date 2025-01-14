# File Organiser

A Python script to automatically organize downloaded files on macOS into categorized folders based on file types. This utility helps keep your `Downloads` folder clean and clutter-free.

## Features

- Categorizes files into predefined folders such as `Images`, `Documents`, `Videos`, etc.
- Supports customizable file type extensions for each category.
- Moves unrecognized files to an `Others` folder.
- Easy to run and modify for personal preferences.

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/idevanshrai/File-Organizer.git
   cd download-File-Organizer
   ```

2. **Ensure Python is installed**:
   - Check your Python version:
     ```bash
     python3 --version
     ```
   - Install Python if not already installed.

3. **Install required packages** (if any):
   - This script uses Python's built-in libraries and does not require external packages.

## Usage

1. Run the script:
   ```bash
   python3 organize_downloads.py
   ```

2. The script will organize files in your `Downloads` folder into categorized subfolders:
   - **Images**: `.jpg`, `.png`, `.gif`, etc.
   - **Documents**: `.pdf`, `.docx`, `.xlsx`, etc.
   - **Videos**: `.mp4`, `.avi`, `.mkv`, etc.
   - **Others**: Files that do not match any category.

## Customization

- Open `organize_downloads.py` in a text editor.
- Modify the `categories` dictionary to add, remove, or update file type extensions.

```python
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Others": []  # For uncategorized files
}
```
