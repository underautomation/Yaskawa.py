from enum import IntEnum

class ArmFlipInformation(IntEnum):
	'''Specifies the arm configuration (upper/lower) based on L and U axis positions.'''
	Upper = 0 # Upper arm configuration - elbow is above the line between shoulder and wrist.
	Lower = 1 # Lower arm configuration - elbow is below the line between shoulder and wrist.
