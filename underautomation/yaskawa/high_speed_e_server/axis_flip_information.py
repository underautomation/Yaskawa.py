from enum import IntEnum

class AxisFlipInformation(IntEnum):
	'''Specifies whether an axis angle is less than or greater than/equal to 180 degrees. Used for determining robot configuration in multi-solution situations.'''
	LT180 = 0 # Axis angle is less than 180 degrees.
	UT180 = 1 # Axis angle is greater than or equal to 180 degrees.
