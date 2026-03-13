from enum import IntEnum

class HostControlCycleType(IntEnum):
	'''Specifies the execution cycle type.'''
	Step = 1 # Step mode - execute one instruction at a time.
	OneCycle = 2 # One cycle mode - execute one complete cycle then stop.
	Automatic = 3 # Automatic mode - continuous operation.
