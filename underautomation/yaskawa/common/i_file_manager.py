from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_file_reader import IFileReader
from underautomation.yaskawa.common.i_yaskawa_client import IYaskawaClient
from underautomation.yaskawa.common.i_file_writer import IFileWriter
from UnderAutomation.Yaskawa.Common import IFileManager as i_file_manager

class IFileManager(IFileReader, IFileWriter):
	'''Provides complete file management: read, write, list, and delete operations.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_file_manager()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IFileManager):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
