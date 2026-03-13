import typing
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotByteVariableData as robot_byte_variable_data

class RobotByteVariableData(RobotData):
	'''Represents data returned from reading multiple byte variables (B variables) from the robot controller. B variables are 8-bit unsigned integer storage locations (0-255).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_byte_variable_data()
		else:
			self._instance = _internal

	@property
	def value(self) -> typing.List[int]:
		'''Gets the array of byte variable values read from the robot controller.'''
		return self._instance.Value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotByteVariableData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
