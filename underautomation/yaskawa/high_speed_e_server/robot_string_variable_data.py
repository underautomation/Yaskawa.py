import typing
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotStringVariableData as robot_string_variable_data

class RobotStringVariableData(RobotData):
	'''Represents data returned from reading multiple string variables (S variables) from the robot controller. S variables can be either 16-byte or 32-byte character strings depending on the command used.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_string_variable_data()
		else:
			self._instance = _internal

	@property
	def value(self) -> typing.List[str]:
		'''Gets the array of string values read from the robot controller. Strings are null-terminated and trimmed of trailing null characters.'''
		return self._instance.Value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotStringVariableData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
