from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_yaskawa_client import IYaskawaClient
from underautomation.yaskawa.common.file_extension import FileExtension
from UnderAutomation.Yaskawa.Common import IFileReader as i_file_reader
from UnderAutomation.Yaskawa.Common import FileExtension as file_extension

class IFileReader(IYaskawaClient):
	'''Provides file read operations: download files and list directory contents.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_file_reader()
		else:
			self._instance = _internal

	def get_file(self, fileName: str) -> str:
		'''Downloads a file from the robot controller and returns its content as a string.

		:param fileName: Name of the file to download (e.g., "TEST.JBI").
		:returns: The text content of the file.
		'''
		return self._instance.GetFile(fileName)

	def get_file_list(self, fileExtension_or_pattern: str | FileExtension) -> typing.List[str]:
		'''Lists files matching a name pattern.
		Lists files matching the specified file extension.

		:param fileExtension_or_pattern: File name pattern (e.g., "*.JBI"). Or: The type of files to list.
		:returns: Array of matching file names.
		'''
		return self._instance.GetFileList(fileExtension_or_pattern)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IFileReader):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
