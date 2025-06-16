import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotBasePositionType as robot_base_position_type

class RobotBasePositionType(int):
	PulseValue = robot_base_position_type.PulseValue
	BaseCoordinateValue = robot_base_position_type.BaseCoordinateValue
