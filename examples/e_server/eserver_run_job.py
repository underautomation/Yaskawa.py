"""
Ethernet Server - Run a Job
===========================
Select a job, switch the servo on, start the job and wait for its end in one call,
through the Ethernet Server. The robot moves: check the cell first.
Needs the play mode and the remote mode.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from UnderAutomation.Yaskawa.HostControl import HostControlException

print("=" * 60)
print("  YASKAWA SDK - Ethernet Server: Run a Job")
print("=" * 60)

robot = connect_robot(e_server=True)

try:
    status = robot.e_server.get_status_information()
    if not status.play or not status.command_remote:
        print("The controller must be in play mode and in remote mode.")
        raise SystemExit(1)

    name = input("Job name (without .JBI): ").strip()
    timeout = int(input("Maximum time in seconds [60]: ").strip() or "60")

    confirm = input(f"Start {name}? The robot will move. (y/N): ").strip().lower()
    if confirm == "y":
        try:
            robot.e_server.select_job(name, 0)
            robot.e_server.set_servo(True)
            robot.e_server.start_job()
            print("Running...")
            completed = robot.e_server.wait_for_job_completion(timeout)
            print("Job completed." if completed else "Job stopped or timeout.")
        except HostControlException as ex:
            print(f"Refused by the controller: {ex.Message}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
