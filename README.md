# Admin Automation Scripts

This repository contains a collection of practical Python automation tools designed to reduce repetitive admin work, streamline workflows, and support real-world IT and data tasks.

Every script is lightweight, readable, and created with everyday productivity in mind.

---

## What This Repo Includes

A growing set of automation scripts that handle:

- File and folder organisation  
- Document and naming consistency  
- Data conversion  
- System diagnostics  
- Logging and reporting  
- Backup and workflow safety  

These scripts demonstrate practical automation for IT support, admin work, and systems housekeeping.

---

## Skills Demonstrated

- Python fundamentals  
- Troubleshooting and problem-solving  
- Process automation  
- System information gathering  
- File handling and data manipulation  
- Clean, clear documentation  
- Real-world usability  

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

Below is a complete collection of automation tools included in this repository.

---

### **1. Daily Log Generator (`daily_log_generator.py`)**
Creates a Markdown log file for the current day with sections for Summary, Key Tasks, and Notes.  
- Automatically names the file using today’s date  
- Prevents overwriting existing logs  
- Perfect for journaling or tracking daily work  

---

### **2. Template Generator (`template_generator.py`)**
Generates a markdown file using a simple documentation template (Overview, Details, Next Steps).  
- Title becomes the filename  
- Date inserted automatically  
- Useful for meetings, notes, and documentation  

---

### **3. Intelligent Folder Organiser (`intelligent_folder_organiser.py`)**
Sorts files in the current directory into subfolders based on file extension.  
- Creates folders like Images, Documents, Text, Archives  
- Avoids overwriting existing files  
- Great for cleaning messy folders  

---

### **4. Multi-File Renamer (`multi_file_renamer.py`)**
Renames all files with a chosen extension to a consistent pattern like:  
`notes_1.txt`, `notes_2.txt`, `notes_3.txt`.  
- Choose prefix and starting number  
- Ensures organised, predictable filenames  

---

### **5. Duplicate File Detector (`duplicate_file_detector.py`)**
Detects duplicate files by comparing SHA-256 hashes.  
- Identifies duplicates even if filenames differ  
- Useful for storage cleanup and shared drives  

---

### **6. System Health Checker (`system_health_checker.py`)**
Generates a simple diagnostic report including:  
- OS information  
- Disk usage  
- Python version  
- Optional CPU/RAM usage (via psutil, if installed)  

Ideal for IT support or troubleshooting.

---

### **7. Network Ping Monitor (`network_ping_monitor.py`)**
Pings a list of hosts (from `hosts.txt`, or default DNS servers) and shows which are UP or DOWN.  
- Great for quick connectivity checks  
- Supports Windows and macOS  

---

### **8. CSV to JSON Converter (`csv_to_json_converter.py`)**
Reads a CSV file and exports its contents as formatted JSON.  
- Automatically maps columns  
- Perfect for data cleaning or migrations  

---

### **9. Log File Analyzer (`log_file_analyzer.py`)**
Counts ERROR, WARNING, and INFO entries in any log file.  
- Shows total lines  
- Breaks down severity levels  
- Useful for debugging and incident reports  

---

### **10. Auto-Backup Tool (`auto_backup_tool.py`)**
Creates a timestamped backup of any folder.  
- Backups stored in a separate `backups/` directory  
- Preserves structure and files with `copytree`  
- Ideal for safeguarding important work  

---

## Status

All scripts are functional and tested.  
This repository will continue to grow with more real-world IT and admin automation tools.

---
