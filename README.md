# Admin Automation Scripts

A collection of practical Python automation tools designed to reduce repetitive admin work, streamline workflows, and support real-world IT, data, and system tasks.

Every script in this repository is intentionally lightweight, readable, and built for everyday productivity.

---

## What This Repo Includes

A growing suite of tools for:

- File and folder organisation  
- Naming consistency and batch renaming  
- Data conversion  
- System diagnostics  
- Logging and reporting  
- Backup and workflow safety  
- General admin automation  

This repository will continue to expand with more scripts and documentation.

---

## Skills Demonstrated

- Python fundamentals  
- File handling and automation  
- System operations and diagnostics  
- Data parsing and conversion  
- Structured troubleshooting  
- Clean documentation  
- IT-support–friendly tooling  

---

## Usage

All scripts can be run using Command Prompt (Windows) or Terminal (macOS):

```bash
py script_name.py
```

or

```bash
python script_name.py
```

Each script provides its own prompts and instructions.

---

# Scripts Included

Below is a grid view of all automation tools in this project.  
Each card includes a short description and a direct link to the script.

<br>

<table>
<tr>

<td width="33%" valign="top">

<h3 title="Creates a daily markdown journal file with automatic date naming.">Daily Log Generator</h3>

<p title="Generates a markdown file with Summary, Key Tasks, and Notes sections.">
Creates a daily markdown log with sections for Summary, Tasks, and Notes.
</p>

<a href="./daily_log_generator.py"
   title="Open daily_log_generator.py"
   style="display:inline-block;padding:8px 14px;background:#e0e0e0;color:#000;text-decoration:none;border-radius:6px;font-weight:600;">
   View Script
</a>

</td>

<td width="33%" valign="top">

<h3 title="Generates markdown templates for meetings, notes, and documentation.">Template Generator</h3>

<p title="Creates a markdown file using a clean template (Overview, Details, Next Steps).">
Creates a markdown file using a simple template for notes and documentation.
</p>

<a href="./template_generator.py"
   title="Open template_generator.py"
   style="display:inline-block;padding:8px 14px;background:#e0e0e0;color:#000;text-decoration:none;border-radius:6px;font-weight:600;">
   View Script
</a>

</td>

<td width="33%" valign="top">

<h3 title="Automatically sorts files into folders by type.">Intelligent Folder Organiser</h3>

<p title="Organises files into folders such as Images, Documents, Text, Archives, etc.">
Sorts files into folders based on file extension (Images, Documents, Text, Archives, etc.).
</p>

<a href="./intelligent_folder_organiser.py"
   title="Open intelligent_folder_organiser.py"
   style="display:inline-block;padding:8px 14px;background:#e0e0e0;color:#000;text-decoration:none;border-radius:6px;font-weight:600;">
   View Script
</a>

</td>

</tr>
<tr>

<td width="33%" valign="top">

<h3 title="Renames groups of files with a consistent naming pattern.">Multi-File Renamer</h3>

<p title="Takes all files with a chosen extension and renames them with a prefix and index.">
Batch-renames files using a prefix and numbered sequence.
</p>

<a href="./multi_file_renamer.py"
   title="Open multi_file_renamer.py"
   style="display:inline-block;padding:8px 14px;background:#e0e0e0;color:#000;text-decoration:none;border-radius:6px;font-weight:600;">
   View Script
</a>

</td>

<td width="33%" valign="top">

<h3 title="Identifies duplicate files by content, not just by name.">Duplicate File Detector</h3>

<p title="Uses SHA-256 hashing to detect files with identical content.">
Finds duplicate files by hashing contents with SHA-256.
</p>

<a href="./duplicate_file_detector.py"
   title="Open duplicate_file_detector.py"
   style="display:inline-block;padding:8px 14px;background:#e0e0e0;color:#000;text-decoration:none;border-radius:6px;font-weight:600;">
   View Script
</a>

</td>

<td width="33%" valign="top">

<h3 title="Produces a quick system report for diagnostics.">System Health Checker</h3>

<p title="Prints OS information, disk usage, Python version, and optional CPU/RAM usage.">
Prints OS info, disk usage, and optional CPU/RAM usage.
</p>

<a href="./system_health_checker.py"
   title="Open system_health_checker.py"
   style="display:inline-block;padding:8px 14px;background:#e0e0e0;color:#000;text-decoration:none;border-radius:6px;font-weight:600;">
   View Script
</a>

</td>

</tr>
<tr>

<td width="33%" valign="top">

<h3 title="Checks basic network connectivity to key hosts.">Network Ping Monitor</h3>

<p title="Reads hosts from hosts.txt (if available) or uses defaults, then reports UP/DOWN.">
Pings hosts (default or from hosts.txt) and reports UP/DOWN network status.
</p>

<a href="./network_ping_monitor.py"
   title="Open network_ping_monitor.py"
   style="display:inline-block;padding:8px 14px;background:#e0e0e0;color:#000;text-decoration:none;border-radius:6px;font-weight:600;">
   View Script
</a>

</td>

<td width="33%" valign="top">

<h3 title="Converts spreadsheet-style CSV data into JSON.">CSV to JSON Converter</h3>

<p title="Reads a CSV file and outputs a structured JSON file with one object per row.">
Converts any CSV file into structured JSON format.
</p>

<a href="./csv_to_json_converter.py"
   title="Open csv_to_json_converter.py"
   style="display:inline-block;padding:8px 14px;background:#e0e0e0;color:#000;text-decoration:none;border-radius:6px;font-weight:600;">
   View Script
</a>

</td>

<td width="33%" valign="top">

<h3 title="Summarises log files by severity level.">Log File Analyzer</h3>

<p title="Counts ERROR, WARNING, and INFO lines in any log file to give a quick severity breakdown.">
Counts ERROR, WARNING, and INFO entries in any log file.
</p>

<a href="./log_file_analyzer.py"
   title="Open log_file_analyzer.py"
   style="display:inline-block;padding:8px 14px;background:#e0e0e0;color:#000;text-decoration:none;border-radius:6px;font-weight:600;">
   View Script
</a>

</td>

</tr>
<tr>

<td width="33%" valign="top">

<h3 title="Safely backs up a folder into a timestamped copy.">Auto-Backup Tool</h3>

<p title="Copies a folder into a backups directory, adding a timestamp to keep versions separate.">
Creates timestamped backups of any folder into a dedicated backups directory.
</p>

<a href="./auto_backup_tool.py"
   title="Open auto_backup_tool.py"
   style="display:inline-block;padding:8px 14px;background:#e0e0e0;color:#000;text-decoration:none;border-radius:6px;font-weight:600;">
   View Script
</a>

</td>

<td width="33%" valign="top">

<h3 title="Launches any script from a single menu interface.">Dashboard</h3>

<p title="Provides a simple command-line menu to run any of the tools in this repository.">
A command-line menu for launching any script from a single interface.
</p>

<a href="./dashboard.py"
   title="Open dashboard.py"
   style="display:inline-block;padding:8px 14px;background:#e0e0e0;color:#000;text-decoration:none;border-radius:6px;font-weight:600;">
   View Script
</a>

</td>

<td width="33%" valign="top">

</td>

</tr>
</table>

<br>

---

## Status

All scripts in this repository have been created, tested, and validated.  
New tools and documentation will be added over time.

---
