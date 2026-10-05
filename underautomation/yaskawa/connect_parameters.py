from __future__ import annotations
import typing
from underautomation.yaskawa.high_speed_e_server.internal.high_speed_e_server_connect_parameters_internal import HighSpeedEServerConnectParametersInternal
from underautomation.yaskawa.host_control.internal.e_server_connect_parameters_internal import EServerConnectParametersInternal
from underautomation.yaskawa.http.internal.http_connect_parameters_internal import HttpConnectParametersInternal
from underautomation.yaskawa.ftp.internal.ftp_connect_parameters_internal import FtpConnectParametersInternal
from UnderAutomation.Yaskawa import ConnectParameters as connect_parameters

class ConnectParameters:
	'''Contains a set of connection parameters for robot communication. Supports High Speed Ethernet Server and Host Control protocols.'''
	def __init__(self, ip: str, _internal = 0):
		'''Creates a new set of connect parameters and defines IP property'''
		if(_internal == 0):
			self._instance = connect_parameters(ip)
		else:
			self._instance = _internal

	@property
	def ping_before_connect(self) -> bool:
		'''Send a ping command before connecting'''
		return self._instance.PingBeforeConnect

	@ping_before_connect.setter
	def ping_before_connect(self, value: bool):
		self._instance.PingBeforeConnect = value

	@property
	def ip(self) -> str:
		'''IP Adress or robot host name'''
		return self._instance.IP

	@ip.setter
	def ip(self, value: str):
		self._instance.IP = value

	@property
	def high_speed_e_server(self) -> HighSpeedEServerConnectParametersInternal:
		'''High Speed Ethernet Server connect parameters'''
		return HighSpeedEServerConnectParametersInternal(self._instance.HighSpeedEServer)

	@high_speed_e_server.setter
	def high_speed_e_server(self, value: HighSpeedEServerConnectParametersInternal):
		self._instance.HighSpeedEServer = value._instance if value else None

	@property
	def e_server(self) -> EServerConnectParametersInternal:
		'''Ethernet Server connect parameters. Used for TCP-based Host Control communication via Ethernet Server.'''
		return EServerConnectParametersInternal(self._instance.EServer)

	@e_server.setter
	def e_server(self, value: EServerConnectParametersInternal):
		self._instance.EServer = value._instance if value else None

	@property
	def http(self) -> HttpConnectParametersInternal:
		'''HTTP connect parameters. Used for file listing and file content retrieval via the robot's built-in web server.'''
		return HttpConnectParametersInternal(self._instance.Http)

	@http.setter
	def http(self, value: HttpConnectParametersInternal):
		self._instance.Http = value._instance if value else None

	@property
	def ftp(self) -> FtpConnectParametersInternal:
		'''FTP connect parameters. Used for file upload, download, listing and management via the robot's built-in FTP server.'''
		return FtpConnectParametersInternal(self._instance.Ftp)

	@ftp.setter
	def ftp(self, value: FtpConnectParametersInternal):
		self._instance.Ftp = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
