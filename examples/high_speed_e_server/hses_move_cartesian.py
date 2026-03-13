"""
HSES - Move Cartesian
=======================
Move the robot to a Cartesian position (X, Y, Z, Rx, Ry, Rz).
Requires the robot to be in remote mode with servo ON.

WARNING: This will physically move the robot. Ensure the path is clear.
"""
import sys, os

from underautomation.yaskawa.high_speed_e_server.on_off_command_type import OnOffCommandType
from underautomation.yaskawa.high_speed_e_server.position_command_type import PositionCommandType
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.yaskawa.high_speed_e_server.position_command_classification import PositionCommandClassification
from underautomation.yaskawa.high_speed_e_server.position_command_operation_coordinate import PositionCommandOperationCoordinate

print("=" * 60)
print("  YASKAWA SDK - HSES: Move Cartesian")
print("=" * 60)
print("\n  WARNING: This will physically move the robot!")
print("  Make sure the robot is in a safe state.\n")

robot = connect_robot()

try:
    # Show current position first
    pos = robot.high_speed_e_server.get_robot_cartesian_position()
    print(f"Current position:")
    print(f"  X={pos.x:.3f}  Y={pos.y:.3f}  Z={pos.z:.3f}")
    print(f"  Rx={pos.rx:.3f}  Ry={pos.ry:.3f}  Rz={pos.rz:.3f}")

    print("\nEnter target position (press Enter to keep current value):")
    x_str = input(f"  X [{pos.x:.3f}]: ").strip()
    y_str = input(f"  Y [{pos.y:.3f}]: ").strip()
    z_str = input(f"  Z [{pos.z:.3f}]: ").strip()
    rx_str = input(f"  Rx [{pos.rx:.3f}]: ").strip()
    ry_str = input(f"  Ry [{pos.ry:.3f}]: ").strip()
    rz_str = input(f"  Rz [{pos.rz:.3f}]: ").strip()

    x = float(x_str) if x_str else pos.x
    y = float(y_str) if y_str else pos.y
    z = float(z_str) if z_str else pos.z
    rx = float(rx_str) if rx_str else pos.rx
    ry = float(ry_str) if ry_str else pos.ry
    rz = float(rz_str) if rz_str else pos.rz

    speed_str = input("  Speed % [5]: ").strip()
    speed = float(speed_str) if speed_str else 5

    confirm = input(f"\nServo On and Move to X={x} Y={y} Z={z} Rx={rx} Ry={ry} Rz={rz} at {speed} %? (y/N): ").strip().lower()
    
    robot.high_speed_e_server.servo_command(OnOffCommandType.Servo, True)
    
    if confirm == 'y' or confirm == '':
        print("\nMoving robot...")
        result = robot.high_speed_e_server.move_cartesian(
            x=x, y=y, z=z,
            rx=rx, ry=ry, rz=rz,
            speed=speed,
            posture=pos.form,
            commandtype= PositionCommandType.LinkAbsolute,
            classification=PositionCommandClassification.LinkPercent,
            coordinate=PositionCommandOperationCoordinate.Base,
        )
        print("Done.")
    else:
        print("Move cancelled.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
