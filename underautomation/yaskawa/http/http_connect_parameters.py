import typing
from UnderAutomation.Yaskawa.Http import HttpConnectParameters as http_connect_parameters

class HttpConnectParameters:
	'''Connection parameters for HTTP communication with the robot controller.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the HTTP connection parameters.'''
		if(_internal == 0):
			self._instance = http_connect_parameters()
		else:
			self._instance = _internal

	@property
	def port(self) -> int:
		'''Gets or sets the HTTP port number. Default: 80.'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	@property
	def timeout_milliseconds(self) -> int:
		'''Gets or sets the maximum time in milliseconds to wait for a response. Default: 5000ms.'''
		return self._instance.TimeoutMilliseconds

	@timeout_milliseconds.setter
	def timeout_milliseconds(self, value: int):
		self._instance.TimeoutMilliseconds = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HttpConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default HTTP port (80).
HttpConnectParameters.DEFAULT_PORT = http_connect_parameters.DEFAULT_PORT

# Default timeout in milliseconds for HTTP requests (5000ms).
HttpConnectParameters.DEFAULT_TIMEOUT_MILLISECONDS = http_connect_parameters.DEFAULT_TIMEOUT_MILLISECONDS
