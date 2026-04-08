from __future__ import annotations
import typing
from UnderAutomation.Yaskawa.HighSpeedEServer import InvalidDataAnswerException as invalid_data_answer_exception

class InvalidDataAnswerException:
	'''Exception thrown when the robot controller returns an error response to a High Speed Ethernet Server command. This exception contains detailed status codes that help identify the specific error condition.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = invalid_data_answer_exception()
		else:
			self._instance = _internal

	@property
	def status(self) -> int:
		'''Gets the primary status code returned by the robot controller. A value of 0 indicates success; any other value indicates an error condition.'''
		return self._instance.Status

	@property
	def added_status(self) -> int:
		'''Gets the additional status code providing more detailed error information. The interpretation of this value depends on the primary Status code.'''
		return self._instance.AddedStatus

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, InvalidDataAnswerException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
