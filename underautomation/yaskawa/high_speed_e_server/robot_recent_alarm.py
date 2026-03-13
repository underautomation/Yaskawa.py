from enum import IntEnum

class RobotRecentAlarm(IntEnum):
	'''Specifies which recent alarm to retrieve from the robot controller. The controller maintains a history of the most recent alarms.'''
	Latest = 1 # The most recent (current) alarm.
	SecondLatest = 2 # The second most recent alarm.
	ThirdLatest = 3 # The third most recent alarm.
	FourthLatest = 4 # The fourth most recent alarm.
