import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import PositionCommandType as position_command_type

class PositionCommandType(int):
	LinkAbsolute = position_command_type.LinkAbsolute
	StraightAbsolute = position_command_type.StraightAbsolute
	StraightIncrement = position_command_type.StraightIncrement
