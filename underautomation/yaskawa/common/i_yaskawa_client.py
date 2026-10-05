from __future__ import annotations
import typing
from UnderAutomation.Yaskawa.Common import IYaskawaClient as i_yaskawa_client

class IYaskawaClient:
	'''Base interface for all Yaskawa robot communication clients. Provides connection management shared across all communication protocols.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_yaskawa_client()
		else:
			self._instance = _internal

	def close(self) -> None:
		'''Closes the connection to the robot controller and releases resources.'''
		self._instance.Close()

	@property
	def address(self) -> str:
		'''Gets the address of the robot controller: an IP address or a host name.'''
		return self._instance.Address

	@property
	def connected(self) -> bool:
		'''Gets a value indicating whether the client is connected to a robot controller.'''
		return self._instance.Connected

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IYaskawaClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
