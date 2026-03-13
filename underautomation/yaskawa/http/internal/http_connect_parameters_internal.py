import typing
from underautomation.yaskawa.http.http_connect_parameters import HttpConnectParameters
from UnderAutomation.Yaskawa.Http.Internal import HttpConnectParametersInternal as http_connect_parameters_internal

class HttpConnectParametersInternal(HttpConnectParameters):
	'''Connection parameters for HTTP communication with the robot controller, with enable flag.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = http_connect_parameters_internal()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Gets or sets a value indicating whether to enable the HTTP connection (default: false).'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HttpConnectParametersInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
