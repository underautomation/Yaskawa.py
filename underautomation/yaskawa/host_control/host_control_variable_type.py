from enum import IntEnum

class HostControlVariableType(IntEnum):
	'''Specifies the type of variable to read or write.'''
	Byte = 0 # Byte variable (B).
	Integer = 1 # Integer variable (I).
	DoubleInteger = 2 # Double integer variable (D).
	Real = 3 # Real (floating point) variable (R).
	Position = 4 # Robot axis position variable (P).
	BasePosition = 5 # Base axis position variable (BP).
	ExternalPosition = 6 # Station axis position variable (EX), pulse type only.
	String = 7 # String variable (S).
