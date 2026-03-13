import typing
from underautomation.yaskawa.high_speed_e_server.robot_axis_raw_data_1 import RobotAxisRawData1
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotAxisConfigData as robot_axis_config_data

class RobotAxisConfigData(RobotAxisRawData1[str]):
	'''Represents raw axis data with string values for axis configuration information. Used to retrieve axis name/type information from the robot controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_axis_config_data()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotAxisConfigData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
