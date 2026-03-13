import typing
from underautomation.yaskawa.http.http_connect_parameters import HttpConnectParameters
from underautomation.yaskawa.http.internal.http_client_base import HttpClientBase
from UnderAutomation.Yaskawa.Http import HttpClient as http_client

class HttpClient(HttpClientBase):
	'''Standalone client class for communicating with Yaskawa Motoman industrial robots via HTTP. Provides file listing and file content retrieval from the robot controller's built-in web server.'''
	def __init__(self, _internal = 0):
		'''Creates a new instance of HttpClient for robot communication. Call Connect() to establish communication with a robot controller.'''
		if(_internal == 0):
			self._instance = http_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, parameters: HttpConnectParameters) -> None:
		'''Connects to the robot controller with custom connection parameters.

		:param ip: IP address or hostname of the robot controller.
		:param parameters: HTTP connection parameters including port and timeouts.
		'''
		self._instance.Connect(ip, parameters._instance if parameters else None)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HttpClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
