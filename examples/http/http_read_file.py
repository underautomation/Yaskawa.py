"""
HTTP - Read a File
==================
Read the text of a file of the controller through its web server, and save it on the PC.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - HTTP: Read a File")
print("=" * 60)

robot = connect_robot(http=True)

try:
    name = input("File name [VAR.DAT]: ").strip() or "VAR.DAT"
    content = robot.http.get_file(name)
    lines = content.splitlines()
    print(f"\n{name}: {len(content)} characters, {len(lines)} lines\n")
    for line in lines[:20]:
        print(f"  {line}")

    if input("\nSave on the PC? (y/N): ").strip().lower() == "y":
        with open(name, "w", newline="") as f:
            f.write(content)
        print(f"Saved to {os.path.abspath(name)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
