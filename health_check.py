import shutil
from pathlib import Path

# Linux disk monitoring for SRE practice

def check_disk():

    usage = shutil.disk_usage(Path.home())

    total_gb = usage.total / (1024 ** 3)
    free_gb = usage.free / (1024 ** 3)
    used_percent = (usage.used / usage.total) * 100

    print("===== DISK HEALTH REPORT =====")
    print(f"Total: {total_gb:.2f} GB")
    print(f"Free: {free_gb:.2f} GB")
    print(f"Used: {used_percent:.2f}%")

    if used_percent >= 90:
        print("WARNING: Disk usage is critical")
    else:
        print("Disk usage is within threshold")

if __name__ == "__main__":
    check_disk()
