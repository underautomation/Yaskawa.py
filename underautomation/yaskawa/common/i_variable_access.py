from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_yaskawa_client import IYaskawaClient
from UnderAutomation.Yaskawa.Common import IVariableAccess as i_variable_access

class IVariableAccess(IYaskawaClient):
	'''Provides typed read/write access to robot controller variables.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_variable_access()
		else:
			self._instance = _internal

	def read_byte(self, firstIndex: int, count: int) -> typing.List[int]:
		'''Reads byte (B) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param count: Number of variables to read.
		:returns: Array of byte values.
		'''
		return self._instance.ReadByte(firstIndex, count)

	def write_byte(self, firstIndex: int, data: typing.List[int]) -> None:
		'''Writes byte (B) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param data: Byte values to write.
		'''
		self._instance.WriteByte(firstIndex, data)

	def read_integer(self, firstIndex: int, count: int) -> typing.List[int]:
		'''Reads integer (I) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param count: Number of variables to read.
		:returns: Array of 16-bit signed integer values.
		'''
		return self._instance.ReadInteger(firstIndex, count)

	def write_integer(self, firstIndex: int, data: typing.List[int]) -> None:
		'''Writes integer (I) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param data: Integer values to write.
		'''
		self._instance.WriteInteger(firstIndex, data)

	def read_double_integer(self, firstIndex: int, count: int) -> typing.List[int]:
		'''Reads double integer (D) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param count: Number of variables to read.
		:returns: Array of 32-bit signed integer values.
		'''
		return self._instance.ReadDoubleInteger(firstIndex, count)

	def write_double_integer(self, firstIndex: int, data: typing.List[int]) -> None:
		'''Writes double integer (D) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param data: Double integer values to write.
		'''
		self._instance.WriteDoubleInteger(firstIndex, data)

	def read_real(self, firstIndex: int, count: int) -> typing.List[float]:
		'''Reads real (R) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param count: Number of variables to read.
		:returns: Array of floating-point values.
		'''
		return self._instance.ReadReal(firstIndex, count)

	def write_real(self, firstIndex: int, data: typing.List[float]) -> None:
		'''Writes real (R) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param data: Real values to write.
		'''
		self._instance.WriteReal(firstIndex, data)

	def read16_bytes_char(self, firstIndex: int, count: int) -> typing.List[str]:
		'''Reads 16-byte string (S) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param count: Number of variables to read.
		:returns: Array of string values.
		'''
		return self._instance.Read16BytesChar(firstIndex, count)

	def write16_bytes_char(self, firstIndex: int, data: typing.List[str]) -> None:
		'''Writes 16-byte string (S) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param data: String values to write.
		'''
		self._instance.Write16BytesChar(firstIndex, data)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IVariableAccess):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
