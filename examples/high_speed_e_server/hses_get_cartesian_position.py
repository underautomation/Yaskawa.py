"""
HSES - Get Cartesian Position
===============================
Read the current robot TCP position in Cartesian coordinates (X, Y, Z, Rx, Ry, Rz).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - HSES: Get Cartesian Position")
print("=" * 60)

robot = connect_robot()

try:
    print("Reading Cartesian position...")
    pos = robot.high_speed_e_server.get_robot_cartesian_position()

    print(f"\nCartesian Position:")
    print(f"  X  = {pos.x:>10.3f} mm")
    print(f"  Y  = {pos.y:>10.3f} mm")
    print(f"  Z  = {pos.z:>10.3f} mm")
    print(f"  Rx = {pos.rx:>10.3f} deg")
    print(f"  Ry = {pos.ry:>10.3f} deg")
    print(f"  Rz = {pos.rz:>10.3f} deg")
    print(f"\n  Tool Number            : {pos.tool_number}")
    print(f"  User Coordinate Number : {pos.user_coordinate_number}")
    print(f"  Data Type              : {pos.data_type}")
    print(f"  Posture (Form)         : {pos.form}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
