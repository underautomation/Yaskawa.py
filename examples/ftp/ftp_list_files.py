"""
FTP - List Files
================
List the folders and the files of the controller over FTP, with their date.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - FTP: List Files")
print("=" * 60)

robot = connect_robot(ftp=True)

try:
    print(f"Logged as {robot.ftp.user}\n")
    for folder in robot.ftp.get_listing("/"):
        files = robot.ftp.get_listing(folder.full_name)
        print(f"{folder.full_name}: {len(files)} file(s)")
        for item in list(files)[:5]:
            print(f"    {item.name:20} {item.modified}")
        if len(files) > 5:
            print("    ...")

finally:
    robot.disconnect()
    print("\nDisconnected.")
