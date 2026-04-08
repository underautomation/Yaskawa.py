from __future__ import annotations
import typing
from underautomation.yaskawa.high_speed_e_server.robot_base_position_data import RobotBasePositionData
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotBasePositionVariableData as robot_base_position_variable_data

class RobotBasePositionVariableData(RobotData):
	'''Represents data returned from reading multiple base position variables (BP variables) from the robot controller. BP variables store base position information used for coordinated motion with external axes or travel units.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_base_position_variable_data()
		else:
			self._instance = _internal

	@property
	def value(self) -> typing.List[RobotBasePositionData]:
		'''Gets the array of base position data read from the robot controller.'''
		return [RobotBasePositionData(None, x) for x in self._instance.Value]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotBasePositionVariableData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
