import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import ArmFlipInformation as arm_flip_information

class ArmFlipInformation(int):
	Upper = arm_flip_information.Upper
	Lower = arm_flip_information.Lower
