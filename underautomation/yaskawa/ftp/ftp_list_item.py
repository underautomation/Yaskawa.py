from __future__ import annotations
import typing
from datetime import datetime, timedelta
from underautomation.yaskawa.ftp.ftp_file_system_object_type import FtpFileSystemObjectType
from UnderAutomation.Yaskawa.Ftp import FtpListItem as ftp_list_item
from UnderAutomation.Yaskawa.Ftp import FtpFileSystemObjectType as ftp_file_system_object_type

class FtpListItem:
	'''Represents a file or a folder on the robot controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_list_item()
		else:
			self._instance = _internal

	@property
	def full_name(self) -> str:
		'''Full path on the controller (e.g. "/JOB/TEST.JBI").'''
		return self._instance.FullName

	@property
	def name(self) -> str:
		'''File or folder name without its path (e.g. "TEST.JBI").'''
		return self._instance.Name

	@property
	def modified(self) -> datetime:
		'''Date and time of the last modification, as given by the controller.'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.Modified.Ticks // 10)

	@property
	def type(self) -> FtpFileSystemObjectType:
		'''Indicates whether this item is a file or a folder.'''
		return FtpFileSystemObjectType(int(self._instance.Type))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpListItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
