from enum import IntEnum

class RegardedReversePositionSpecified(IntEnum):
	'''Specifies how to handle position in reverse direction scenarios.'''
	Previous = 0 # Use the previous position as reference.
	Form = 1 # Use the specified form/posture as reference.
