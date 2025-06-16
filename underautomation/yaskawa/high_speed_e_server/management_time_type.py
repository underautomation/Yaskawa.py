import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import ManagementTimeType as management_time_type

class ManagementTimeType(int):
	ControlPowerOnTime = management_time_type.ControlPowerOnTime
	ServoPowerOnTimeTotal = management_time_type.ServoPowerOnTimeTotal
	ServoPowerOnTimR1ToR8 = management_time_type.ServoPowerOnTimR1ToR8
	ServoPowerOnTimeS1ToS24 = management_time_type.ServoPowerOnTimeS1ToS24
	PlayBackTimeTotal = management_time_type.PlayBackTimeTotal
	PlayBackTimeR1ToR8 = management_time_type.PlayBackTimeR1ToR8
	PlayBackTimeS1ToS24 = management_time_type.PlayBackTimeS1ToS24
	MotionTimeTotal = management_time_type.MotionTimeTotal
	MotionTimeR1ToR8 = management_time_type.MotionTimeR1ToR8
	MotionTimeS1ToS24 = management_time_type.MotionTimeS1ToS24
	OperationTimeApplication1To8 = management_time_type.OperationTimeApplication1To8
