"""
HSES - Get Joint Position
===========================
Read the current robot joint position (pulse values for each axis).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - HSES: Get Joint Position")
print("=" * 60)

robot = connect_robot()

try:
    print("Reading joint position...")
    joint = robot.high_speed_e_server.get_robot_joint_position()

    print(f"\nJoint Position (pulse):")
    axes = joint.axes
    for i, val in enumerate(axes, 1):
        print(f"  Axis {i} = {val}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
