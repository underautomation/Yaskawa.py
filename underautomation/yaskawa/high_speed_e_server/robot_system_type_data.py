import typing
from underautomation.yaskawa.high_speed_e_server.robot_system_type import RobotSystemType
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotSystemTypeData as robot_system_type_data
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotSystemType as robot_system_type

class RobotSystemTypeData:
	'''Represents a system type and index combination for querying specific robot system components. Used to specify which robot, station, or application to query in multi-robot configurations.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_system_type_data()
		else:
			self._instance = _internal

	@property
	def index(self) -> int:
		'''Gets the index within the system type (1-based).'''
		return self._instance.Index

	@property
	def type(self) -> RobotSystemType:
		'''Gets the system type (Robot, Station, or Application).'''
		return RobotSystemType(int(self._instance.Type))

	@property
	def byte(self) -> int:
		'''Gets the combined byte value sent to the controller (Type + Index).'''
		return self._instance.Byte

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotSystemTypeData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default system type data for querying the primary robot (Robot 1).
RobotSystemTypeData.Default = RobotSystemTypeData(robot_system_type_data.Default)
