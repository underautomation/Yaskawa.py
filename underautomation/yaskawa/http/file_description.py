import typing
from UnderAutomation.Yaskawa.Http import FileDescription as file_description

class FileDescription:
	'''Describes a file available on the robot controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_description()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''File name including extension.'''
		return self._instance.Name

	@property
	def description(self) -> str:
		'''Description of the file, if available.'''
		return self._instance.Description

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileDescription):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
