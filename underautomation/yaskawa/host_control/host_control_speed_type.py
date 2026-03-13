from enum import IntEnum

class HostControlSpeedType(IntEnum):
	'''Specifies the speed type for motion commands.'''
	Percentage = 0 # Speed is specified as a percentage of maximum speed (V).
	MillimetersPerSecond = 1 # Speed is specified in mm/s (VE).
