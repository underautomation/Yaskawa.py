"""
HSES - File Operations
========================
List, download, upload, and delete files on the robot controller.
Supports job files and other controller files.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - HSES: File Operations")
print("=" * 60)

robot = connect_robot()

try:
    while True:
        print("\n  1. List files")
        print("  2. Download file")
        print("  3. Upload file")
        print("  4. Delete file")
        print("  0. Quit")
        choice = input("\nChoice: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            pattern = input("File pattern (e.g. *.JBI) [*.*]: ").strip()
            if not pattern:
                pattern = "*.*"

            print(f"\nListing files matching '{pattern}'...")
            file_list = robot.high_speed_e_server.get_file_list(pattern)
            print(f"\nFiles found: {len(file_list.files)}")
            for f in file_list.files:
                print(f"  {f}")

        elif choice == "2":
            name = input("File name to download: ").strip()
            if not name:
                continue

            print(f"\nDownloading '{name}'...")
            content = robot.high_speed_e_server.get_file(name)
            print(f"File size: {len(content.content_raw)} bytes")

            save = input("Save to local file? (y/N): ").strip().lower()
            if save == 'y':
                local_path = input("Local file path: ").strip()
                if local_path:
                    with open(local_path, 'w', encoding='utf-8', newline='') as f:
                        f.write(content.content)
                    print(f"Saved to {local_path}")

        elif choice == "3":
            local_path = input("Local file path to upload: ").strip()
            if not local_path or not os.path.exists(local_path):
                print("File not found.")
                continue

            remote_name = input(f"Remote file name [{os.path.basename(local_path)}]: ").strip()
            if not remote_name:
                remote_name = os.path.basename(local_path)

            with open(local_path, 'r', encoding='utf-8', newline='') as f:
                file_content = f.read()

            print(f"\nUploading '{remote_name}' ({len(file_content)} bytes)...")
            result = robot.high_speed_e_server.load_file(remote_name, file_content)
            print("Done.")

        elif choice == "4":
            name = input("File name to delete: ").strip()
            if not name:
                continue

            confirm = input(f"Delete '{name}' from robot? (y/N): ").strip().lower()
            if confirm == 'y':
                print(f"\nDeleting '{name}'...")
                result = robot.high_speed_e_server.delete_file(name)
                print("Done.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
