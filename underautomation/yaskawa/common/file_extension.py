from enum import IntEnum

class FileExtension(IntEnum):
	'''Represents the file types available on a Yaskawa robot controller.'''
	JOB = 0 # Job files (.JBI)
	DAT = 1 # Data files (.DAT)
	CND = 2 # Condition files (.CND)
	SYS = 3 # System files (.SYS)
	PRM = 4 # Parameter files (.PRM)
	LST = 5 # List files (.LST)
	CSV = 6 # CSV files (.CSV)
	LOG = 7 # Log files (.LOG)
	TXT = 8 # Text files (.TXT)
