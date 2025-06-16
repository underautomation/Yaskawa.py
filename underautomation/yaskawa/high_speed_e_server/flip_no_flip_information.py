import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import FlipNoFlipInformation as flip_no_flip_information

class FlipNoFlipInformation(int):
	Flip = flip_no_flip_information.Flip
	NoFlip = flip_no_flip_information.NoFlip
