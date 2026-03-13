import typing
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from UnderAutomation.Yaskawa.HostControl import HostControlIOData as host_control_io_data

class HostControlIOData(HostControlResponse):
	'''Contains I/O signal data. Retrieved using the IOREAD command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_io_data()
		else:
			self._instance = _internal

	def get_bit(self, bitOffset: int) -> bool:
		'''Gets the bit value at the specified offset from the start address.

		:param bitOffset: The bit offset from the start address (0-based).
		:returns: True if the bit is set, false otherwise.
		'''
		return self._instance.GetBit(bitOffset)

	@property
	def start_address(self) -> int:
		'''Gets or sets the starting I/O contact number.'''
		return self._instance.StartAddress

	@property
	def count(self) -> int:
		'''Gets or sets the number of I/O bytes read.'''
		return self._instance.Count

	@property
	def data(self) -> typing.List[int]:
		'''Gets or sets the I/O data bytes.'''
		return self._instance.Data

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlIOData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
