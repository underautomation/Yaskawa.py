from __future__ import annotations
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

	@typing.overload
	def connect(self, ip: str, parameters: HttpConnectParameters) -> None: ...

	@typing.overload
	def connect(self, ip: str) -> None: ...

	def connect(self, *args, **kwargs) -> None:
		'''Connects to the robot controller with custom connection parameters.
		Connects to the robot controller using default parameters.

		Arguments: (ip, parameters)
		Arguments: (ip)
		:param ip: IP address or hostname of the robot controller.
		:param parameters: HTTP connection parameters including port and timeouts.
		'''
		__a = _bind_overload(args, kwargs, ['ip', 'parameters'], {})
		if __a is not None:
			ip, parameters = __a
			self._instance.Connect(ip, parameters._instance if parameters else None)
			return
		__a = _bind_overload(args, kwargs, ['ip'], {})
		if __a is not None:
			ip, = __a
			self._instance.Connect(ip)
			return
		raise TypeError("connect(): no overload takes these arguments")

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

def _bind_overload(args, kwargs, names, defaults):
	if len(args) > len(names) or any(k not in names[len(args):] for k in kwargs):
		return None
	values = list(args)
	for name in names[len(args):]:
		if name in kwargs:
			values.append(kwargs[name])
		elif name in defaults:
			values.append(defaults[name])
		else:
			return None
	return values
