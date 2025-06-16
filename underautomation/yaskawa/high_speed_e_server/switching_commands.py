import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import SwitchingCommands as switching_commands

class SwitchingCommands(int):
	Cycle = switching_commands.Cycle
	Step = switching_commands.Step
	Continue = switching_commands.Continue
