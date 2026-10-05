"""
Kinematics - Forward and Inverse
================================
Compute the flange position from joint angles, then every joint solution for this position,
offline, for a robot model of the catalog. No robot is needed.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from underautomation.yaskawa.common.dh_parameters import DhParameters
from underautomation.yaskawa.common.joints_angles import JointsAngles
from underautomation.yaskawa.kinematics.kinematics_utils import KinematicsUtils

print("=" * 60)
print("  YASKAWA SDK - Kinematics: Forward and Inverse")
print("=" * 60)

name = input("Robot model [GP7]: ").strip() or "GP7"
dh = DhParameters.from_arm_kinematic_model_name(name)
if dh is None:
    print(f"{name} is not in the catalog.")
    raise SystemExit(1)
print(f"{dh} ({dh.kinematics_category.name})")

text = input("Joint angles S L U R B T in degrees [0 0 0 0 -90 0]: ").strip() or "0 0 0 0 -90 0"
s, l, u, r, b, t = (float(v) for v in text.split())

flange = KinematicsUtils.forward_kinematics(JointsAngles(s, l, u, r, b, t), dh)
print(f"\nFlange: {flange}")

solutions = KinematicsUtils.inverse_kinematics(flange, dh)
print(f"\n{len(solutions)} joint solutions for this position:")
for solution in solutions:
    print(f"  {solution}")
