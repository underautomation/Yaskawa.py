from enum import IntEnum

class PositionCommandClassification(IntEnum):
	'''Specifies the speed classification (units) for motion commands. Determines how the speed value is interpreted by the controller.'''
	LinkPercent = 0 # Speed as percentage of maximum link (joint) speed. Valid range: 0.01 to 100.00 percent.
	Cartesian_MM_S = 1 # Speed in millimeters per second for linear motion. Valid range depends on robot model.
	Cartesian_DEG_S = 2 # Speed in degrees per second for rotational motion. Valid range depends on robot model.
