import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import OnOffCommandType as on_off_command_type

class OnOffCommandType(int):
	Hold = on_off_command_type.Hold
	Servo = on_off_command_type.Servo
	HLock = on_off_command_type.HLock
