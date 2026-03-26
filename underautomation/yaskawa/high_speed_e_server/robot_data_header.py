import typing
from __future__ import annotation
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotDataHeader as robot_data_header

class RobotDataHeader:
	'''Contains header information extracted from a High Speed Ethernet Server response packet. Provides metadata about the communication including source address, data size, and transfer status.'''
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
		'''Gets the size of the data payload in the response packet. Does not include the header size.'''
		return self._instance.DataSize

	@property
	def block_no(self) -> int:
		'''Gets the block number for multi-block transfers. The most significant bit (0x80000000) indicates this is the last block. Used primarily for file transfer operations.'''
		return self._instance.BlockNo

	@property
	def is_last_block(self) -> bool:
		'''Gets a value indicating whether this is the last block in a multi-block transfer. Returns true when the MSB of BlockNo is set (0x80000000).'''
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
