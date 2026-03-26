from enum import IntEnum

class RobotPositionDataType(IntEnum):
	'''Defines the coordinate system type for position data.'''
	PulseValue = 0 # Position in encoder pulse values (joint space).
	BaseCoordinateValue = 16 # Position in base coordinate system (world frame, value 16).
	RobotCoordinateValue = 17 # Position in robot coordinate system (robot base frame, value 17).
	ToolCoordinateValue = 18 # Position in tool coordinate system (value 18).
	UserCoordinateValue = 19 # Position in user-defined coordinate system (value 19).
