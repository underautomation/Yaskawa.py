import typing
from underautomation.yaskawa.host_control.host_control_serial_connect_parameters import HostControlSerialConnectParameters
from underautomation.yaskawa.host_control.internal.host_control_serial_client_internal import HostControlSerialClientInternal
from UnderAutomation.Yaskawa.HostControl import HostControlSerialClient as host_control_serial_client

class HostControlSerialClient(HostControlSerialClientInternal):
	'''Standalone client class for communicating with Yaskawa Motoman industrial robots using the Host Control protocol via serial (RS-232C). This class provides methods for reading robot status, positions, variables, and controlling robot operations.'''
	def __init__(self, _internal = 0):
		'''Creates a new instance of HostControlSerialClient for robot communication via serial port. Call Connect() to establish communication with a robot controller.'''
		if(_internal == 0):
			self._instance = host_control_serial_client()
		else:
			self._instance = _internal

	def connect(self, parameters: HostControlSerialConnectParameters) -> None:
		'''Connects to the robot controller via serial port.

		:param parameters: Serial connection parameters including port name, baud rate, etc.
		'''
		self._instance.Connect(parameters._instance if parameters else None)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlSerialClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
