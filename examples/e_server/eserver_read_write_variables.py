"""
Ethernet Server - Variables
===========================
Read the B, I, D, R and S variables through the Ethernet Server, and write one B variable
after a confirmation. The write needs the remote mode.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - Ethernet Server: Variables")
print("=" * 60)

robot = connect_robot(e_server=True)

try:
    first = int(input("First index [0]: ").strip() or "0")
    count = int(input("Number of variables [4]: ").strip() or "4")

    print(f"\nB{first:03d}.. : {list(robot.e_server.read_byte(first, count))}")
    print(f"I{first:03d}.. : {list(robot.e_server.read_integer(first, count))}")
    print(f"D{first:03d}.. : {list(robot.e_server.read_double_integer(first, count))}")
    print(f"R{first:03d}.. : {list(robot.e_server.read_real(first, count))}")
    print(f"S{first:03d}.. : {list(robot.e_server.read16_bytes_char(first, count))}")

    answer = input("\nWrite a B variable? (y/N): ").strip().lower()
    if answer == "y":
        index = int(input("Index of the B variable: ").strip())
        value = int(input("Value (0 to 255): ").strip())
        robot.e_server.write_byte(index, [value])
        print(f"B{index:03d} = {robot.e_server.read_byte(index, 1)[0]}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
