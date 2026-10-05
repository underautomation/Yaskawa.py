from __future__ import annotations
import typing
from underautomation.yaskawa.connect_parameters import ConnectParameters
from underautomation.yaskawa.high_speed_e_server.internal.high_speed_e_server_client_internal import HighSpeedEServerClientInternal
from underautomation.yaskawa.host_control.internal.e_server_client_internal import EServerClientInternal
from underautomation.yaskawa.http.internal.http_client_internal import HttpClientInternal
from underautomation.yaskawa.ftp.internal.ftp_client_internal import FtpClientInternal
from underautomation.yaskawa.license.license_info import LicenseInfo
from UnderAutomation.Yaskawa import YaskawaRobot as yaskawa_robot

class _StaticProperty:
	'''Property of the class, readable from the class or from an instance'''
	def __init__(self, fget, fset=None):
		self._fget = fget
		self._fset = fset
		self.__doc__ = fget.__doc__

	def __get__(self, obj, owner=None):
		return self._fget()

	def __set__(self, obj, value):
		if self._fset is None:
			raise AttributeError("read-only property")
		self._fset(value)

class YaskawaRobot:
	'''Main entry point for communicating with Yaskawa Motoman robots. This class provides methods to connect, monitor, and control the robot through multiple interfaces: High Speed Ethernet Server, Ethernet Server (Host Control over TCP), HTTP and FTP.'''
	def __init__(self, _internal = 0):
		'''Creates a new Yaskawa robot instance'''
		if(_internal == 0):
			self._instance = yaskawa_robot()
		else:
			self._instance = _internal

	def connect(self, ip_or_parameters: str | ConnectParameters) -> None:
		'''Connects to the robot by its IP address. Establishes the connection of each protocol enabled by default in ConnectParameters.
		Connects to the robot using the specified parameters. Establishes the connection of each protocol enabled in the parameters.

		:param ip_or_parameters: IP or robot host name. Or: Connection parameters.
		'''
		self._instance.Connect(getattr(ip_or_parameters, '_instance', ip_or_parameters))

	def disconnect(self) -> None:
		'''Disconnects all active connections to the robot controller.'''
		self._instance.Disconnect()

	@staticmethod
	def register_license(Licensee: str, key: str) -> LicenseInfo:
		'''If you have a license And a key, please call this static method to register the product And exit the trial period ou can register a product even if the trial period has ended

		:param Licensee: Your organization name
		:param key: The associated key supplied by UnderAutomation
		:returns: Information about the supplied license
		'''
		return LicenseInfo(None, None, yaskawa_robot.RegisterLicense(Licensee, key))

	@property
	def connected(self) -> bool:
		'''Indicates whether any communication interface (High Speed Ethernet Server, Ethernet Server, HTTP or FTP) is currently connected.'''
		return self._instance.Connected

	@property
	def high_speed_e_server(self) -> HighSpeedEServerClientInternal:
		'''Access High Speed Ethernet Server features. Provides high-speed UDP-based communication for real-time robot monitoring and control.'''
		return HighSpeedEServerClientInternal(self._instance.HighSpeedEServer)

	@property
	def e_server(self) -> EServerClientInternal:
		'''Access Host Control features via Ethernet Server (TCP). Supports YRC1000 and compatible controllers. Connected automatically when calling Connect() with EServer.Enable = true.'''
		return EServerClientInternal(self._instance.EServer)

	@property
	def http(self) -> HttpClientInternal:
		'''Access HTTP features for file listing and file content retrieval. Communicates with the robot controller's built-in web server. Connected automatically when calling Connect() with Http.Enable = true.'''
		return HttpClientInternal(self._instance.Http)

	@property
	def ftp(self) -> FtpClientInternal:
		'''Access FTP features for file upload, download, listing, and management. Communicates with the robot controller's built-in FTP server. Connected automatically when calling Connect() with Ftp.Enable = true.'''
		return FtpClientInternal(self._instance.Ftp)

	@staticmethod
	def _get_license_info() -> LicenseInfo:
		'''Return information about your license'''
		return LicenseInfo(None, None, yaskawa_robot.LicenseInfo)

	license_info = _StaticProperty(_get_license_info)
	del _get_license_info

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, YaskawaRobot):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
