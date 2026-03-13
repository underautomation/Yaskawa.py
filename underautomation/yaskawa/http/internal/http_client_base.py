import typing
from underautomation.yaskawa.http.file_description import FileDescription
from underautomation.yaskawa.common.file_extension import FileExtension
from UnderAutomation.Yaskawa.Http.Internal import HttpClientBase as http_client_base
from UnderAutomation.Yaskawa.Common import FileExtension as file_extension

class HttpClientBase:
	'''Base class implementing HTTP communication with Yaskawa robot controllers. Provides file listing and file content retrieval via the controller's built-in HTTP server.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = http_client_base()
		else:
			self._instance = _internal

	def close(self) -> None:
		'''Marks the client as disconnected.'''
		self._instance.Close()

	def get_file_list(self, fileExtension: FileExtension) -> typing.List[FileDescription]:
		'''Gets the list of files of the specified type available on the robot controller.

		:param fileExtension: The type of files to list.
		:returns: An array of file descriptions.
		'''
		return [FileDescription(x) for x in self._instance.GetFileList(file_extension(int(fileExtension)))]

	def get_file(self, fileName: str) -> str:
		'''Gets the content of a file from the robot controller. The file type is deduced from the file name extension (e.g. "PICK_JOB.JBI" queries /FGET_REQUEST/ROBOT/JOB/PICK_JOB.JBI).

		:param fileName: File name including extension (e.g. "PICK_JOB.JBI", "VAR.DAT").
		:returns: The text content of the file.
		'''
		return self._instance.GetFile(fileName)

	@property
	def connected(self) -> bool:
		'''Indicates whether the client is configured and ready to communicate.'''
		return self._instance.Connected

	@property
	def ip(self) -> str:
		'''Gets the IP address or hostname of the robot controller.'''
		return self._instance.IP

	@property
	def port(self) -> int:
		'''Gets the HTTP port number.'''
		return self._instance.Port

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HttpClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
