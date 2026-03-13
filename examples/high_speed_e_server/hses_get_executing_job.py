"""
HSES - Get Executing Job
==========================
Read information about the currently executing job.
Shows job name, current line, step, and speed override.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - HSES: Get Executing Job")
print("=" * 60)

robot = connect_robot()

try:
    print("Reading executing job information...")
    job = robot.high_speed_e_server.get_executing_job_information()

    print(f"\nExecuting Job:")
    print(f"  Name           : {job.name}")
    print(f"  Line           : {job.line}")
    print(f"  Step           : {job.step}")
    print(f"  Speed Override : {job.speed_override}%")

finally:
    robot.disconnect()
    print("\nDisconnected.")
