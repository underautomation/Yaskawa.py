import typing
from __future__ import annotation
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotRealVariableData as robot_real_variable_data

class RobotRealVariableData(RobotData):
	'''Represents data returned from reading multiple real variables (R variables) from the robot controller. R variables are 32-bit single-precision floating point storage locations.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_real_variable_data()
		else:
			self._instance = _internal

	@property
	def value(self) -> typing.List[float]:
		'''Gets the array of single-precision floating point values read from the robot controller.'''
		return self._instance.Value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotRealVariableData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
