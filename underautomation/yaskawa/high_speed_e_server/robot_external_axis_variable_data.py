import typing
from __future__ import annotation
from underautomation.yaskawa.high_speed_e_server.robot_external_axis_data import RobotExternalAxisData
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotExternalAxisVariableData as robot_external_axis_variable_data

class RobotExternalAxisVariableData(RobotData):
	'''Represents data returned from reading multiple external axis variables (EX variables) from the robot controller. EX variables store position data for external axes such as positioners, travel units, or additional servo axes.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_external_axis_variable_data()
		else:
			self._instance = _internal

	@property
	def value(self) -> typing.List[RobotExternalAxisData]:
		'''Gets the array of external axis data read from the robot controller.'''
		return [RobotExternalAxisData(None, x) for x in self._instance.Value]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotExternalAxisVariableData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
