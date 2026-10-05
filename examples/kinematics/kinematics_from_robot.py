"""
Kinematics - Model of the Connected Robot
=========================================
Download ALL.PRM over FTP, read the DH parameters of the robot from it, then compute
the joint solutions of the current position. The download takes about 13 s.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.yaskawa.common.dh_parameters import DhParameters
from underautomation.yaskawa.kinematics.kinematics_utils import KinematicsUtils

print("=" * 60)
print("  YASKAWA SDK - Kinematics: Model of the Connected Robot")
print("=" * 60)

robot = connect_robot(ftp=True)

try:
    print("Downloading ALL.PRM...")
    dh = DhParameters.from_prm_content(robot.ftp.get_file("ALL.PRM"))
    print(f"{dh} ({dh.kinematics_category.name})")

    position = robot.high_speed_e_server.get_robot_cartesian_position()
    print(f"\nCurrent position (tool {position.tool_number}): "
          f"X={position.x} Y={position.y} Z={position.z} Rx={position.rx} Ry={position.ry} Rz={position.rz}")
    if position.tool_number != 0:
        print("The kinematics give the flange: select the tool 0 for an exact comparison.")

    solutions = KinematicsUtils.inverse_kinematics(position, dh)
    print(f"\n{len(solutions)} joint solutions:")
    for solution in solutions:
        print(f"  {solution}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
