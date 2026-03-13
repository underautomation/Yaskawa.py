"""
HSES - Reset Alarm
====================
Reset an active alarm on the robot controller.
Supports standard reset and error reset.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.yaskawa.high_speed_e_server.alarm_reset_type import AlarmResetType

print("=" * 60)
print("  YASKAWA SDK - HSES: Reset Alarm")
print("=" * 60)

robot = connect_robot()

try:
    print("\nAlarm reset types:")
    print("  1. Reset (standard alarm reset)")
    print("  2. Error Reset")

    choice = input("\nSelect reset type [1]: ").strip()

    if choice == "2":
        reset_type = AlarmResetType.ErrorReset
        type_name = "Error Reset"
    else:
        reset_type = AlarmResetType.Reset
        type_name = "Reset"

    print(f"\nPerforming {type_name}...")
    result = robot.high_speed_e_server.alarm_reset(reset_type)
    print("Done.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
