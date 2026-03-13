from enum import IntEnum

class IOType(IntEnum):
	'''Yaskawa Motoman I/O signal type categories.'''
	GeneralInput = 0 # Robot user input signals (#00010–)
	GeneralOutput = 1 # Robot user output signals (#10010–)
	ExternalInput = 2 # External input signals (#20010–)
	NetworkInput = 3 # Network input signals (#27010–)
	ExternalOutput = 4 # External output signals (#30010–)
	NetworkOutput = 5 # Network output signals (#37010–)
	SpecificInput = 6 # Robot system input signals (#40010–)
	SpecificOutput = 7 # Robot system output signals (#50010–)
	InterfacePanelInput = 8 # Interface panel input signals (#60010–)
	AuxiliaryRelay = 9 # Auxiliary relay signals (#70010–)
	RobotControlStatus = 10 # Robot control status signals (#80010–)
	PseudoInput = 11 # Pseudo input signals (#82010–)
