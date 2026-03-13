"""
HSES - Get System Information
===============================
Read system information from the robot controller.
Shows software version, system name, and parameter info.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.yaskawa.high_speed_e_server.robot_system_type_data import RobotSystemTypeData

print("=" * 60)
print("  YASKAWA SDK - HSES: Get System Information")
print("=" * 60)

robot = connect_robot()

try:
    print("Reading system information...")


    try:
        info = robot.high_speed_e_server.get_system_information(RobotSystemTypeData.Default)
        print(f"\n  System Information:")
        print(f"    Software Version : {info.software_version}")
        print(f"    Name             : {info.name}")
        print(f"    Parameter        : {info.parameter}")
    except Exception as e:
        print(f"  Could not read system information: {e}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
