import typing
from underautomation.yaskawa.common.io_type import IOType
from UnderAutomation.Yaskawa.Common import IoHelpers as io_helpers
from UnderAutomation.Yaskawa.Common import IOType as io_type

class IoHelpers:
	'''Helper methods for handling Yaskawa I/O group conversions and related utilities.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_helpers()
		else:
			self._instance = _internal

	@staticmethod
	def convert_io_group_to_bit_address(type: IOType, group: int, bitIndex: int) -> int:
		'''Converts an I/O group address (type + group + bit) to a flat Yaskawa 5-digit contact number.

		:param type: The I/O signal category.
		:param group: 1-based group number within the I/O type.
		:param bitIndex: Bit index within the group (0–7).
		:returns: The flat contact number (bit address).
		'''
		return io_helpers.ConvertIOGroupToBitAddress(io_type(int(type)), group, bitIndex)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IoHelpers):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
