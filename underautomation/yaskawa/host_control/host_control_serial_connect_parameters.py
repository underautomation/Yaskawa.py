import typing
from underautomation.yaskawa.host_control.host_control_parity import HostControlParity
from underautomation.yaskawa.host_control.host_control_stop_bits import HostControlStopBits
from underautomation.yaskawa.host_control.host_control_handshake import HostControlHandshake
from underautomation.yaskawa.host_control.internal.host_control_connect_parameters_base import HostControlConnectParametersBase
from UnderAutomation.Yaskawa.HostControl import HostControlSerialConnectParameters as host_control_serial_connect_parameters
from UnderAutomation.Yaskawa.HostControl import HostControlParity as host_control_parity
from UnderAutomation.Yaskawa.HostControl import HostControlStopBits as host_control_stop_bits
from UnderAutomation.Yaskawa.HostControl import HostControlHandshake as host_control_handshake

class HostControlSerialConnectParameters(HostControlConnectParametersBase):
	'''Base class defining serial (RS-232C) connection parameters for the Host Control communication. This class provides BSC-like protocol configuration for direct serial communication.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_serial_connect_parameters()
		else:
			self._instance = _internal

	@property
	def port_name(self) -> str:
		'''Gets or sets the serial port name (e.g., "COM1", "COM2").'''
		return self._instance.PortName

	@port_name.setter
	def port_name(self, value: str):
		self._instance.PortName = value

	@property
	def baud_rate(self) -> int:
		'''Gets or sets the baud rate for serial communication. Valid values: 150, 300, 600, 1200, 2400, 4800, 9600, 19200. Default: 9600 bps.'''
		return self._instance.BaudRate

	@baud_rate.setter
	def baud_rate(self, value: int):
		self._instance.BaudRate = value

	@property
	def data_bits(self) -> int:
		'''Gets or sets the number of data bits. Valid values: 7 or 8. Default: 8.'''
		return self._instance.DataBits

	@data_bits.setter
	def data_bits(self, value: int):
		self._instance.DataBits = value

	@property
	def parity(self) -> HostControlParity:
		'''Gets or sets the parity checking protocol. Valid values: None, Odd, Even. Default: Even.'''
		return HostControlParity(int(self._instance.Parity))

	@parity.setter
	def parity(self, value: HostControlParity):
		self._instance.Parity = host_control_parity(int(value))

	@property
	def stop_bits(self) -> HostControlStopBits:
		'''Gets or sets the number of stop bits. Valid values: One, OnePointFive, Two. Default: One.'''
		return HostControlStopBits(int(self._instance.StopBits))

	@stop_bits.setter
	def stop_bits(self, value: HostControlStopBits):
		self._instance.StopBits = host_control_stop_bits(int(value))

	@property
	def handshake(self) -> HostControlHandshake:
		'''Gets or sets the handshaking protocol for serial port transmission. Default: RequestToSend (RTS/CTS hardware handshaking).'''
		return HostControlHandshake(int(self._instance.Handshake))

	@handshake.setter
	def handshake(self, value: HostControlHandshake):
		self._instance.Handshake = host_control_handshake(int(value))

	@property
	def retry_count(self) -> int:
		'''Gets or sets the maximum number of retries on no response or invalid response. Default: 10.'''
		return self._instance.RetryCount

	@retry_count.setter
	def retry_count(self, value: int):
		self._instance.RetryCount = value

	@property
	def nak_retry_count(self) -> int:
		'''Gets or sets the maximum number of retries on NAK (block check error). Default: 3.'''
		return self._instance.NakRetryCount

	@nak_retry_count.setter
	def nak_retry_count(self, value: int):
		self._instance.NakRetryCount = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlSerialConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default baud rate for serial communication (9600 bps).
HostControlSerialConnectParameters.DEFAULT_BAUD_RATE = host_control_serial_connect_parameters.DEFAULT_BAUD_RATE

# Default number of data bits (8).
HostControlSerialConnectParameters.DEFAULT_DATA_BITS = host_control_serial_connect_parameters.DEFAULT_DATA_BITS

# Default parity setting (Even).
HostControlSerialConnectParameters.DEFAULT_PARITY = HostControlParity(int(host_control_serial_connect_parameters.DEFAULT_PARITY))

# Default number of stop bits (One).
HostControlSerialConnectParameters.DEFAULT_STOP_BITS = HostControlStopBits(int(host_control_serial_connect_parameters.DEFAULT_STOP_BITS))

# Default handshake/flow control (RTS/CTS hardware handshaking).
HostControlSerialConnectParameters.DEFAULT_HANDSHAKE = HostControlHandshake(int(host_control_serial_connect_parameters.DEFAULT_HANDSHAKE))

# Maximum number of retries for no response or invalid response (10).
HostControlSerialConnectParameters.DEFAULT_RETRY_COUNT = host_control_serial_connect_parameters.DEFAULT_RETRY_COUNT

# Maximum number of retries on NAK (block check error) (3).
HostControlSerialConnectParameters.DEFAULT_NAK_RETRY_COUNT = host_control_serial_connect_parameters.DEFAULT_NAK_RETRY_COUNT
