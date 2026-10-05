from __future__ import annotations
import typing
from underautomation.yaskawa.ftp.internal.ftp_client_base import FtpClientBase
from UnderAutomation.Yaskawa.Ftp import FtpClient as ftp_client

class FtpClient(FtpClientBase):
	'''Standalone FTP client for connecting directly to a Yaskawa robot controller.'''
	def __init__(self, _internal = 0):
		'''Creates a new standalone FTP client instance.'''
		if(_internal == 0):
			self._instance = ftp_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, user: str="anonymous", password: str=None, port: int=21, timeoutMilliseconds: int=30000) -> None:
		'''Connects to the robot controller via FTP.

		:param ip: IP address or host name of the robot controller.
		:param user: FTP user name. Defaults to "anonymous". See ftp_user for a description of available accounts.
		:param password: FTP password for user. Defaults to null (accepted by ftp and anonymous accounts).
		:param port: FTP port. Defaults to DEFAULT_PORT (21).
		:param timeoutMilliseconds: Timeout in milliseconds for read, connect and data transfer operations. Defaults to DEFAULT_TIMEOUT_MILLISECONDS (30000ms).
		'''
		self._instance.Connect(ip, user, password, port, timeoutMilliseconds)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
