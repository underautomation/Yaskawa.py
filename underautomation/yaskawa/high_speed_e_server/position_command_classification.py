import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import PositionCommandClassification as position_command_classification

class PositionCommandClassification(int):
	LinkPercent = position_command_classification.LinkPercent
	Cartesian_MM_S = position_command_classification.Cartesian_MM_S
	Cartesian_DEG_S = position_command_classification.Cartesian_DEG_S
