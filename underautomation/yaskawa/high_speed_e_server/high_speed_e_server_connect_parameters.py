import typing
from __future__ import annotation
from UnderAutomation.Yaskawa.HighSpeedEServer import HighSpeedEServerConnectParameters as high_speed_e_server_connect_parameters

class HighSpeedEServerConnectParameters:
	'''Base class defining connection parameters for the High Speed Ethernet Server communication. This class cannot be instantiated directly; use a derived class or use Connect with optional parameters. Allows customization of timeouts and ports for different network environments.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the connection parameters class.'''
		if(_internal == 0):
			self._instance = high_speed_e_server_connect_parameters()
		else:
			self._instance = _internal

	@property
	def data_timeout_milliseconds(self) -> int:
		'''Gets or sets the maximum time in milliseconds to wait for a response to data commands. Applies to most read/write operations like position reading, variable access, etc. Default: 1500ms.'''
		return self._instance.DataTimeoutMilliseconds

	@data_timeout_milliseconds.setter
	def data_timeout_milliseconds(self, value: int):
		self._instance.DataTimeoutMilliseconds = value

	@property
	def power_on_timeout_milliseconds(self) -> int:
		'''Gets or sets the maximum time in milliseconds to wait for servo power on to complete. Servo power on may take longer due to brake release and motor initialization. Default: 8000ms.'''
		return self._instance.PowerOnTimeoutMilliseconds

	@power_on_timeout_milliseconds.setter
	def power_on_timeout_milliseconds(self, value: int):
		self._instance.PowerOnTimeoutMilliseconds = value

	@property
	def file_timeout_milliseconds(self) -> int:
		'''Gets or sets the maximum time in milliseconds to wait for file operation responses. File operations may be slower due to larger data transfers and disk I/O on the controller. Default: 4000ms.'''
		return self._instance.FileTimeoutMilliseconds

	@file_timeout_milliseconds.setter
	def file_timeout_milliseconds(self, value: int):
		self._instance.FileTimeoutMilliseconds = value

	@property
	def data_port(self) -> int:
		'''Gets or sets the UDP port number for data communication. Must match the robot controller's High Speed Ethernet Server data port configuration. Default: 10040.'''
		return self._instance.DataPort

	@data_port.setter
	def data_port(self, value: int):
		self._instance.DataPort = value

	@property
	def file_port(self) -> int:
		'''Gets or sets the UDP port number for file transfer operations. Must match the robot controller's High Speed Ethernet Server file port configuration. Default: 10041.'''
		return self._instance.FilePort

	@file_port.setter
	def file_port(self, value: int):
		self._instance.FilePort = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HighSpeedEServerConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default timeout in milliseconds for data commands (1500ms).
HighSpeedEServerConnectParameters.DEFAULT_DATA_TIMEOUT_MILLISECONDS = high_speed_e_server_connect_parameters.DEFAULT_DATA_TIMEOUT_MILLISECONDS

# Default timeout in milliseconds for servo power on operations (8000ms).
HighSpeedEServerConnectParameters.DEFAULT_POWER_ON_TIMEOUT_MILLISECONDS = high_speed_e_server_connect_parameters.DEFAULT_POWER_ON_TIMEOUT_MILLISECONDS

# Default timeout in milliseconds for file operations (4000ms).
HighSpeedEServerConnectParameters.DEFAULT_FILE_TIMEOUT_MILLISECONDS = high_speed_e_server_connect_parameters.DEFAULT_FILE_TIMEOUT_MILLISECONDS

# Default UDP port for data communication (10040).
HighSpeedEServerConnectParameters.DEFAULT_DATA_PORT = high_speed_e_server_connect_parameters.DEFAULT_DATA_PORT

# Default UDP port for file transfer operations (10041).
HighSpeedEServerConnectParameters.DEFAULT_FILE_PORT = high_speed_e_server_connect_parameters.DEFAULT_FILE_PORT
