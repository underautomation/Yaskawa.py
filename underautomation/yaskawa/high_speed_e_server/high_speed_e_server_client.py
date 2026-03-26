import typing
from __future__ import annotation
from underautomation.yaskawa.high_speed_e_server.high_speed_e_server_connect_parameters import HighSpeedEServerConnectParameters
from underautomation.yaskawa.high_speed_e_server.internal.high_speed_e_server_client_base import HighSpeedEServerClientBase
from UnderAutomation.Yaskawa.HighSpeedEServer import HighSpeedEServerClient as high_speed_e_server_client

class HighSpeedEServerClient(HighSpeedEServerClientBase):
	'''Main client class for communicating with Yaskawa Motoman industrial robots using the High Speed Ethernet Server protocol. This class provides methods for reading robot status, positions, variables, and controlling robot operations via UDP.'''
	def __init__(self, _internal = 0):
		'''Creates a new instance of HighSpeedEServerClient for robot communication. Call Connect() to establish communication with a robot controller.'''
		if(_internal == 0):
			self._instance = high_speed_e_server_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, parameters: HighSpeedEServerConnectParameters) -> None:
		'''Connects to a robot controller with custom connection parameters object.

		:param ip: IP address or hostname of the robot controller.
		:param parameters: Connection parameters including ports and timeouts.
		'''
		self._instance.Connect(ip, parameters._instance if parameters else None)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HighSpeedEServerClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
