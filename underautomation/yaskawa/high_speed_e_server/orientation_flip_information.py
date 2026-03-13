from enum import IntEnum

class OrientationFlipInformation(IntEnum):
	'''Specifies the orientation (front/back) configuration of the robot arm. Determined by the position of the B-axis rotation center relative to the S-axis.'''
	Front = 0 # Front configuration - B-axis rotation center is in front of S-axis rotation center when viewed from the right-hand side of the robot.
	Back = 1 # Back configuration - B-axis rotation center is behind S-axis rotation center when viewed from the right-hand side of the robot.
