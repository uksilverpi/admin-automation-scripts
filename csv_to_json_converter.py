import csv
import json
from pathlib import Path

def main():
    csv_name = input("Enter CSV filename (e.g. data.csv): ").strip()
    if not csv_name:
        print("Filename cannot be empty.")
        return

    csv_path = Path(csv_name)
    if not csv_path.exists():
        print(f"File not found: {csv_path}")
        return

    json_path = csv_path.with_suffix(".json")

    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)

    print(f"Converted {csv_path} -> {json_path}")

if __name__ == "__main__":
    main()
