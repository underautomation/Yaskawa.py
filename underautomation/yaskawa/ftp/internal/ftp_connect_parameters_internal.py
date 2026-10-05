from __future__ import annotations
import typing
from underautomation.yaskawa.ftp.ftp_connect_parameters import FtpConnectParameters
from UnderAutomation.Yaskawa.Ftp.Internal import FtpConnectParametersInternal as ftp_connect_parameters_internal

class FtpConnectParametersInternal(FtpConnectParameters):
	'''FTP connection parameters with an enable flag, used by ConnectParameters.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_connect_parameters_internal()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Gets or sets a value indicating whether to establish an FTP connection when calling connect(). Default: false.'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpConnectParametersInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
