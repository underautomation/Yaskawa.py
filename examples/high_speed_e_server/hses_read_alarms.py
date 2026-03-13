"""
HSES - Read Alarms
====================
Read active alarms from the robot controller.
Shows alarm code, type, message, and timestamp.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.yaskawa.high_speed_e_server.robot_recent_alarm import RobotRecentAlarm

print("=" * 60)
print("  YASKAWA SDK - HSES: Read Alarms")
print("=" * 60)

robot = connect_robot()

try:
    print("Reading alarms...")

    alarm_slots = [
        RobotRecentAlarm.Latest,
        RobotRecentAlarm.SecondLatest,
        RobotRecentAlarm.ThirdLatest,
        RobotRecentAlarm.FourthLatest,
    ]

    found_alarm = False
    for slot in alarm_slots:
        try:
            alarm = robot.high_speed_e_server.get_alarm(slot)
            if alarm and alarm.code != 0:
                found_alarm = True
                print(f"\n  {slot.name}:")
                print(f"    Code    : {alarm.code}")
                print(f"    Type    : {alarm.type}")
                print(f"    Data    : {alarm.data}")
                print(f"    Text    : {alarm.text}")
                print(f"    Time    : {alarm.occurring_time}")
        except Exception as e:
            print(f"  Could not read {slot.name}: {e}")

    if not found_alarm:
        print("\nNo active alarms.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
