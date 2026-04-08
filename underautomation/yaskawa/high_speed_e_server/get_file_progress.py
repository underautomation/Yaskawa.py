from __future__ import annotations
import typing
from UnderAutomation.Yaskawa.HighSpeedEServer import GetFileProgress as get_file_progress

class GetFileProgress:
	'''Contains progress information for file download (GetFile) operations. Used with the GetFileProgressDelegate callback to track download progress.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = get_file_progress()
		else:
			self._instance = _internal

	@property
	def completed(self) -> bool:
		'''Gets whether the file download has completed successfully.'''
		return self._instance.Completed

	@property
	def file_name(self) -> str:
		'''Gets the name of the file being downloaded.'''
		return self._instance.FileName

	@property
	def downloaded_bytes(self) -> int:
		'''Gets the number of bytes downloaded so far.'''
		return self._instance.DownloadedBytes

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetFileProgress):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
