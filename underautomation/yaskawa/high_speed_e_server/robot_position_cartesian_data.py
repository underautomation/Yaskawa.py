import typing
from __future__ import annotation
from underautomation.yaskawa.high_speed_e_server.robot_posture import RobotPosture
from underautomation.yaskawa.high_speed_e_server.robot_position_data_type import RobotPositionDataType
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotPositionCartesianData as robot_position_cartesian_data
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotPositionDataType as robot_position_data_type

class RobotPositionCartesianData(RobotData):
	'''Represents Cartesian position data with coordinates in millimeters and degrees. This class provides human-readable position data converted from the raw protocol values.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_position_cartesian_data()
		else:
			self._instance = _internal

	@property
	def form(self) -> RobotPosture:
		'''Gets the robot posture (form) data defining the kinematic configuration.'''
		return RobotPosture(None, None, None, None, None, None, None, None, None, None, None, None, None, self._instance.Form)

	@property
	def data_type(self) -> RobotPositionDataType:
		'''Gets the position data type indicating the coordinate system used.'''
		return RobotPositionDataType(int(self._instance.DataType))

	@property
	def tool_number(self) -> int:
		'''Gets the tool number (TCP) used for this position.'''
		return self._instance.ToolNumber

	@property
	def user_coordinate_number(self) -> int:
		'''Gets the user coordinate system number used for this position.'''
		return self._instance.UserCoordinateNumber

	@property
	def x(self) -> float:
		'''Gets the X coordinate in millimeters.'''
		return self._instance.X

	@property
	def y(self) -> float:
		'''Gets the Y coordinate in millimeters.'''
		return self._instance.Y

	@property
	def z(self) -> float:
		'''Gets the Z coordinate in millimeters.'''
		return self._instance.Z

	@property
	def rx(self) -> float:
		'''Gets the rotation around X axis (Rx) in degrees.'''
		return self._instance.Rx

	@property
	def ry(self) -> float:
		'''Gets the rotation around Y axis (Ry) in degrees.'''
		return self._instance.Ry

	@property
	def rz(self) -> float:
		'''Gets the rotation around Z axis (Rz) in degrees.'''
		return self._instance.Rz

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotPositionCartesianData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
