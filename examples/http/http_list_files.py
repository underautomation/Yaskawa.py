"""
HTTP - List Files
=================
List the files of each type with the description given by the web server of the
controller. No account and no remote mode are needed.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.yaskawa.common.file_extension import FileExtension

print("=" * 60)
print("  YASKAWA SDK - HTTP: List Files")
print("=" * 60)

robot = connect_robot(http=True)

try:
    for extension in (FileExtension.JOB, FileExtension.DAT, FileExtension.PRM):
        files = robot.http.get_file_list(extension)
        print(f"\n{extension.name}: {len(files)} file(s)")
        for file in files:
            print(f"  {file.name:16} {file.description or ''}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
