import typing
from UnderAutomation.Yaskawa.HostControl.Internal import HostControlConnectParametersBase as host_control_connect_parameters_base

class HostControlConnectParametersBase:
	'''Base class defining connection parameters for the Host Control communication. This class cannot be instantiated directly; use HostControlSerialConnectParameters or HostControlEthernetConnectParameters instead.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_connect_parameters_base()
		else:
			self._instance = _internal

	@property
	def timeout_milliseconds(self) -> int:
		'''Gets or sets the maximum time in milliseconds to wait for a response to commands. Default: 5000ms.'''
		return self._instance.TimeoutMilliseconds

	@timeout_milliseconds.setter
	def timeout_milliseconds(self, value: int):
		self._instance.TimeoutMilliseconds = value

	@property
	def power_on_timeout_milliseconds(self) -> int:
		'''Gets or sets the maximum time in milliseconds to wait for servo power on to complete. Servo power on may take longer due to brake release and motor initialization. Default: 10000ms.'''
		return self._instance.PowerOnTimeoutMilliseconds

	@power_on_timeout_milliseconds.setter
	def power_on_timeout_milliseconds(self, value: int):
		self._instance.PowerOnTimeoutMilliseconds = value

	@property
	def motion_timeout_milliseconds(self) -> int:
		'''Gets or sets the maximum time in milliseconds to wait for motion commands to complete. Motion commands may take longer depending on the distance to travel. Default: 30000ms.'''
		return self._instance.MotionTimeoutMilliseconds

	@motion_timeout_milliseconds.setter
	def motion_timeout_milliseconds(self, value: int):
		self._instance.MotionTimeoutMilliseconds = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlConnectParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default timeout in milliseconds for commands (5000ms).
HostControlConnectParametersBase.DEFAULT_TIMEOUT_MILLISECONDS = host_control_connect_parameters_base.DEFAULT_TIMEOUT_MILLISECONDS

# Default timeout in milliseconds for servo power on operations (10000ms).
HostControlConnectParametersBase.DEFAULT_POWER_ON_TIMEOUT_MILLISECONDS = host_control_connect_parameters_base.DEFAULT_POWER_ON_TIMEOUT_MILLISECONDS

# Default timeout in milliseconds for motion commands (30000ms).
HostControlConnectParametersBase.DEFAULT_MOTION_TIMEOUT_MILLISECONDS = host_control_connect_parameters_base.DEFAULT_MOTION_TIMEOUT_MILLISECONDS
