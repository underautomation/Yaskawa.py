from enum import IntEnum

class HostControlVariableType(IntEnum):
	'''Specifies the type of variable to read or write.'''
	Byte = 0 # Byte variable (B).
	Integer = 1 # Integer variable (I).
	DoubleInteger = 2 # Double integer variable (D).
	Real = 3 # Real (floating point) variable (R).
	String = 4 # String variable (S).
	RobotAxisPosition = 5 # Robot axis position variable (not supported via SAVEV).
	Position = 6 # Position variable (P).
	BasePosition = 7 # Base position variable (BP).
	ExternalPosition = 8 # External axis position variable (EX).
