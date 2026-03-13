from enum import IntEnum

class HostControlResponseCode(IntEnum):
	'''Specifies the interpreter error/response codes.'''
	Success = 0 # Normal completion.
	ManipulatorMoving = 2010 # Manipulator is moving.
	HoldByCommand = 2020 # In hold state (command).
	HoldByExternal = 2030 # In hold state (external).
	HoldByPendant = 2040 # In hold state (pendant).
	HoldByOperationPanel = 2050 # In hold state (operation panel).
	AlarmOrError = 2060 # Alarm or error occurring.
	ServoOff = 2070 # Servo OFF.
	IncorrectMode = 2080 # Incorrect mode.
	NoCommandRemote = 2100 # No command remote setting.
