import typing
from __future__ import annotation
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotRegisterData as robot_register_data

class RobotRegisterData(RobotData):
	'''Represents data returned from reading multiple register values from the robot controller. Registers are 16-bit signed integer storage locations used for general-purpose data.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_register_data()
		else:
			self._instance = _internal

	@property
	def value(self) -> typing.List[int]:
		'''Gets the array of register values read from the robot controller. Each value is a 16-bit signed integer (-32768 to 32767).'''
		return self._instance.Value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotRegisterData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
