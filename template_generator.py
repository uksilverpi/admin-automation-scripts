import os
from datetime import datetime

TEMPLATE = """# {title}

Date: {date}

## Overview
- 

## Details
- 

## Next Steps
- 
"""

def main():
    title = input("Enter a title for the template: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    safe_title = title.replace(" ", "_").lower()
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{safe_title}_{today}.md"

    if os.path.exists(filename):
        print(f"{filename} already exists.")
        return

    content = TEMPLATE.format(title=title, date=today)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Created {filename}")

if __name__ == "__main__":
    main()
