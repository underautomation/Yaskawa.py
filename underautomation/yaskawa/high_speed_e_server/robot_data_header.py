from __future__ import annotations
import typing
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotDataHeader as robot_data_header

class RobotDataHeader:
	'''Information about a response of the robot controller: the controller that answered, the size of the data, and the state of a transfer in several parts.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_data_header()
		else:
			self._instance = _internal

	@property
	def ip(self) -> typing.Any:
		'''Gets the IP endpoint (address and port) of the robot controller that sent the response. Useful for identifying the source in multi-robot configurations.'''
		return self._instance.IP

	@property
	def data_size(self) -> int:
		'''Gets the size, in bytes, of the data returned by the controller in this response.'''
		return self._instance.DataSize

	@property
	def block_no(self) -> int:
		'''Gets the raw block number of a transfer in several parts, such as a file transfer. Use is_last_block to know if this response is the last part.'''
		return self._instance.BlockNo

	@property
	def is_last_block(self) -> bool:
		'''Gets a value indicating whether this response is the last part of a transfer in several parts.'''
		return self._instance.IsLastBlock

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotDataHeader):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
