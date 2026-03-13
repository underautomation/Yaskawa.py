"""
HSES - Display Message on Pendant
====================================
Send a text message to be displayed on the robot teach pendant.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - HSES: Display Message on Pendant")
print("=" * 60)

robot = connect_robot()

try:
    while True:
        message = input("\nEnter message to display on pendant (q to quit): ").strip()
        if message.lower() == 'q':
            break
        if not message:
            print("  Message cannot be empty.")
            continue

        print(f"Sending message: \"{message}\"")
        result = robot.high_speed_e_server.display(message)
        print("Done.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
