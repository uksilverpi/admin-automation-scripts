import os
from datetime import datetime

TEMPLATE = """# Daily Log – {date}

## Summary
- 

## Key Tasks
- 

## Notes
- 
"""

def main():
    # Get today's date in YYYY-MM-DD format
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"daily_log_{today}.md"

    # Avoid overwriting an existing log
    if os.path.exists(filename):
        print(f"{filename} already exists.")
        return

    # Fill the template with today's date
    content = TEMPLATE.format(date=today)

    # Create the log file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Created {filename}")

if __name__ == "__main__":
    main()
