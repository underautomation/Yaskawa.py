import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import AxisFlipInformation as axis_flip_information

class AxisFlipInformation(int):
	LT180 = axis_flip_information.LT180
	UT180 = axis_flip_information.UT180
