from __future__ import annotations
import typing
from underautomation.yaskawa.high_speed_e_server.robot_position_data_type import RobotPositionDataType
from underautomation.yaskawa.high_speed_e_server.robot_posture import RobotPosture
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotKinematicsPositionData as robot_kinematics_position_data
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotPositionDataType as robot_position_data_type

class RobotKinematicsPositionData(RobotData):
	'''Base class for kinematic position data exchanged with the robot controller. Contains coordinate type, posture flags, tool/user numbers, and the 8 raw axis values.'''
	def __init__(self, _internal = 0):
		'''Creates a blank instance for use as input to kinematics conversion methods.'''
		if(_internal == 0):
			self._instance = robot_kinematics_position_data()
		else:
			self._instance = _internal

	@property
	def data_type(self) -> RobotPositionDataType:
		'''Gets or sets the coordinate type of this position.'''
		return RobotPositionDataType(int(self._instance.DataType))

	@data_type.setter
	def data_type(self, value: RobotPositionDataType):
		self._instance.DataType = robot_position_data_type(int(value))

	@property
	def form(self) -> RobotPosture:
		'''Gets or sets the posture/form flags for this position.'''
		return RobotPosture(None, None, None, None, None, None, None, None, None, None, None, None, None, self._instance.Form)

	@form.setter
	def form(self, value: RobotPosture):
		self._instance.Form = value._instance if value else None

	@property
	def tool_number(self) -> int:
		'''Gets or sets the tool number used for this position.'''
		return self._instance.ToolNumber

	@tool_number.setter
	def tool_number(self, value: int):
		self._instance.ToolNumber = value

	@property
	def user_coordinate_number(self) -> int:
		'''Gets or sets the user coordinate number used for this position.'''
		return self._instance.UserCoordinateNumber

	@user_coordinate_number.setter
	def user_coordinate_number(self, value: int):
		self._instance.UserCoordinateNumber = value

	@property
	def axes(self) -> typing.List[int]:
		'''Gets or sets the 8 raw axis values. For joint positions: values in 0.0001° units (divide by 10 000 for degrees). For Cartesian positions: XYZ axes (0–2) in µm; orientation axes (3–5) in 0.0001°.'''
		return self._instance.Axes

	@axes.setter
	def axes(self, value: typing.List[int]):
		self._instance.Axes = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotKinematicsPositionData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
