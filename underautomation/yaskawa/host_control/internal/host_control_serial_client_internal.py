import typing
from underautomation.yaskawa.host_control.internal.host_control_client_base import HostControlClientBase
from UnderAutomation.Yaskawa.HostControl.Internal import HostControlSerialClientInternal as host_control_serial_client_internal

class HostControlSerialClientInternal(HostControlClientBase):
	'''Internal implementation of the Host Control client for serial (RS-232C) communication. Implements the BSC-LIKE protocol for NX100 and compatible controllers.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_serial_client_internal()
		else:
			self._instance = _internal

	def close(self) -> None:
		'''Closes the serial port connection and releases resources.'''
		self._instance.Close()

	@staticmethod
	def get_port_names() -> typing.List[str]:
		'''Gets available serial port names on the system.

		:returns: Array of available serial port names.
		'''
		return host_control_serial_client_internal.GetPortNames()

	@property
	def connected(self) -> bool:
		'''Gets a value indicating whether the client is connected via serial port.'''
		return self._instance.Connected

	@property
	def port_name(self) -> str:
		'''Gets the serial port name.'''
		return self._instance.PortName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlSerialClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
