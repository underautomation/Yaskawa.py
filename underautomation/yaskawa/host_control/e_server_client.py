import typing
from underautomation.yaskawa.host_control.e_server_connect_parameters import EServerConnectParameters
from underautomation.yaskawa.host_control.internal.e_server_client_internal import EServerClientInternal
from UnderAutomation.Yaskawa.HostControl import EServerClient as e_server_client

class EServerClient(EServerClientInternal):
	'''Standalone client class for communicating with Yaskawa Motoman industrial robots using the Host Control protocol via Ethernet Server (TCP). This class provides methods for reading robot status, positions, variables, and controlling robot operations.'''
	def __init__(self, _internal = 0):
		'''Creates a new instance of EServerClient for robot communication via TCP. Call Connect() to configure communication with a robot controller.'''
		if(_internal == 0):
			self._instance = e_server_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, parameters: EServerConnectParameters) -> None:
		'''Configures connection to the robot controller via TCP.

		:param ip: IP address or hostname of the robot controller.
		:param parameters: Ethernet Server connection parameters including port and timeouts.
		'''
		self._instance.Connect(ip, parameters._instance if parameters else None)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, EServerClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
