# System Health Monitoring Script

import psutil

CPU_LIMIT = 80
MEM_LIMIT = 80
DISK_LIMIT = 80

def check_health():
    cpu = psutil.cpu_percent(1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {mem}%")
    print(f"Disk Usage: {disk}%")

    if cpu > CPU_LIMIT:
        print("CPU usage is high!")
    if mem > MEM_LIMIT:
        print("Memory usage is high!")
    if disk > DISK_LIMIT:
        print("Disk usage is high!")

check_health()

# Application Health Checker

import requests

def check_app(url):
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            print(f"{url} is working fine")
        else:
            print(f"{url} is not responding properly")
    except Exception as e:
        print(f"Error checking {url}: {e}")

check_app("https://example.com")
