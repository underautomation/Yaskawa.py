import typing
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from underautomation.yaskawa.high_speed_e_server.robot_data_header import RobotDataHeader
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotFileListData as robot_file_list_data

class RobotFileListData(RobotData):
	'''Contains the result of a file listing operation on the robot controller. Returns an array of file names matching the specified pattern.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_file_list_data()
		else:
			self._instance = _internal

	@property
	def headers(self) -> typing.Any:
		'''Gets the list of response headers from multi-block transfers. File listings may span multiple UDP packets for large directories.'''
		return self._instance.Headers

	@property
	def files(self) -> typing.List[str]:
		'''Gets the array of file names returned by the listing operation. File names include extensions (e.g., "MYJOB.JBI", "SYSTEM.SYS").'''
		return self._instance.Files

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotFileListData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
