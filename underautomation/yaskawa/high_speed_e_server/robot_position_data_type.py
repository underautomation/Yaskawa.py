import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotPositionDataType as robot_position_data_type

class RobotPositionDataType(int):
	PulseValue = robot_position_data_type.PulseValue
	BaseCoordinateValue = robot_position_data_type.BaseCoordinateValue
	RobotCoordinateValue = robot_position_data_type.RobotCoordinateValue
	UserCoordinateValue = robot_position_data_type.UserCoordinateValue
	ToolCoordinateValue = robot_position_data_type.ToolCoordinateValue
