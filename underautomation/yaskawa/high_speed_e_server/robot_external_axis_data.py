import typing
from underautomation.yaskawa.high_speed_e_server.robot_data_header import RobotDataHeader
from underautomation.yaskawa.high_speed_e_server.robot_axis_raw_data_1 import RobotAxisRawData1
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotExternalAxisData as robot_external_axis_data

class RobotExternalAxisData(RobotAxisRawData1[int]):
	'''Represents external axis position data for positioners, travel units, or additional servo axes. External axes are coordinated with the robot motion for applications like welding positioners.'''
	def __init__(self, header: RobotDataHeader, _internal = 0):
		'''Creates a new instance of RobotExternalAxisData with the specified header information.

		:param header: Response header containing metadata about the communication.
		'''
		if(_internal == 0):
			self._instance = robot_external_axis_data(header)
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotExternalAxisData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
