from enum import IntEnum

class HostControlCoordinateSystem(IntEnum):
	'''Specifies the coordinate system for position commands.'''
	Base = 0 # Base coordinate system (robot base frame).
	Robot = 1 # Robot coordinate system.
	User1 = 2 # User coordinate system 1.
	User2 = 3 # User coordinate system 2.
	User3 = 4 # User coordinate system 3.
	User4 = 5 # User coordinate system 4.
	User5 = 6 # User coordinate system 5.
	User6 = 7 # User coordinate system 6.
	User7 = 8 # User coordinate system 7.
	User8 = 9 # User coordinate system 8.
	Tool = 16 # Tool coordinate system.
