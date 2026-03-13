import typing
from underautomation.yaskawa.high_speed_e_server.robot_data_header import RobotDataHeader
from underautomation.yaskawa.high_speed_e_server.robot_posture import RobotPosture
from underautomation.yaskawa.high_speed_e_server.robot_position_data_type import RobotPositionDataType
from underautomation.yaskawa.high_speed_e_server.robot_axis_raw_data_1 import RobotAxisRawData1
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotPositionData as robot_position_data_1
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotPositionDataType as robot_position_data_type

T = typing.TypeVar('T')
class RobotPositionData1(RobotAxisRawData1[T], typing.Generic[T]):
	'''Represents generic robot position data with axis values of the specified type. This class provides a flexible structure for storing position information that can be represented in different data formats (pulse values, Cartesian coordinates, etc.).'''
	def __init__(self, header: RobotDataHeader, _internal = 0):
		'''Creates a new instance of RobotPositionData with the specified header information.

		:param header: Response header containing metadata about the communication.
		'''
		if(_internal == 0):
			self._instance = robot_position_data_1(header)
		else:
			self._instance = _internal

	@property
	def form(self) -> RobotPosture:
		'''Gets or sets the robot posture (form) data defining the robot's kinematic configuration. This includes flip/no-flip state, arm configuration (upper/lower), and axis angle ranges.'''
		return RobotPosture(None, None, None, None, None, None, None, None, None, None, None, None, None, self._instance.Form)

	@form.setter
	def form(self, value: RobotPosture):
		self._instance.Form = value._instance if value else None

	@property
	def data_type(self) -> RobotPositionDataType:
		'''Gets or sets the position data type indicating the coordinate system used. Determines how axis values should be interpreted (pulse, base, robot, user, or tool coordinates).'''
		return RobotPositionDataType(int(self._instance.DataType))

	@data_type.setter
	def data_type(self, value: RobotPositionDataType):
		self._instance.DataType = robot_position_data_type(int(value))

	@property
	def tool_number(self) -> int:
		'''Gets or sets the tool number (TCP - Tool Center Point) used for this position. Tool numbers typically range from 0-63, where 0 is often the robot flange center.'''
		return self._instance.ToolNumber

	@tool_number.setter
	def tool_number(self, value: int):
		self._instance.ToolNumber = value

	@property
	def user_coordinate_number(self) -> int:
		'''Gets or sets the user coordinate system number used for this position. User coordinates define custom reference frames for specific workpiece locations.'''
		return self._instance.UserCoordinateNumber

	@user_coordinate_number.setter
	def user_coordinate_number(self, value: int):
		self._instance.UserCoordinateNumber = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotPositionData1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
