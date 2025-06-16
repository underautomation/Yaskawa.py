import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import PositionCommandOperationCoordinate as position_command_operation_coordinate

class PositionCommandOperationCoordinate(int):
	Base = position_command_operation_coordinate.Base
	Robot = position_command_operation_coordinate.Robot
	User = position_command_operation_coordinate.User
	Tool = position_command_operation_coordinate.Tool
