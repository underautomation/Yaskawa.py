import typing
from UnderAutomation.Yaskawa.HostControl import HostControlResponse as host_control_response

class HostControlResponse:
	'''Base class for all robot data response objects returned by Host Control commands. Contains common response information about the communication.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_response()
		else:
			self._instance = _internal

	@property
	def response_code(self) -> str:
		'''Gets or sets the raw response code from the robot controller. "0000" indicates normal completion.'''
		return self._instance.ResponseCode

	@property
	def command(self) -> str:
		'''Gets or sets the command that was executed.'''
		return self._instance.Command

	@property
	def success(self) -> bool:
		'''Gets a value indicating whether the command completed successfully.'''
		return self._instance.Success

	@property
	def error_message(self) -> str:
		'''Gets or sets the error message if the command failed.'''
		return self._instance.ErrorMessage

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
