import typing
from underautomation.yaskawa.host_control.internal.host_control_client_base import HostControlClientBase
from UnderAutomation.Yaskawa.HostControl.Internal import HostControlEthernetClientInternal as host_control_ethernet_client_internal

class HostControlEthernetClientInternal(HostControlClientBase):
	'''Internal implementation of the Host Control client for Ethernet (UDP) communication. Implements the ASCII text-based protocol for YRC1000 and compatible controllers.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_ethernet_client_internal()
		else:
			self._instance = _internal

	def close(self) -> None:
		'''Closes the UDP connection and releases resources.'''
		self._instance.Close()

	def reconnect(self) -> None:
		'''Reconnects to the robot controller if the connection was lost.'''
		self._instance.Reconnect()

	@property
	def connected(self) -> bool:
		'''Gets a value indicating whether the client is connected via UDP.'''
		return self._instance.Connected

	@property
	def ip(self) -> str:
		'''Gets the IP address or hostname of the connected robot controller.'''
		return self._instance.IP

	@property
	def port(self) -> int:
		'''Gets the UDP port number for commands.'''
		return self._instance.Port

	@property
	def file_port(self) -> int:
		'''Gets the UDP port number for file operations.'''
		return self._instance.FilePort

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlEthernetClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
