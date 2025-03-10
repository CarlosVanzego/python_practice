# This is example is for a scenario where you may want to check the health of your computer.
# As this may require various tests, we can create a script to check each of these values all at once.
# We can use the shutil module, and the disk_usage function to check for the available disk space
# We can also the psutil and the cpu_percent function that will return a number showing how much of the CPU is being used.
# The script below conducts both of these checks together:
# 

# !/user/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")

else:
    print("Everything is OK!")    