import shutil
from datetime import datetime
from pathlib import Path

def main():
    source_input = input("Enter folder to back up (leave empty for current folder): ").strip()
    source = Path(source_input) if source_input else Path.cwd()

    if not source.exists() or not source.is_dir():
        print(f"Invalid folder: {source}")
        return

    backups_root = source.parent / "backups"
    backups_root.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = backups_root / f"{source.name}_{timestamp}"

    print(f"Backing up {source} -> {dest}")
    shutil.copytree(source, dest)
    print("Backup complete.")

if __name__ == "__main__":
    main()
