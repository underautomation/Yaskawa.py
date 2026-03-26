import typing
from __future__ import annotation
from underautomation.yaskawa.high_speed_e_server.robot_position_int_data import RobotPositionIntData
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotPositionVariableData as robot_position_variable_data

class RobotPositionVariableData(RobotData):
	'''Represents data returned from reading multiple position variables (P variables) from the robot controller. P variables store complete robot position data including coordinates, posture, tool and user coordinate references.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_position_variable_data()
		else:
			self._instance = _internal

	@property
	def value(self) -> typing.List[RobotPositionIntData]:
		'''Gets the array of position variable data read from the robot controller. Each element contains full position information including axis values, posture, and coordinate references.'''
		return [RobotPositionIntData(None, x) for x in self._instance.Value]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotPositionVariableData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
