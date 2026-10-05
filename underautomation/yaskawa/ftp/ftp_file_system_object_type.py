from enum import IntEnum

class FtpFileSystemObjectType(IntEnum):
	'''Type of an item on the controller file system.'''
	File = 0 # A file.
	Directory = 1 # A folder.
