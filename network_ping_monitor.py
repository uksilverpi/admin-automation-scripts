import platform
import subprocess
from pathlib import Path

DEFAULT_HOSTS = [
    "8.8.8.8",      # Google DNS
    "1.1.1.1",      # Cloudflare DNS
    "github.com",   # GitHub
]

def ping_host(host: str) -> bool:
    """Return True if host responds to a single ping."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False

def load_hosts_file(path: Path) -> list[str]:
    if not path.exists():
        return []
    hosts = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                hosts.append(line)
    return hosts

def main():
    hosts_file = Path("hosts.txt")
    hosts = load_hosts_file(hosts_file) or DEFAULT_HOSTS

    print("Network Ping Monitor")
    print("--------------------")
    print(f"Using hosts: {', '.join(hosts)}\n")

    for host in hosts:
        status = "UP" if ping_host(host) else "DOWN"
        print(f"{host:<25} {status}")

if __name__ == "__main__":
    main()
