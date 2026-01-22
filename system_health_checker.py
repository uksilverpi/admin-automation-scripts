import platform
import shutil
from datetime import datetime
from pathlib import Path

def get_disk_usage(path: Path):
    total, used, free = shutil.disk_usage(path)
    to_gb = 1024 ** 3
    return total / to_gb, used / to_gb, free / to_gb

def try_psutil():
    try:
        import psutil  # type: ignore
    except ImportError:
        return None
    return psutil

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"System Health Report – {now}")
    print("-" * 40)

    print(f"OS: {platform.system()} {platform.release()} ({platform.version()})")
    print(f"Machine: {platform.machine()}")
    print(f"Python: {platform.python_version()}")
    print()

    total, used, free = get_disk_usage(Path.cwd())
    print("Disk usage (current drive):")
    print(f"- Total: {total:.2f} GB")
    print(f"- Used:  {used:.2f} GB")
    print(f"- Free:  {free:.2f} GB")
    print()

    psutil = try_psutil()
    if psutil:
        print("CPU and Memory (via psutil):")
        print(f"- CPU usage: {psutil.cpu_percent(interval=1)}%")
        mem = psutil.virtual_memory()
        print(f"- RAM used: {mem.percent}%")
    else:
        print("CPU and RAM usage: psutil not installed (optional).")
        print("Install with: pip install psutil")

if __name__ == "__main__":
    main()
