from underautomation.yaskawa.connect_parameters import ConnectParameters
from underautomation.yaskawa.high_speed_e_server.alarm_reset_type import AlarmResetType
from underautomation.yaskawa.high_speed_e_server.position_command_classification import PositionCommandClassification
from underautomation.yaskawa.yaskawa_robot import YaskawaRobot
from underautomation.yaskawa.high_speed_e_server.position_command_operation_coordinate import PositionCommandOperationCoordinate
import typing


robot = YaskawaRobot()
parameters = ConnectParameters("192.168.0.1")
parameters.ping_before_connect = True

robot.connect(parameters)


# Check connection
if robot.high_speed_e_server.connected:
    print("Connected!")

# Move in Cartesian
robot.high_speed_e_server.move_cartesian(
    x=1000, y=10, z=0,
    rx=0, ry=0, rz=0,
    speed=10,
    classification=PositionCommandClassification.Cartesian_MM_S,
    coordinate= PositionCommandOperationCoordinate.Base
)

# Get current joint position
joint_position = robot.high_speed_e_server.get_robot_joint_position()
print(joint_position.axes)

# Read and write register
reg = robot.high_speed_e_server.read_register(10, count=2)
robot.high_speed_e_server.write_register(10, [1234, 5678])

# Reset alarm
robot.high_speed_e_server.alarm_reset(AlarmResetType.Reset)