"""
HSES - Read and Write Byte Variables
======================================
Read and write byte variables (B variables) on the robot.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - HSES: Read/Write Byte Variables")
print("=" * 60)

robot = connect_robot()

try:
    while True:
        print("\n  1. Read byte variables")
        print("  2. Write byte variable")
        print("  0. Quit")
        choice = input("\nChoice: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            start_str = input("Start index (default 0): ").strip()
            start = int(start_str) if start_str else 0
            count_str = input("Count (default 10): ").strip()
            count = int(count_str) if count_str else 10

            print(f"\nReading byte variables {start} to {start + count - 1}...")
            data = robot.high_speed_e_server.read_byte(start, count)
            for i, val in enumerate(data.value, start=start):
                print(f"  B[{i}] = {val}")

        elif choice == "2":
            idx_str = input("Variable index: ").strip()
            if not idx_str:
                continue
            idx = int(idx_str)

            val_str = input(f"Values for B[{idx}] (0-255, comma-separated, must be even count e.g. 0,255): ").strip()
            if not val_str:
                continue

            values = [int(v.strip()) for v in val_str.split(",")]
            if len(values) % 2 != 0:
                print(f"  Error: you entered {len(values)} value(s), but the count must be even (2, 4, 6, ...).")
                continue
            print(f"\nWriting {values} at index {idx}...")
            result = robot.high_speed_e_server.write_byte(idx, values)
            print("Done.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
