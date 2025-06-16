import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotSystemType as robot_system_type

class RobotSystemType(int):
	Robot = robot_system_type.Robot
	Station = robot_system_type.Station
	Application = robot_system_type.Application
