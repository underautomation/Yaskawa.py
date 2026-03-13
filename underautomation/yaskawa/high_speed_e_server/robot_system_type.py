from enum import IntEnum

class RobotSystemType(IntEnum):
	'''Defines the types of system components that can be queried for information.'''
	Robot = 10 # Robot manipulator system (R1-R8). Valid index: 1-8.
	Station = 20 # Station/positioner system (S1-S24). Valid index: 1-24.
	Application = 100 # Application system (APP1-APP8). Valid index: 1-8.
