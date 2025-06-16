import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import RegardedReversePositionSpecified as regarded_reverse_position_specified

class RegardedReversePositionSpecified(int):
	Previous = regarded_reverse_position_specified.Previous
	Form = regarded_reverse_position_specified.Form
