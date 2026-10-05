from __future__ import annotations
import typing
from underautomation.yaskawa.ftp.ftp_operation import FtpOperation
from underautomation.yaskawa.ftp.ftp_error_reason import FtpErrorReason
from UnderAutomation.Yaskawa.Ftp import FtpException as ftp_exception
from UnderAutomation.Yaskawa.Ftp import FtpOperation as ftp_operation
from UnderAutomation.Yaskawa.Ftp import FtpErrorReason as ftp_error_reason

class FtpException:
	'''Exception thrown when an FTP operation on the Yaskawa controller fails. The message explains the cause and, when the logged user does not have enough rights, which user to use.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_exception()
		else:
			self._instance = _internal

	@property
	def operation(self) -> FtpOperation:
		'''Operation that failed.'''
		return FtpOperation(int(self._instance.Operation))

	@property
	def reason(self) -> FtpErrorReason:
		'''Reason of the failure.'''
		return FtpErrorReason(int(self._instance.Reason))

	@property
	def remote_path(self) -> str:
		'''Path of the file on the controller concerned by the operation. Null for connection and listing errors.'''
		return self._instance.RemotePath

	@property
	def user(self) -> str:
		'''FTP user name that was logged when the error occurred.'''
		return self._instance.User

	@property
	def reply_code(self) -> int:
		'''FTP reply code returned by the controller (e.g. 550). 0 if the controller did not reply.'''
		return self._instance.ReplyCode

	@property
	def reply_message(self) -> str:
		'''Raw reply text returned by the controller. Null if the controller did not reply.'''
		return self._instance.ReplyMessage

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
