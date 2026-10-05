"""
Ethernet Server - Inputs and Outputs
====================================
Read I/O signals by their number (#10010...) and write the network inputs (#27010 to
#29567) through the Ethernet Server.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  YASKAWA SDK - Ethernet Server: Inputs and Outputs")
print("=" * 60)

robot = connect_robot(e_server=True)

try:
    address = int(input("First signal, number ending with 0 [10010]: ").strip() or "10010")
    count = int(input("Number of bytes (8 signals each) [2]: ").strip() or "2")

    io = robot.e_server.read_io(address, count)
    for i, value in enumerate(io.data):
        first = address + i * 10
        bits = " ".join("1" if value & (1 << b) else "0" for b in range(8))
        print(f"  #{first:05d} to #{first + 7:05d}: {bits}")

    answer = input("\nWrite a network input byte (#27010...)? (y/N): ").strip().lower()
    if answer == "y":
        target = int(input("Signal number [27010]: ").strip() or "27010")
        value = int(input("Byte value (0 to 255): ").strip())
        robot.e_server.write_io(target, [value])
        print(f"#{target:05d}: {robot.e_server.read_io(target, 1).data[0]}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
