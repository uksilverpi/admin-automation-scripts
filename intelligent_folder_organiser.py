import os
import shutil
from pathlib import Path

# Map file extensions to folder names
EXTENSION_MAP = {
    ".txt": "Text",
    ".md": "Markdown",
    ".pdf": "PDFs",
    ".doc": "Documents",
    ".docx": "Documents",
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Data",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".zip": "Archives",
    ".rar": "Archives",
}

DEFAULT_FOLDER = "Other"

def organise_folder(target: Path) -> None:
    for item in target.iterdir():
        # Skip directories
        if item.is_dir():
            continue

        # Skip this script itself
        if item.name == Path(__file__).name:
            continue

        ext = item.suffix.lower()
        folder_name = EXTENSION_MAP.get(ext, DEFAULT_FOLDER)
        dest_folder = target / folder_name
        dest_folder.mkdir(exist_ok=True)

        dest_path = dest_folder / item.name
        if dest_path.exists():
            print(f"Skipping (already exists): {dest_path}")
            continue

        print(f"Moving {item} -> {dest_path}")
        shutil.move(str(item), str(dest_path))

def main():
    target = Path.cwd()
    print(f"Organising folder: {target}")
    organise_folder(target)
    print("Done.")

if __name__ == "__main__":
    main()
