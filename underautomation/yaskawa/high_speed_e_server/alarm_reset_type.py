import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import AlarmResetType as alarm_reset_type

class AlarmResetType(int):
	Reset = alarm_reset_type.Reset
	Cancel = alarm_reset_type.Cancel
