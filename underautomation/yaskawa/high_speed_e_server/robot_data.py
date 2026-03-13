import typing
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotData as robot_data

class RobotData:
	'''Base class for all robot data response objects returned by High Speed Ethernet Server commands. Contains common header information about the communication response.'''
	def __init__(self, _internal = 0):
		'''Creates a blank instance of RobotData, for use as input to robot commands (e.g. kinematics conversions).'''
		if(_internal == 0):
			self._instance = robot_data()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
