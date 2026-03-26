import typing
from __future__ import annotation
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotPluralData as robot_plural_data_1

T = typing.TypeVar('T')
class RobotPluralData1(RobotData, typing.Generic[T]):
	'''Represents a collection of data values returned from plural (batch) read operations. Used for reading multiple variables, registers, or I/O points in a single request.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_plural_data_1()
		else:
			self._instance = _internal

	@property
	def value(self) -> typing.List[T]:
		'''Gets the array of values read from the robot controller. The array length corresponds to the number of values successfully read.'''
		return list(self._instance.Value)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotPluralData1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
