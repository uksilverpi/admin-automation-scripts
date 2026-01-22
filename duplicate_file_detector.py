import hashlib
from pathlib import Path

BUFFER_SIZE = 1024 * 1024  # 1 MB chunks

def file_hash(path: Path) -> str:
    """Return a SHA-256 hash of the file."""
    hasher = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(BUFFER_SIZE):
            hasher.update(chunk)
    return hasher.hexdigest()

def main():
    folder = Path.cwd()
    print(f"Scanning for duplicates in: {folder}\n")

    seen = {}       # hash → original file
    duplicates = [] # list of (original, duplicate)

    for f in folder.iterdir():
        if not f.is_file():
            continue

        h = file_hash(f)

        if h in seen:
            duplicates.append((seen[h], f))
        else:
            seen[h] = f

    if not duplicates:
        print("No duplicate files found.")
        return

    print("Duplicate files detected:\n")
    for original, duplicate in duplicates:
        print(f"• {duplicate.name} is a duplicate of {original.name}")

if __name__ == "__main__":
    main()
