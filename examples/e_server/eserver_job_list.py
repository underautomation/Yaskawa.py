"""
Ethernet Server - Job List
==========================
List the jobs of the controller with an optional filter, and read the executing job,
through the Ethernet Server.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - Ethernet Server: Job List")
print("=" * 60)

robot = connect_robot(e_server=True)

try:
    pattern = input("Job name filter, * for every job [*]: ").strip() or "*"
    directory = robot.e_server.get_job_directory(pattern)
    names = list(directory.job_names)
    print(f"\n{len(names)} job(s):")
    for name in names:
        print(f"  {name}")

    job = robot.e_server.get_executing_job_information()
    print(f"\nExecuting job: {job.name}, line {job.line}, step {job.step}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
