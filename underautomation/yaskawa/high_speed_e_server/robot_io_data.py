import typing
from __future__ import annotation
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotIOData as robot_io_data

class RobotIOData(RobotData):
	'''Represents data returned from reading multiple I/O (Input/Output) points from the robot controller. I/O addresses are organized in groups based on their function and accessibility.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_io_data()
		else:
			self._instance = _internal

	@property
	def value(self) -> typing.List[int]:
		'''Gets the array of I/O byte values read from the robot controller. Each byte represents 8 consecutive I/O points where each bit corresponds to one I/O state.'''
		return self._instance.Value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotIOData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
