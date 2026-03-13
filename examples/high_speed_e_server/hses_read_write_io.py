"""
HSES - Read and Write I/O
===========================
Read and write digital I/O signals on the robot.
Supports various I/O types: General, Universal, External, etc.
"""
import sys, os

from underautomation.yaskawa.common.io_helpers import IoHelpers
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.yaskawa.common.io_type import IOType

print("=" * 60)
print("  YASKAWA SDK - HSES: Read and Write I/O")
print("=" * 60)

robot = connect_robot()

# Build a list of available I/O types for the menu
io_types = [
    ("General Input",        IOType.GeneralInput),
    ("General Output",       IOType.GeneralOutput),
    ("External Input",       IOType.ExternalInput),
    ("External Output",      IOType.ExternalOutput),
    ("Specific Input",       IOType.SpecificInput),
    ("Specific Output",      IOType.SpecificOutput),
    ("Network Input",        IOType.NetworkInput),
    ("Network Output",       IOType.NetworkOutput),
]

try:
    while True:
        print("\n  1. Read I/O")
        print("  2. Write Network Input")
        print("  0. Quit")
        choice = input("\nChoice: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            print("\nI/O Types:")
            for i, (name, _) in enumerate(io_types, 1):
                print(f"  {i}. {name}")

            type_str = input("Select I/O type: ").strip()
            if not type_str or not type_str.isdigit():
                continue
            type_idx = int(type_str) - 1
            if type_idx < 0 or type_idx >= len(io_types):
                print("Invalid selection.")
                continue

            io_name, io_type = io_types[type_idx]

            group_str = input("Group number (default 1): ").strip()
            group = int(group_str) if group_str else 1
            count_str = input("Count (default 1): ").strip()
            count = int(count_str) if count_str else 1

            print(f"\nReading {io_name} group {group}, count {count}...")
            data = robot.high_speed_e_server.read_io(io_type, group, count)
            for i, val in enumerate(data.value):
                addr = int(IoHelpers.convert_io_group_to_bit_address(io_type, group+i, 0) / 10)
                print(f"  #{addr:05d} = {val}")

        elif choice == "2":
            print("\nWrite Network Input (via write_io_network_input)")

            group_str = input("Group number (default 1): ").strip()
            group = int(group_str) if group_str else 1

            val_str = input("Values (comma-separated bytes, e.g. 0,255): ").strip()
            if not val_str:
                continue
            values = [int(v.strip()) for v in val_str.split(",")]

            print(f"\nWriting Network Input group {group}: {values}...")
            result = robot.high_speed_e_server.write_io_network_input(group, values)
            print("Done.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
