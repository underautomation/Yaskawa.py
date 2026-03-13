import typing
from underautomation.yaskawa.http.internal.http_client_base import HttpClientBase
from UnderAutomation.Yaskawa.Http.Internal import HttpClientInternal as http_client_internal

class HttpClientInternal(HttpClientBase):
	'''Internal implementation of the HTTP client. This class is not intended for direct use by application code. Use YaskawaRobot instead.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = http_client_internal()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HttpClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
