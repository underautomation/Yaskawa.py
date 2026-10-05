"""
Ethernet Server - Positions and Torque
======================================
Read the joint pulses, the Cartesian position in the base and robot frames, the posture,
the torque and the encoder temperatures through the Ethernet Server.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.yaskawa.host_control.host_control_coordinate_system import HostControlCoordinateSystem

print("=" * 60)
print("  YASKAWA SDK - Ethernet Server: Positions and Torque")
print("=" * 60)

robot = connect_robot(e_server=True)

try:
    joints = robot.e_server.get_robot_joint_position()
    print(f"\nJoints (pulses): S={joints.s} L={joints.l} U={joints.u} R={joints.r} B={joints.b} T={joints.t}")

    for frame in (HostControlCoordinateSystem.Base, HostControlCoordinateSystem.Robot):
        tcp = robot.e_server.get_robot_cartesian_position(frame)
        print(f"{frame.name:5} frame (mm, deg): X={tcp.x:.3f} Y={tcp.y:.3f} Z={tcp.z:.3f} "
              f"Rx={tcp.rx:.4f} Ry={tcp.ry:.4f} Rz={tcp.rz:.4f}")

    tcp = robot.e_server.get_robot_cartesian_position()
    print(f"Posture: front={tcp.is_front} upper arm={tcp.is_upper_arm} flip={tcp.is_flip}")

    torque = robot.e_server.get_torque()
    temperatures = robot.e_server.get_encoder_temperature()
    print("\nAxis  Torque (%)  Encoder (C)")
    for axis in range(6):
        print(f"  {axis + 1}   {torque.values[axis]:10.1f}  {temperatures.values[axis]:11.1f}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
