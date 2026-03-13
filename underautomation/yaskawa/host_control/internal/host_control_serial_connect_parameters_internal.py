import typing
from underautomation.yaskawa.host_control.host_control_serial_connect_parameters import HostControlSerialConnectParameters
from UnderAutomation.Yaskawa.HostControl.Internal import HostControlSerialConnectParametersInternal as host_control_serial_connect_parameters_internal

class HostControlSerialConnectParametersInternal(HostControlSerialConnectParameters):
	'''Connection parameters for Host Control serial (RS-232C) communication. Use this class to configure serial port settings for direct cable connection to the robot controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_serial_connect_parameters_internal()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Gets or sets a value indicating whether to enable the Host Control Serial connection (default: false).'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlSerialConnectParametersInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
