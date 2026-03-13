"""
HSES - Read Position Variables
=================================
Read robot position variables stored in the controller.
Shows Cartesian position data for each variable.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - HSES: Read Position Variables")
print("=" * 60)

robot = connect_robot()

try:
    start_str = input("Start index (default 0): ").strip()
    start = int(start_str) if start_str else 0
    count_str = input("Count (default 5): ").strip()
    count = int(count_str) if count_str else 5

    print(f"\nReading position variables {start} to {start + count - 1}...")
    data = robot.high_speed_e_server.read_position_variable(start, count)

    for i, pos in enumerate(data.value, start=start):
        print(f"\n  P[{i}]:")
        print(f"    Axis1  = {pos.axis1:>10.3f}")
        print(f"    Axis2  = {pos.axis2:>10.3f}")
        print(f"    Axis3  = {pos.axis3:>10.3f}")
        print(f"    Axis4  = {pos.axis4:>10.3f}")
        print(f"    Axis5  = {pos.axis5:>10.3f}")
        print(f"    Axis6  = {pos.axis6:>10.3f}")
        print(f"    Data Type  = {pos.data_type}")
        print(f"    Form       = {pos.form}")
        print(f"    Tool Number = {pos.tool_number}")
        print(f"    User Coordinate = {pos.user_coordinate_number}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
