from enum import IntEnum

class AlarmResetType(IntEnum):
	'''Specifies the type of alarm reset operation to perform.'''
	Reset = 1 # Reset the current alarm. Requires the alarm condition to be resolved.
	Cancel = 2 # Cancel the current error. Used for recoverable errors.
