from enum import IntEnum

class ManagementTimeType(IntEnum):
	'''Specifies the type of management time data to retrieve. Different metrics track various aspects of robot operation.'''
	ControlPowerOnTime = 1 # Total time the controller power has been on.
	ServoPowerOnTimeTotal = 10 # Total servo power on time across all robots.
	ServoPowerOnTimR1ToR8 = 10 # Servo power on time for robots R1 through R8. Pass the robot number (1 to 8) as index of GetManagementTime.
	ServoPowerOnTimeS1ToS24 = 20 # Servo power on time for stations S1 through S24. Pass the station number (1 to 24) as index of GetManagementTime.
	PlayBackTimeTotal = 110 # Total playback time across all robots.
	PlayBackTimeR1ToR8 = 110 # Playback time for robots R1 through R8. Pass the robot number (1 to 8) as index of GetManagementTime.
	PlayBackTimeS1ToS24 = 120 # Playback time for stations S1 through S24. Pass the station number (1 to 24) as index of GetManagementTime.
	MotionTimeTotal = 210 # Total motion time across all robots.
	MotionTimeR1ToR8 = 210 # Motion time for robots R1 through R8. Pass the robot number (1 to 8) as index of GetManagementTime.
	MotionTimeS1ToS24 = 220 # Motion time for stations S1 through S24. Pass the station number (1 to 24) as index of GetManagementTime.
	OperationTimeApplication1To8 = 300 # Operation time for applications 1 through 8. Add application number (0-7) to get specific application.
