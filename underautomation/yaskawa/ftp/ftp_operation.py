from enum import IntEnum

class FtpOperation(IntEnum):
	'''FTP operation that was running when an FtpException was thrown.'''
	Connect = 0 # Connection and login to the controller.
	List = 1 # Listing of files or folders.
	Download = 2 # File download from the controller.
	Upload = 3 # File upload to the controller.
	Delete = 4 # File deletion on the controller.
