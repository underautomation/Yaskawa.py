import typing
from __future__ import annotation
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from underautomation.yaskawa.high_speed_e_server.robot_data_header import RobotDataHeader
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotFileContentData as robot_file_content_data

class RobotFileContentData(RobotData):
	'''Contains the content of a file downloaded from the robot controller. Provides methods for parsing structured file content such as job files and parameter files.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_file_content_data()
		else:
			self._instance = _internal

	def get_param(self, section: str, parameterLine: int, parameterColumn: int) -> int:
		return self._instance.GetParam(section, parameterLine, parameterColumn)

	@property
	def headers(self) -> typing.Any:
		'''Gets the list of response headers from multi-block transfers. Large files are transferred in multiple UDP packets.'''
		return self._instance.Headers

	@property
	def content(self) -> str:
		'''Gets the text content of the downloaded file.'''
		return self._instance.Content

	@property
	def content_raw(self) -> typing.List[int]:
		'''Gets the text content of the downloaded file.'''
		return self._instance.ContentRaw

	@property
	def file_name(self) -> str:
		'''Gets the name of the downloaded file.'''
		return self._instance.FileName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotFileContentData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
