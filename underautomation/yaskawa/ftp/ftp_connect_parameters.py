from __future__ import annotations
import typing
from UnderAutomation.Yaskawa.Ftp import FtpConnectParameters as ftp_connect_parameters

class FtpConnectParameters:
	'''Connection parameters for FTP communication with the Yaskawa robot controller.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the FTP connection parameters with default values.'''
		if(_internal == 0):
			self._instance = ftp_connect_parameters()
		else:
			self._instance = _internal

	@property
	def ftp_user(self) -> str:
		'''Gets or sets the FTP user name used to authenticate with the robot controller. Standard accounts: rcmaster: widest rights, requires the management mode password.ftp: standard mode only, accepts any password.anonymous: standard mode only, accepts any password, download only. If the password protection option is enabled on the controller, only a user defined in that option is valid. The standard accounts above are then unavailable. Default: "anonymous".'''
		return self._instance.FtpUser

	@ftp_user.setter
	def ftp_user(self, value: str):
		self._instance.FtpUser = value

	@property
	def ftp_password(self) -> str:
		'''Gets or sets the FTP password associated with ftp_user. For rcmaster: must be the controller management mode password.For ftp or anonymous: any value is accepted (including null or empty).If the password protection option is enabled: use the password defined in that option. Default: null.'''
		return self._instance.FtpPassword

	@ftp_password.setter
	def ftp_password(self, value: str):
		self._instance.FtpPassword = value

	@property
	def port(self) -> int:
		'''Gets or sets the FTP port number. Default: 21.'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	@property
	def timeout_milliseconds(self) -> int:
		'''Gets or sets the timeout in milliseconds applied to FTP read, connect, and data transfer operations. Default: 30000ms.'''
		return self._instance.TimeoutMilliseconds

	@timeout_milliseconds.setter
	def timeout_milliseconds(self, value: int):
		self._instance.TimeoutMilliseconds = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default FTP port (21).
FtpConnectParameters.DEFAULT_PORT = ftp_connect_parameters.DEFAULT_PORT

# Default timeout in milliseconds for FTP operations (30000ms).
FtpConnectParameters.DEFAULT_TIMEOUT_MILLISECONDS = ftp_connect_parameters.DEFAULT_TIMEOUT_MILLISECONDS
