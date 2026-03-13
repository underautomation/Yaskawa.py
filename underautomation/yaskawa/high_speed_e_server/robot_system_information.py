import typing
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotSystemInformation as robot_system_information

class RobotSystemInformation(RobotData):
	'''Contains system information about the robot controller including software version and configuration. Retrieved using the system information acquiring command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_system_information()
		else:
			self._instance = _internal

	@property
	def software_version(self) -> str:
		'''Gets the controller software version string. Format typically includes model and version number. Maximum 24 characters.'''
		return self._instance.SoftwareVersion

	@property
	def name(self) -> str:
		'''Gets the system/robot name or model identifier. Maximum 16 characters.'''
		return self._instance.Name

	@property
	def parameter(self) -> str:
		'''Gets parameter file or configuration information. Maximum 8 characters.'''
		return self._instance.Parameter

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotSystemInformation):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
