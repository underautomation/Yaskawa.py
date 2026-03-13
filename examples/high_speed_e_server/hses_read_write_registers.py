"""
HSES - Read and Write Registers
=================================
Read and write numeric registers (register variables) on the robot.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - HSES: Read and Write Registers")
print("=" * 60)

robot = connect_robot()

try:
    while True:
        print("\n  1. Read registers")
        print("  2. Write register")
        print("  0. Quit")
        choice = input("\nChoice: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            start_str = input("Start index (default 0): ").strip()
            start = int(start_str) if start_str else 0
            count_str = input("Count (default 5): ").strip()
            count = int(count_str) if count_str else 5

            print(f"\nReading registers {start} to {start + count - 1}...")
            data = robot.high_speed_e_server.read_register(start, count)
            for i, val in enumerate(data.value, start=start):
                print(f"  Register[{i}] = {val}")

        elif choice == "2":
            idx_str = input("Register index: ").strip()
            if not idx_str:
                continue
            idx = int(idx_str)

            val_str = input(f"Value for Register[{idx}]: ").strip()
            if not val_str:
                continue

            values = [int(v.strip()) for v in val_str.split(",")]
            print(f"\nWriting {values} at index {idx}...")
            result = robot.high_speed_e_server.write_register(idx, values)
            print("Done.")

            # Read back
            readback = robot.high_speed_e_server.read_register(idx, len(values))
            print("Read back:")
            for i, val in enumerate(readback.value, start=idx):
                print(f"  Register[{i}] = {val}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
