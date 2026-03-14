"""
HSES - Read and Write Position Variables
==========================================
Read and write robot position variables (P variables) stored in the controller.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.yaskawa.high_speed_e_server.robot_position_int_data import RobotPositionIntData
from underautomation.yaskawa.high_speed_e_server.robot_position_data_type import RobotPositionDataType
from underautomation.yaskawa.high_speed_e_server.robot_posture import RobotPosture
from underautomation.yaskawa.yaskawa_robot import YaskawaRobot

print("=" * 60)
print("  YASKAWA SDK - HSES: Read/Write Position Variables")
print("=" * 60)

"""robot = connect_robot()"""
robot = YaskawaRobot()

try:
    while True:
        print("\n  1. Read position variables")
        print("  2. Write position variable")
        print("  0. Quit")
        choice = input("\nChoice: ").strip()

        if choice == "0":
            break

        elif choice == "1":
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

        elif choice == "2":
            idx_str = input("Variable index: ").strip()
            if not idx_str:
                continue
            idx = int(idx_str)

            # Data type selection
            print("\n  Data type:")
            print("    1. PulseValue")
            print("    2. BaseCoordinateValue")
            print("    3. RobotCoordinateValue")
            print("    4. UserCoordinateValue")
            dt_str = input("  Data type (1-4): ").strip()
            if not dt_str or dt_str == "5":
                print("Invalid data type.")
                continue

            data_type_map = {
                "1": RobotPositionDataType.PulseValue,
                "2": RobotPositionDataType.BaseCoordinateValue,
                "3": RobotPositionDataType.RobotCoordinateValue,
                "4": RobotPositionDataType.UserCoordinateValue,
            }
            if dt_str not in data_type_map:
                print("Invalid data type.")
                continue
            data_type = data_type_map[dt_str]

            # Tool number (not needed for PulseValue)
            tool_number = 0
            if data_type != RobotPositionDataType.PulseValue:
                tool_str = input("Tool number (default 0): ").strip()
                tool_number = int(tool_str) if tool_str else 0

            # User coordinate number (only for UserCoordinateValue)
            user_coord = 0
            if data_type == RobotPositionDataType.UserCoordinateValue:
                uc_str = input("User coordinate number (default 0): ").strip()
                user_coord = int(uc_str) if uc_str else 0

            # Axis values
            axis1 = int(input("Axis1: ").strip())
            axis2 = int(input("Axis2: ").strip())
            axis3 = int(input("Axis3: ").strip())
            axis4 = int(input("Axis4: ").strip())
            axis5 = int(input("Axis5: ").strip())
            axis6 = int(input("Axis6: ").strip())

            # Form (posture)
            form_value = 0
            if data_type != RobotPositionDataType.PulseValue:
                form_str = input("Form as integer (default 0): ").strip()
                form_value = int(form_str) if form_str else 0

            # Build position data
            pos = RobotPositionIntData(None)
            pos.data_type = data_type
            pos.axis1 = axis1
            pos.axis2 = axis2
            pos.axis3 = axis3
            pos.axis4 = axis4
            pos.axis5 = axis5
            pos.axis6 = axis6
            pos.tool_number = tool_number
            pos.user_coordinate_number = user_coord
            pos.form = RobotPosture.from_integer(form_value)

            print(f"\nWriting position variable P[{idx}]...")
            result = robot.high_speed_e_server.write_position_variable(idx, [pos])
            print("Done.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
