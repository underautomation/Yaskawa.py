from __future__ import annotations
import typing
from underautomation.yaskawa.high_speed_e_server.robot_base_position_type import RobotBasePositionType
from underautomation.yaskawa.high_speed_e_server.robot_data_header import RobotDataHeader
from underautomation.yaskawa.high_speed_e_server.robot_axis_raw_data_1 import RobotAxisRawData1
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotBasePositionData as robot_base_position_data
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotBasePositionType as robot_base_position_type

class RobotBasePositionData(RobotAxisRawData1[int]):
	'''Represents base position data for coordinated motion with travel units or external bases. Base positions define the location of the robot's base in world coordinates or pulse values.'''
	def __init__(self, header: RobotDataHeader, _internal = 0):
		'''Creates a new instance of RobotBasePositionData with the specified header information.

		:param header: Response header containing metadata about the communication.
		'''
		if(_internal == 0):
			self._instance = robot_base_position_data(header)
		else:
			self._instance = _internal

	@property
	def data_type(self) -> RobotBasePositionType:
		'''Gets the data type indicating whether values are pulse or coordinate values.'''
		return RobotBasePositionType(int(self._instance.DataType))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotBasePositionData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
