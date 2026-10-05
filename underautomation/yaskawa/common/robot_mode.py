from enum import IntEnum

class RobotMode(IntEnum):
	'''Specifies the robot operation mode.'''
	Teach = 1 # Teach mode : robot can be manually positioned and jobs can be edited.
	Play = 2 # Play mode : robot can execute programmed jobs.
