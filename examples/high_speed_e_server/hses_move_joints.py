"""
HSES - Move Joints
====================
Move the robot by specifying joint pulse values for each axis.
Requires the robot to be in remote mode with servo ON.

WARNING: This will physically move the robot. Ensure the path is clear.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.yaskawa.high_speed_e_server.position_command_classification import PositionCommandClassification
from underautomation.yaskawa.high_speed_e_server.position_command_type import PositionCommandType

print("=" * 60)
print("  YASKAWA SDK - HSES: Move Joints")
print("=" * 60)
print("\n  WARNING: This will physically move the robot!")
print("  Make sure the robot is in a safe state.\n")

robot = connect_robot()

try:
    # Show current position
    joint = robot.high_speed_e_server.get_robot_joint_position()
    axes = joint.axes
    print(f"Current joint position (pulse):")
    for i, val in enumerate(axes, 1):
        print(f"  Axis {i} = {val}")

    print("\nEnter target pulse values (comma-separated, e.g. 0,0,0,0,0,0):")
    vals_str = input("  Axes pulse: ").strip()
    if not vals_str:
        print("No values provided.")
    else:
        pulse_values = [int(v.strip()) for v in vals_str.split(",")]

        speed_str = input("  Speed % [5]: ").strip()
        speed = float(speed_str) if speed_str else 5

        confirm = input(f"\nMove joints to {pulse_values} at speed {speed}%? (y/N): ").strip().lower()
        if confirm == 'y' or confirm == '':
            print("\nMoving robot joints...")
            result = robot.high_speed_e_server.move_joints(
                axesPulse=pulse_values,
                classification=PositionCommandClassification.LinkPercent,
                speed=speed,
                commandtype=PositionCommandType.LinkAbsolute,
            )
            print("Done.")
        else:
            print("Move cancelled.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
