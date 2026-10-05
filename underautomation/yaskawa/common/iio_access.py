from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_yaskawa_client import IYaskawaClient
from UnderAutomation.Yaskawa.Common import IIOAccess as iio_access

class IIOAccess(IYaskawaClient):
	'''Provides read/write access to robot I/O signals.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = iio_access()
		else:
			self._instance = _internal

	def read_io(self, startAddress: int, count: int) -> typing.List[int]:
		'''Reads I/O signal bytes from the robot controller. Each byte holds a group of 8 signals.

		:param startAddress: I/O index of the first group: contact number divided by 10 (1 for #00010, 1001 for #10010, 2701 for #27010).
		:param count: Number of bytes to read.
		:returns: Array of I/O byte values.
		'''
		return self._instance.ReadIO(startAddress, count)

	def write_io(self, startAddress: int, data: typing.List[int]) -> None:
		'''Writes I/O signal bytes to the robot controller. Each byte holds a group of 8 signals.

		:param startAddress: I/O index of the first group: contact number divided by 10 (2701 for #27010).
		:param data: Data bytes to write.
		'''
		self._instance.WriteIO(startAddress, data)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IIOAccess):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
