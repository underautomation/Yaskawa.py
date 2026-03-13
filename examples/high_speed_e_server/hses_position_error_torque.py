"""
HSES - Get Position Error and Torque
======================================
Read the position error (difference between command and actual)
and the torque for each axis.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.yaskawa.high_speed_e_server.robot_control_group import RobotControlGroup

print("=" * 60)
print("  YASKAWA SDK - HSES: Position Error & Torque")
print("=" * 60)

robot = connect_robot()

try:
    print("\nReading position error...")
    error = robot.high_speed_e_server.get_position_error(RobotControlGroup.DefaultRobotPulse)
    print(f"  Position Error (pulse):")
    for i, val in enumerate(error.axes, 1):
        print(f"    Axis {i} = {val}")

    print("\nReading torque...")
    torque = robot.high_speed_e_server.get_torque(RobotControlGroup.DefaultRobotPulse)
    print(f"  Torque (%):")
    for i, val in enumerate(torque.axes, 1):
        print(f"    Axis {i} = {val}%")

finally:
    robot.disconnect()
    print("\nDisconnected.")
