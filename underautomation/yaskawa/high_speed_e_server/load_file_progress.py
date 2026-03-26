import typing
from __future__ import annotation
from UnderAutomation.Yaskawa.HighSpeedEServer import LoadFileProgress as load_file_progress

class LoadFileProgress:
	'''Contains progress information for file upload (LoadFile) operations. Used with the LoadFileProgressDelegate callback to track upload progress.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = load_file_progress()
		else:
			self._instance = _internal

	@property
	def completed(self) -> bool:
		'''Gets whether the file upload has completed successfully.'''
		return self._instance.Completed

	@property
	def file_name(self) -> str:
		'''Gets the name of the file being uploaded.'''
		return self._instance.FileName

	@property
	def total_bytes(self) -> int:
		'''Gets the total size of the file in bytes.'''
		return self._instance.TotalBytes

	@property
	def loaded_bytes(self) -> int:
		'''Gets the number of bytes uploaded so far.'''
		return self._instance.LoadedBytes

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, LoadFileProgress):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
