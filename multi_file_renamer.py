import os
from pathlib import Path

def main():
    folder = Path.cwd()
    print(f"Working in: {folder}")

    extension = input("Enter file extension to rename (e.g. .txt, .jpg): ").strip()
    if not extension.startswith("."):
        extension = "." + extension

    prefix = input("Enter filename prefix (e.g. case_notes): ").strip()
    if not prefix:
        print("Prefix cannot be empty.")
        return

    try:
        start_index = int(input("Enter starting number (e.g. 1): ").strip())
    except ValueError:
        print("Invalid number.")
        return

    files = sorted([
        f for f in folder.iterdir()
        if f.is_file() and f.suffix.lower() == extension.lower()
    ])

    if not files:
        print(f"No files with extension {extension} found.")
        return

    index = start_index
    for f in files:
        new_name = f"{prefix}_{index}{extension}"
        dest = folder / new_name

        if dest.exists():
            print(f"Skipping {f.name} -> {new_name} (target exists)")
        else:
            print(f"Renaming {f.name} -> {new_name}")
            f.rename(dest)

        index += 1

    print("Done.")

if __name__ == "__main__":
    main()
