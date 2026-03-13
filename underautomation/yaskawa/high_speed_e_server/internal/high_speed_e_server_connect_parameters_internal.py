import typing
from underautomation.yaskawa.high_speed_e_server.high_speed_e_server_connect_parameters import HighSpeedEServerConnectParameters
from UnderAutomation.Yaskawa.HighSpeedEServer.Internal import HighSpeedEServerConnectParametersInternal as high_speed_e_server_connect_parameters_internal

class HighSpeedEServerConnectParametersInternal(HighSpeedEServerConnectParameters):
	'''Represents a set of High Speed Ethernet Server connection parameters'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = high_speed_e_server_connect_parameters_internal()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Gets or sets a value indicating whether to enable the High Speed Ethernet Server connection (default: true).'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HighSpeedEServerConnectParametersInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
