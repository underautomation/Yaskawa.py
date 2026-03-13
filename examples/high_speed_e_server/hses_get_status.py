"""
HSES - Get Robot Status
========================
Read the robot status information via High Speed Ethernet Server.
Shows operating mode, servo state, alarms, hold status, and more.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - HSES: Get Robot Status")
print("=" * 60)

robot = connect_robot()

try:
    print("Reading status information...")
    status = robot.high_speed_e_server.get_status_information()

    print(f"\nRobot Status:")
    print(f"  Mode:")
    print(f"    Teach            : {status.teach}")
    print(f"    Play             : {status.play}")
    print(f"    Automatic        : {status.automatic}")
    print(f"    Remote Command   : {status.command_remote}")
    print(f"  Execution:")
    print(f"    Running          : {status.running}")
    print(f"    Step             : {status.step}")
    print(f"    Cycle            : {status.cycle}")
    print(f"  Servo:")
    print(f"    Servo ON         : {status.servo_on}")
    print(f"  Hold Status:")
    print(f"    Pendant Hold     : {status.in_hold_status_pendant}")
    print(f"    External Hold    : {status.in_hold_status_externally}")
    print(f"    Command Hold     : {status.in_hold_status_by_command}")
    print(f"  Safety:")
    print(f"    Alarming         : {status.alarming}")
    print(f"    Error Occurring  : {status.error_occurring}")
    print(f"    Guard Safe Op    : {status.in_guard_safe_operation}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
