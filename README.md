# Admin Automation Scripts

A collection of practical Python automation tools designed to reduce repetitive admin work, improve productivity, and support real-world IT, data, and system tasks.

Every script in this repository is lightweight, useful, and intentionally written for clarity and maintainability.

---

## What This Repo Includes

A full suite of scripts covering:

- File and folder organisation  
- Naming consistency and batch renaming  
- Data conversion  
- System diagnostics  
- Logging and reporting  
- Backup and workflow safety  
- General admin automation  

This repository continues to grow as more useful scripts are added.

---

## Skills Demonstrated

- Python fundamentals  
- File handling & system operations  
- Troubleshooting workflows  
- Data parsing and conversion  
- Process automation  
- Clean documentation and structured thinking  
- IT support–friendly tooling  

---

## Usage

All scripts can be run from Command Prompt (Windows) or Terminal (macOS):

```
py script_name.py
```

or

```
python script_name.py
```

Each script provides its own prompts and usage instructions.

---

# Scripts Included  
Click any script below to expand its details and open the file.

---

<details>
<summary><strong>1. Daily Log Generator</strong> – (click to expand)</summary>

Creates a Markdown log file for the current day with sections for Summary, Key Tasks, and Notes.

- Automatically names the file using today’s date  
- Prevents overwriting an existing log  
- Perfect for daily notes, journaling, or tracking work  

👉 **Open script:**  
[daily_log_generator.py](./daily_log_generator.py)

</details>

---

<details>
<summary><strong>2. Template Generator</strong> – (click to expand)</summary>

Creates a Markdown document using a clean boilerplate template (Overview, Details, Next Steps).

- Title becomes a cleaned filename  
- Automatically inserts today’s date  
- Ideal for meeting notes and documentation  

👉 **Open script:**  
[template_generator.py](./template_generator.py)

</details>

---

<details>
<summary><strong>3. Intelligent Folder Organiser</strong> – (click to expand)</summary>

Sorts files into extension-based folders such as Images, Documents, Text, Archives, etc.

- Avoids overwriting  
- Automatically creates missing folders  
- Great for cleaning messy directories  

👉 **Open script:**  
[intelligent_folder_organiser.py](./intelligent_folder_organiser.py)

</details>

---

<details>
<summary><strong>4. Multi-File Renamer</strong> – (click to expand)</summary>

Renames all files of a selected extension to a consistent numbered pattern.

Example:

`notes_1.txt`  
`notes_2.txt`  
`notes_3.txt`

- Choose prefix  
- Choose starting index  
- Ensures tidy, organised filenames  

👉 **Open script:**  
[multi_file_renamer.py](./multi_file_renamer.py)

</details>

---

<details>
<summary><strong>5. Duplicate File Detector</strong> – (click to expand)</summary>

Detects duplicate files by hashing file contents (SHA-256), not by filename.

- Finds duplicates even with different names  
- Useful for storage clean-ups  
- Helps manage shared drives  

👉 **Open script:**  
[duplicate_file_detector.py](./duplicate_file_detector.py)

</details>

---

<details>
<summary><strong>6. System Health Checker</strong> – (click to expand)</summary>

Produces a system report including:

- OS version  
- Python version  
- Disk usage  
- Optional CPU/RAM usage (via `psutil`)

Great for troubleshooting and IT diagnostics.

👉 **Open script:**  
[system_health_checker.py](./system_health_checker.py)

</details>

---

<details>
<summary><strong>7. Network Ping Monitor</strong> – (click to expand)</summary>

Pings a list of hosts (from `hosts.txt` or default DNS servers) and shows UP/DOWN status.

- Useful for quick connectivity tests  
- Works on Windows and macOS  

👉 **Open script:**  
[network_ping_monitor.py](./network_ping_monitor.py)

</details>

---

<details>
<summary><strong>8. CSV to JSON Converter</strong> – (click to expand)</summary>

Converts any CSV file into neatly formatted JSON.

- Perfect for admin data tasks  
- Preserves column-to-JSON mapping automatically  

👉 **Open script:**  
[csv_to_json_converter.py](./csv_to_json_converter.py)

</details>

---

<details>
<summary><strong>9. Log File Analyzer</strong> – (click to expand)</summary>

Counts how many lines contain ERROR, WARNING, or INFO in any log file.

- Helps with debugging and incident reporting  
- Fast and lightweight  

👉 **Open script:**  
[log_file_analyzer.py](./log_file_analyzer.py)

</details>

---

<details>
<summary><strong>10. Auto-Backup Tool</strong> – (click to expand)</summary>

Creates timestamped backups of a folder and places them inside a dedicated `backups/` directory.

- Protects important files  
- Maintains historical versions  
- Uses Python’s `copytree` to preserve structure  

👉 **Open script:**  
[auto_backup_tool.py](./auto_backup_tool.py)

</details>

---

## Status

All scripts have been created, tested, and validated.  
This repository will continue expanding with more automation tools and documentation.

---
<details>
<summary><b>Daily Log Generator</b></summary>

<div style="padding:10px; border:1px solid #ddd; border-radius:6px;">

Description here...

[Open Script](./daily_log_generator.py)

</div>
</details>

