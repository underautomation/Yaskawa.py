import typing
from __future__ import annotation
from underautomation.yaskawa.high_speed_e_server.internal.high_speed_e_server_client_base import HighSpeedEServerClientBase
from UnderAutomation.Yaskawa.HighSpeedEServer.Internal import HighSpeedEServerClientInternal as high_speed_e_server_client_internal

class HighSpeedEServerClientInternal(HighSpeedEServerClientBase):
	'''Internal implementation of the High Speed Ethernet Server client. This class provides the concrete implementation used internally by the SDK.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = high_speed_e_server_client_internal()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HighSpeedEServerClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
