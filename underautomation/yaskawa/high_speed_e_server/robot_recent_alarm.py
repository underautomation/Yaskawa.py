import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotRecentAlarm as robot_recent_alarm

class RobotRecentAlarm(int):
	Latest = robot_recent_alarm.Latest
	SecondLatest = robot_recent_alarm.SecondLatest
	ThirdLatest = robot_recent_alarm.ThirdLatest
	FourthLatest = robot_recent_alarm.FourthLatest
