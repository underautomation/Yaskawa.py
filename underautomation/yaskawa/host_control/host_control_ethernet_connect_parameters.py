import typing
from underautomation.yaskawa.host_control.internal.host_control_connect_parameters_base import HostControlConnectParametersBase
from UnderAutomation.Yaskawa.HostControl import HostControlEthernetConnectParameters as host_control_ethernet_connect_parameters

class HostControlEthernetConnectParameters(HostControlConnectParametersBase):
	'''Base class defining Ethernet (UDP) connection parameters for the Host Control communication. This class provides configuration for network-based communication with YRC1000 controllers.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the Ethernet connection parameters.'''
		if(_internal == 0):
			self._instance = host_control_ethernet_connect_parameters()
		else:
			self._instance = _internal

	@property
	def port(self) -> int:
		'''Gets or sets the UDP port number for Host Control command communication. Must match the robot controller's Host Control port configuration. Default: 10000.'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	@property
	def file_port(self) -> int:
		'''Gets or sets the UDP port number for Host Control file operations. Default: 10006.'''
		return self._instance.FilePort

	@file_port.setter
	def file_port(self, value: int):
		self._instance.FilePort = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlEthernetConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default UDP port for Host Control command communication (10000).
HostControlEthernetConnectParameters.DEFAULT_PORT = host_control_ethernet_connect_parameters.DEFAULT_PORT

# Default UDP port for Host Control file operations (10006).
HostControlEthernetConnectParameters.DEFAULT_FILE_PORT = host_control_ethernet_connect_parameters.DEFAULT_FILE_PORT
