import typing
from underautomation.yaskawa.host_control.host_control_ethernet_connect_parameters import HostControlEthernetConnectParameters
from underautomation.yaskawa.host_control.internal.host_control_ethernet_client_internal import HostControlEthernetClientInternal
from UnderAutomation.Yaskawa.HostControl import HostControlEthernetClient as host_control_ethernet_client

class HostControlEthernetClient(HostControlEthernetClientInternal):
	'''Standalone client class for communicating with Yaskawa Motoman industrial robots using the Host Control protocol via Ethernet (UDP). This class provides methods for reading robot status, positions, variables, and controlling robot operations.'''
	def __init__(self, _internal = 0):
		'''Creates a new instance of HostControlEthernetClient for robot communication via UDP. Call Connect() to establish communication with a robot controller.'''
		if(_internal == 0):
			self._instance = host_control_ethernet_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, parameters: HostControlEthernetConnectParameters) -> None:
		'''Connects to the robot controller via UDP.

		:param ip: IP address or hostname of the robot controller.
		:param parameters: Ethernet connection parameters including port and timeouts.
		'''
		self._instance.Connect(ip, parameters._instance if parameters else None)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlEthernetClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
