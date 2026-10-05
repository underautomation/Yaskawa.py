from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_yaskawa_client import IYaskawaClient
from UnderAutomation.Yaskawa.Common import IFileWriter as i_file_writer

class IFileWriter(IYaskawaClient):
	'''Provides file write and delete operations on the robot controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_file_writer()
		else:
			self._instance = _internal

	def load_file(self, fileName: str, content: str) -> None:
		'''Uploads a file to the robot controller.

		:param fileName: Name of the file to create or overwrite (e.g., "TEST.JBI").
		:param content: The text content of the file.
		'''
		self._instance.LoadFile(fileName, content)

	def delete_file(self, fileName: str) -> None:
		'''Deletes a file from the robot controller.

		:param fileName: Name of the file to delete (e.g., "TEST.JBI").
		'''
		self._instance.DeleteFile(fileName)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IFileWriter):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
