from enum import IntEnum

class PositionCommandOperationCoordinate(IntEnum):
	'''Specifies the coordinate system for position command interpretation. Determines how X, Y, Z, Rx, Ry, Rz values are interpreted.'''
	Base = 16 # Base coordinate system (world frame at robot base). Fixed reference frame typically aligned with robot mounting.
	Robot = 17 # Robot coordinate system. Reference frame at the robot's origin point.
	User = 18 # User-defined coordinate system. Custom reference frame defined for specific workpiece or fixture.
	Tool = 19 # Tool coordinate system. Reference frame at the tool center point (TCP).
