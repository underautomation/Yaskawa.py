"""
HSES - Select and Start Job
=============================
Select a job by name and optionally start it.
Requires the robot to be in remote mode with proper permissions.
"""
import sys, os

from underautomation.yaskawa.high_speed_e_server.on_off_command_type import OnOffCommandType
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - HSES: Select and Start Job")
print("=" * 60)

robot = connect_robot()

try:
    job_name = input("Enter job name to select (e.g. JOB1): ").strip()
    if not job_name:
        print("No job name provided.")
    else:
        line_str = input("Start line [1]: ").strip()
        line = int(line_str) if line_str else 1

        print(f"\nSelecting job '{job_name}' at line {line}...")
        result = robot.high_speed_e_server.select_job(job_name, line)
        print(f"Selected.")

        start = input("\nServo On and Start the job? (y/N): ").strip().lower()
        if start == 'y' or start == '':
            print('Servo On...')
            robot.high_speed_e_server.servo_command(OnOffCommandType.Servo, True)
            print(f"Servo On OK.")
            print("Starting job...")
            result = robot.high_speed_e_server.start_job()
            print(f"Started.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
