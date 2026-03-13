from enum import IntEnum

class FlipNoFlipInformation(IntEnum):
	'''Specifies the flip/no-flip wrist configuration.'''
	Flip = 0 # Flip configuration - wrist is in flipped orientation.
	NoFlip = 1 # No-flip configuration - wrist is in standard orientation.
