import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import ControlGroup as control_group

class ControlGroup(int):
	RobotPulseValue = control_group.RobotPulseValue
	BasePulseValue = control_group.BasePulseValue
	StationPulseValue = control_group.StationPulseValue
	RobotCartesian = control_group.RobotCartesian
	BaseCartesian = control_group.BaseCartesian
