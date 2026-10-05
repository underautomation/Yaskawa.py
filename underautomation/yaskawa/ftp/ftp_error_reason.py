from enum import IntEnum

class FtpErrorReason(IntEnum):
	'''Reason why an FTP operation failed.'''
	Unknown = 0 # The controller refused the operation for another reason. See reply_message.
	LoginIncorrect = 1 # The user name or the password is not accepted by the controller.
	AccessDenied = 2 # The logged user does not have the right to do this operation on this file.
	FileNotFound = 3 # The file does not exist on the controller.
	JobAlreadyExists = 4 # The job already exists on the controller. The controller does not overwrite a job by FTP.
	DeleteRefused = 5 # The controller refused to delete the file.
	ConnectionError = 6 # The connection with the controller was lost or timed out.
