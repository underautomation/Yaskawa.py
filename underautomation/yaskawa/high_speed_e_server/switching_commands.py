from enum import IntEnum

class SwitchingCommands(IntEnum):
	'''Specifies the execution mode switching command to send to the robot controller. These modes control how the robot executes programmed jobs.'''
	Cycle = 1 # Cycle mode - robot executes one complete cycle of the program then stops. Useful for testing or single-part operations.
	Step = 2 # Step mode - robot executes one instruction at a time, stopping after each. Useful for debugging and detailed program verification.
	Continue_ = 3 # Continuous mode - robot executes the program continuously until stopped. Normal production operation mode.
