"""
FTP - Download Files
====================
Download the files that match a pattern into a local folder over FTP, with the progress.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - FTP: Download Files")
print("=" * 60)

robot = connect_robot(ftp=True)

try:
    pattern = input("File pattern [*.JBI]: ").strip() or "*.JBI"
    folder = input("Local folder [backup]: ").strip() or "backup"

    names = list(robot.ftp.get_file_list_by_pattern(pattern))
    print(f"\n{len(names)} file(s) match {pattern}")

    def progress(percent):
        if percent >= 0:
            print(f"\r  {percent:5.1f} %", end="")

    saved = robot.ftp.download_files_to_local(names, folder, progress)
    print()
    for path in saved:
        print(f"  {path}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
