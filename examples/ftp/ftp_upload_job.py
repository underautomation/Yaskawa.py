"""
FTP - Upload a Job
==================
Send a job of the PC to the controller over FTP with the account ftp. The controller
does not overwrite a job by FTP: the existing job is deleted first, after a confirmation.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from UnderAutomation.Yaskawa.Ftp import FtpException

print("=" * 60)
print("  YASKAWA SDK - FTP: Upload a Job")
print("=" * 60)

robot = connect_robot(ftp=True, ftp_user="ftp")

try:
    local_path = input("Local job file (.JBI): ").strip()
    if not os.path.isfile(local_path):
        print("File not found.")
        raise SystemExit(1)

    name = os.path.basename(local_path)
    remote_path = "/JOB/" + name

    if robot.ftp.file_exists(remote_path):
        confirm = input(f"{name} exists on the controller. Delete and replace it? (y/N): ").strip().lower()
        if confirm != "y":
            raise SystemExit(0)
        robot.ftp.delete_file(name)

    try:
        robot.ftp.upload_file_from_local(local_path)
        print(f"{name} sent.")
    except FtpException as ex:
        print(f"{ex.Operation} failed: {ex.Reason} ({ex.ReplyMessage})")

finally:
    robot.disconnect()
    print("\nDisconnected.")
