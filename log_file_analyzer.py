from pathlib import Path
from collections import Counter

LEVELS = ["ERROR", "WARNING", "INFO"]

def main():
    log_name = input("Enter log filename (e.g. app.log): ").strip()
    if not log_name:
        print("Filename cannot be empty.")
        return

    log_path = Path(log_name)
    if not log_path.exists():
        print(f"File not found: {log_path}")
        return

    counts = Counter()
    total_lines = 0

    with log_path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            total_lines += 1
            upper_line = line.upper()
            for level in LEVELS:
                if level in upper_line:
                    counts[level] += 1

    print(f"\nLog Analysis – {log_path.name}")
    print("-----------------------------")
    print(f"Total lines: {total_lines}\n")
    for level in LEVELS:
        print(f"{level}: {counts[level]}")

if __name__ == "__main__":
    main()
