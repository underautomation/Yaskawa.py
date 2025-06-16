import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import OrientationFlipInformation as orientation_flip_information

class OrientationFlipInformation(int):
	Front = orientation_flip_information.Front
	Back = orientation_flip_information.Back
