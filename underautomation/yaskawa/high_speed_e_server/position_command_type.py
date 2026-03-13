from enum import IntEnum

class PositionCommandType(IntEnum):
	'''Specifies the type of position command (motion instruction) to execute. Determines the path type and whether position is absolute or incremental.'''
	LinkAbsolute = 1 # Link (joint interpolated) motion to an absolute position. All joints move simultaneously to reach the target, resulting in non-linear TCP path.
	StraightAbsolute = 2 # Straight (linear interpolated) motion to an absolute position. TCP moves in a straight line to the target position.
	StraightIncrement = 3 # Straight (linear interpolated) motion by an incremental offset. TCP moves in a straight line relative to current position.
