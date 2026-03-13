from enum import IntEnum

class ControlGroup(IntEnum):
	'''Defines control group types for robot systems. Control groups organize different motion units within the robot system.'''
	RobotPulseValue = 0 # Robot axes in pulse (encoder) values. Valid index: 1-8.
	BasePulseValue = 10 # Base axes in pulse values. Valid index: 1-8.
	StationPulseValue = 21 # Station axes in pulse values. Valid index: 1-44.
	RobotCartesian = 100 # Robot axes in Cartesian coordinates. Valid index: 1-8.
	BaseCartesian = 110 # Base axes in Cartesian coordinates. Valid index: 1-8.
