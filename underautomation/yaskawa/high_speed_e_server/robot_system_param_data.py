import typing
from __future__ import annotation
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotSystemParamData as robot_system_param_data

class RobotSystemParamData(RobotData):
	'''Contains a system parameter value read from the robot controller. Retrieved using YERC command 0x039C.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_system_param_data()
		else:
			self._instance = _internal

	@property
	def value(self) -> int:
		'''Gets the raw system parameter value returned by the controller.'''
		return self._instance.Value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotSystemParamData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
