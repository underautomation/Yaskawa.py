"""
HSES - Read and Write String Variables
========================================
Read and write 32-byte string (character) variables on the robot.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - HSES: Read/Write String Variables")
print("=" * 60)

robot = connect_robot()

try:
    while True:
        print("\n  1. Read strings")
        print("  2. Write string")
        print("  0. Quit")
        choice = input("\nChoice: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            start_str = input("Start index (default 0): ").strip()
            start = int(start_str) if start_str else 0
            count_str = input("Count (default 5): ").strip()
            count = int(count_str) if count_str else 5

            print(f"\nReading string variables {start} to {start + count - 1}...")
            data = robot.high_speed_e_server.read32_bytes_char(start, count)
            for i, val in enumerate(data.value, start=start):
                print(f"  S[{i}] = \"{val}\"")

        elif choice == "2":
            idx_str = input("Variable index: ").strip()
            if not idx_str:
                continue
            idx = int(idx_str)

            val = input(f"String value for S[{idx}] (max 32 chars): ").strip()
            print(f"\nWriting \"{val}\" at index {idx}...")
            result = robot.high_speed_e_server.write32_bytes_char(idx, [val])
            print("Done.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
