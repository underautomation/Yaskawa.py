from enum import IntEnum

class RobotBasePositionType(IntEnum):
	'''Defines the type of base position data representation.'''
	PulseValue = 0 # Position is represented as encoder pulse values.
	BaseCoordinateValue = 16 # Position is represented in base coordinate system values.
