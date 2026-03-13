import typing
from underautomation.yaskawa.host_control.internal.host_control_connect_parameters_base import HostControlConnectParametersBase
from UnderAutomation.Yaskawa.HostControl import HostControlEthernetServerConnectParameters as host_control_ethernet_server_connect_parameters

class HostControlEthernetServerConnectParameters(HostControlConnectParametersBase):
	'''Base class defining Ethernet Server (TCP) connection parameters for the Host Control communication. This class provides configuration for TCP-based communication with YRC1000 controllers.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the Ethernet Server connection parameters.'''
		if(_internal == 0):
			self._instance = host_control_ethernet_server_connect_parameters()
		else:
			self._instance = _internal

	@property
	def port(self) -> int:
		'''Gets or sets the TCP port number for Ethernet Server communication. Must match the robot controller's Ethernet Server port configuration. Default: 80.'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlEthernetServerConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default TCP port for Ethernet Server communication (80).
HostControlEthernetServerConnectParameters.DEFAULT_PORT = host_control_ethernet_server_connect_parameters.DEFAULT_PORT
