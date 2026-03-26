import typing
from __future__ import annotation
from underautomation.yaskawa.connect_parameters import ConnectParameters
from underautomation.yaskawa.high_speed_e_server.internal.high_speed_e_server_client_internal import HighSpeedEServerClientInternal
from underautomation.yaskawa.license.license_info import LicenseInfo
from UnderAutomation.Yaskawa import YaskawaRobot as yaskawa_robot

class YaskawaRobot:
	'''Main entry point for communicating with Yaskawa Motoman robots. This class provides methods to connect, monitor, and control the robot through multiple interfaces: High Speed Ethernet Server'''
	def __init__(self, _internal = 0):
		'''Creates a new Yaskawa robot instance'''
		if(_internal == 0):
			self._instance = yaskawa_robot()
		else:
			self._instance = _internal

	def connect(self, parameters: ConnectParameters) -> None:
		'''Connects to the robot using the specified parameters. Establishes connections for High Speed Ethernet Server.

		:param parameters: Connection parameters
		'''
		self._instance.Connect(parameters._instance if parameters else None)

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
		'''Indicates whether the High Speed Ethernet Server is currently connected and enabled.'''
		return self._instance.Connected

	@property
	def high_speed_e_server(self) -> HighSpeedEServerClientInternal:
		'''Access High Speed Ethernet Server features. Provides high-speed UDP-based communication for real-time robot monitoring and control.'''
		return HighSpeedEServerClientInternal(self._instance.HighSpeedEServer)

	@property
	def license_info(self) -> LicenseInfo:
		'''Return information about your license'''
		return LicenseInfo(None, None, self._instance.LicenseInfo)

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
