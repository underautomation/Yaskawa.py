"""
HSES - Servo ON/OFF Command
==============================
Send servo power ON or OFF commands to the robot.
Requires the robot to be in remote mode.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.yaskawa.high_speed_e_server.on_off_command_type import OnOffCommandType

print("=" * 60)
print("  YASKAWA SDK - HSES: Servo ON/OFF Command")
print("=" * 60)

robot = connect_robot()

try:
    # Show current status
    status = robot.high_speed_e_server.get_status_information()
    print(f"\nCurrent servo state: {'ON' if status.servo_on else 'OFF'}")

    print("\n  1. Servo ON")
    print("  2. Servo OFF")
    choice = input("\nChoice: ").strip()

    if choice == "1":
        print("\nSending Servo ON...")
        result = robot.high_speed_e_server.servo_command(OnOffCommandType.Servo, True)
        print("Done.")
    elif choice == "2":
        print("\nSending Servo OFF...")
        result = robot.high_speed_e_server.servo_command(OnOffCommandType.Servo, False)
        print("Done.")
    else:
        print("Invalid choice.")

    # Check new status
    status = robot.high_speed_e_server.get_status_information()
    print(f"New servo state: {'ON' if status.servo_on else 'OFF'}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
