from enum import IntEnum

class SystemParameterTypes(IntEnum):
	'''Specifies the category of a system parameter to read from the controller. Types S1CG, AP, and SE require a group number when reading.'''
	S1CG = 0 # S1CxG. requires group number.
	S2C = 1 # S2C
	S3C = 2 # S3C
	S4C = 3 # S4C
	RS = 4 # RS
	AP = 5 # AxP. Requires a group number.
	SE = 6 # SxE. Requires a group number.
