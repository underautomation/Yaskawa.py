"""
Ethernet Server - Status and Alarms
===================================
Read the status of the controller and the active error and alarms with their text,
through the Ethernet Server (TCP 80).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - Ethernet Server: Status and Alarms")
print("=" * 60)

robot = connect_robot(e_server=True)

try:
    status = robot.e_server.get_status_information()
    print("\nStatus:")
    print(f"  Teach / Play     : {status.teach} / {status.play}")
    print(f"  Command remote   : {status.command_remote}")
    print(f"  Servo on         : {status.servo_on}")
    print(f"  Running          : {status.running}")
    print(f"  Speed limit      : {status.speed_limit}")
    print(f"  Hold (pendant)   : {status.in_hold_status_pendant}")
    print(f"  Hold (external)  : {status.in_hold_status_externally}")
    print(f"  Hold (command)   : {status.in_hold_status_by_command}")
    print(f"  Alarm / error    : {status.alarming} / {status.error_occurring}")

    alarms = robot.e_server.get_alarm_with_messages()
    print(f"\nActive alarms: {alarms.alarm_count}")
    if alarms.error is not None and alarms.error.code != 0:
        print(f"  Error {alarms.error.code}: {alarms.error.message}")
    for alarm in alarms.alarms:
        if alarm.code != 0:
            print(f"  Alarm {alarm.code} ({alarm.sub_code}): {alarm.message}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
