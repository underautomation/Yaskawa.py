import typing
from UnderAutomation.Yaskawa.HostControl import HostControlException as host_control_exception

class HostControlException:
	'''Exception thrown when a Host Control command fails.'''
	def __init__(self, message: str, command: str, errorCode: str, _internal = 0):
		'''Creates a new HostControlException with the specified message, command, and error code.

		:param message: The error message.
		:param command: The command that caused the exception.
		:param errorCode: The error code from the robot controller.
		'''
		if(_internal == 0):
			self._instance = host_control_exception(message, command, errorCode)
		else:
			self._instance = _internal

	@property
	def error_code(self) -> str:
		'''Gets the error code returned by the robot controller.'''
		return self._instance.ErrorCode

	@property
	def command(self) -> str:
		'''Gets the command that caused the exception.'''
		return self._instance.Command

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
