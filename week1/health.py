#!/usr/bin/env python3
import shutil
import subprocess
from datetime import datetime

with open("health.log", "a") as f:
    f.write("=== Python health check ===\n")
    f.write(str(datetime.now()) + "\n")
    
    disk = shutil.disk_usage("/")
    f.write("Disk total GB: " + str(round(disk.total / 1024**3, 1)) + "\n")
    f.write("Disk free GB: " + str(round(disk.free / 1024**3, 1)) + "\n")

    memory = subprocess.run(["free", "-h"], capture_output=True, text=True)
    f.write(memory.stdout)

