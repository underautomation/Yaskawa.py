import typing
from underautomation.yaskawa.high_speed_e_server.robot_posture import RobotPosture
from underautomation.yaskawa.high_speed_e_server.robot_position_data_type import RobotPositionDataType
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotPositionCartesianData as robot_position_cartesian_data

class RobotPositionCartesianData(RobotData):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_position_cartesian_data()
		else:
			self._instance = _internal
	@property
	def form(self) -> RobotPosture:
		return RobotPosture(None, None, self._instance.Form)
	@form.setter
	def form(self, value: RobotPosture):
		self._instance.Form = value
	@property
	def data_type(self) -> RobotPositionDataType:
		return RobotPositionDataType(self._instance.DataType)
	@data_type.setter
	def data_type(self, value: RobotPositionDataType):
		self._instance.DataType = value
	@property
	def tool_number(self) -> int:
		return self._instance.ToolNumber
	@tool_number.setter
	def tool_number(self, value: int):
		self._instance.ToolNumber = value
	@property
	def user_coordinate_number(self) -> int:
		return self._instance.UserCoordinateNumber
	@user_coordinate_number.setter
	def user_coordinate_number(self, value: int):
		self._instance.UserCoordinateNumber = value
	@property
	def x(self) -> float:
		return self._instance.X
	@x.setter
	def x(self, value: float):
		self._instance.X = value
	@property
	def y(self) -> float:
		return self._instance.Y
	@y.setter
	def y(self, value: float):
		self._instance.Y = value
	@property
	def z(self) -> float:
		return self._instance.Z
	@z.setter
	def z(self, value: float):
		self._instance.Z = value
	@property
	def rx(self) -> float:
		return self._instance.Rx
	@rx.setter
	def rx(self, value: float):
		self._instance.Rx = value
	@property
	def ry(self) -> float:
		return self._instance.Ry
	@ry.setter
	def ry(self, value: float):
		self._instance.Ry = value
	@property
	def rz(self) -> float:
		return self._instance.Rz
	@rz.setter
	def rz(self, value: float):
		self._instance.Rz = value
