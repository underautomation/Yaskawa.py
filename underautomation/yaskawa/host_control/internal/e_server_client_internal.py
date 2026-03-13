import typing
from underautomation.yaskawa.host_control.internal.host_control_client_base import HostControlClientBase
from UnderAutomation.Yaskawa.HostControl.Internal import EServerClientInternal as e_server_client_internal

class EServerClientInternal(HostControlClientBase):
	'''Internal implementation of the Host Control client for Ethernet Server (TCP) communication. Implements the CONNECT/HOSTCTRL_REQUEST protocol for YRC1000 and compatible controllers.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = e_server_client_internal()
		else:
			self._instance = _internal

	def close(self) -> None:
		'''Marks the client as disconnected and releases any stored state.'''
		self._instance.Close()

	@property
	def connected(self) -> bool:
		'''Gets a value indicating whether the client is ready to communicate with the robot. Since each command opens its own TCP connection, this reflects whether Connect has been called.'''
		return self._instance.Connected

	@property
	def ip(self) -> str:
		'''Gets the IP address or hostname of the robot controller.'''
		return self._instance.IP

	@property
	def port(self) -> int:
		'''Gets the TCP port number.'''
		return self._instance.Port

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, EServerClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
