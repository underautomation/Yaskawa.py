from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_file_manager import IFileManager
from underautomation.yaskawa.common.i_file_reader import IFileReader
from underautomation.yaskawa.common.i_yaskawa_client import IYaskawaClient
from underautomation.yaskawa.common.i_file_writer import IFileWriter
from underautomation.yaskawa.common.file_extension import FileExtension
from underautomation.yaskawa.ftp.on_progress_delegate import OnProgressDelegate
from underautomation.yaskawa.ftp.ftp_list_item import FtpListItem
from UnderAutomation.Yaskawa.Ftp.Internal import FtpClientBase as ftp_client_base
from UnderAutomation.Yaskawa.Common import FileExtension as file_extension
from UnderAutomation.Yaskawa.Ftp import OnProgressDelegate as on_progress_delegate

class FtpClientBase(IFileManager):
	'''Abstract base class that implements FTP communication with a Yaskawa robot controller. Provides file management (upload, download, list, delete) via the controller's FTP server.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_client_base()
		else:
			self._instance = _internal

	def close(self) -> None:
		self._instance.Close()

	def get_file(self, fileName: str) -> str:
		'''Downloads a text file from the robot controller and returns its content.

		:param fileName: Name or full path of the file on the controller (e.g. "TEST.JBI" or "/JOB/TEST.JBI").
		:returns: The text content of the file.
		'''
		return self._instance.GetFile(fileName)

	def get_file_list(self, fileExtension: FileExtension) -> typing.List[str]:
		'''Lists the files of the specified type on the controller.

		:param fileExtension: Type of files to list.
		:returns: Array of file names (e.g. "TEST.JBI").
		'''
		return self._instance.GetFileList(file_extension(int(fileExtension)))

	def get_file_list_by_pattern(self, pattern: str) -> typing.List[str]:
		'''Lists the files whose names match the specified pattern. When the pattern has a known extension (e.g. "*.JBI"), only the matching folder is listed. Otherwise, all folders of the controller are listed.

		:param pattern: File name pattern, with '*' and '?' wildcards (e.g. "*.JBI", "VISION*.JBI", "/DAT/*.DAT").
		:returns: Array of matching file names (e.g. "TEST.JBI").
		'''
		return self._instance.GetFileListByPattern(pattern)

	def load_file(self, fileName: str, content: str) -> None:
		'''Uploads text content to the robot controller as a file. The file type is given by the extension of fileName (e.g. ".JBI" for a job).

		:param fileName: Name or full path of the file on the controller (e.g. "TEST.JBI").
		:param content: The text content to write. Must not be empty.
		'''
		self._instance.LoadFile(fileName, content)

	def delete_file(self, fileName: str) -> None:
		'''Deletes a file from the robot controller. The "anonymous" user cannot delete files.

		:param fileName: Name or full path of the file on the controller (e.g. "TEST.JBI").
		'''
		self._instance.DeleteFile(fileName)

	def upload_file(self, remotePath: str, data: typing.List[int], progress: typing.Callable[[float], None] | OnProgressDelegate=None) -> None:
		'''Uploads a byte array as a file onto the controller. Only jobs (.JBI, .JBR), condition files (.CND) and general data (.DAT) can be uploaded, with the "ftp" or "rcmaster" user. An existing job is not overwritten: delete it first with delete_file().

		:param remotePath: Name or full path of the file on the controller (e.g. "TEST.JBI").
		:param data: Full content of the file. Must not be empty.
		:param progress: Reports upload progress as a percentage (0 to 100). -1 indicates indeterminate progress.
		'''
		self._instance.UploadFile(remotePath, data, (progress._instance if isinstance(progress, OnProgressDelegate) else on_progress_delegate(lambda _x0: progress(_x0))) if progress else None)

	def upload_file_from_local(self, localPath: str, remotePath: str=None, progress: typing.Callable[[float], None] | OnProgressDelegate=None) -> None:
		'''Uploads a local file onto the controller. Only jobs (.JBI, .JBR), condition files (.CND) and general data (.DAT) can be uploaded, with the "ftp" or "rcmaster" user. An existing job is not overwritten: delete it first with delete_file().

		:param localPath: Path to the file on the local file system.
		:param remotePath: Name or full path of the file on the controller. If null or empty, the local file name is used.
		:param progress: Reports upload progress as a percentage (0 to 100). -1 indicates indeterminate progress.
		'''
		self._instance.UploadFileFromLocal(localPath, remotePath, (progress._instance if isinstance(progress, OnProgressDelegate) else on_progress_delegate(lambda _x0: progress(_x0))) if progress else None)

	def upload_files_from_local(self, localPaths: typing.List[str], progress: typing.Callable[[float], None] | OnProgressDelegate=None) -> typing.List[str]:
		'''Uploads several local files onto the controller. Each file is uploaded with its local file name. The controller stores each file in the folder of its type (e.g. a ".JBI" file goes to the JOB folder). The upload stops at the first error.

		:param localPaths: Paths to the files on the local file system.
		:param progress: Reports global progress as a percentage (0 to 100).
		:returns: Names of the uploaded files on the controller.
		'''
		return self._instance.UploadFilesFromLocal(localPaths, (progress._instance if isinstance(progress, OnProgressDelegate) else on_progress_delegate(lambda _x0: progress(_x0))) if progress else None)

	def download_file(self, remotePath: str, progress: typing.Callable[[float], None] | OnProgressDelegate=None) -> typing.List[int]:
		'''Downloads a file from the controller and returns its content.

		:param remotePath: Name or full path of the file on the controller (e.g. "TEST.JBI" or "/JOB/TEST.JBI").
		:param progress: Reports download progress as a percentage (0 to 100). -1 indicates indeterminate progress.
		:returns: The content of the file.
		'''
		return self._instance.DownloadFile(remotePath, (progress._instance if isinstance(progress, OnProgressDelegate) else on_progress_delegate(lambda _x0: progress(_x0))) if progress else None)

	def download_file_to_local(self, remotePath: str, localPath: str, progress: typing.Callable[[float], None] | OnProgressDelegate=None) -> None:
		'''Downloads a file from the controller and saves it on the local file system. Overwrites the local file if it already exists. The local file is not created if the download fails.

		:param remotePath: Name or full path of the file on the controller (e.g. "TEST.JBI" or "/JOB/TEST.JBI").
		:param localPath: Path where the file is saved on the local file system.
		:param progress: Reports download progress as a percentage (0 to 100). -1 indicates indeterminate progress.
		'''
		self._instance.DownloadFileToLocal(remotePath, localPath, (progress._instance if isinstance(progress, OnProgressDelegate) else on_progress_delegate(lambda _x0: progress(_x0))) if progress else None)

	def download_files_to_local(self, remotePaths: typing.List[str], localFolder: str, progress: typing.Callable[[float], None] | OnProgressDelegate=None) -> typing.List[str]:
		'''Downloads several files from the controller into a local folder. Each file is saved with its name, and existing local files are overwritten.

		:param remotePaths: Names or full paths of the files on the controller.
		:param localFolder: Local folder where the files are saved. Created if it does not exist.
		:param progress: Reports global progress as a percentage (0 to 100).
		:returns: Local paths of the downloaded files.
		'''
		return self._instance.DownloadFilesToLocal(remotePaths, localFolder, (progress._instance if isinstance(progress, OnProgressDelegate) else on_progress_delegate(lambda _x0: progress(_x0))) if progress else None)

	def file_exists(self, remotePath: str) -> bool:
		'''Checks whether a file exists on the controller.

		:param remotePath: Name or full path of the file on the controller (e.g. "TEST.JBI" or "/JOB/TEST.JBI").
		:returns: true if the file exists.
		'''
		return self._instance.FileExists(remotePath)

	def directory_exists(self, path: str) -> bool:
		'''Checks whether a folder exists on the controller.

		:param path: Full path of the folder (e.g. "/JOB").
		:returns: true if the folder exists.
		'''
		return self._instance.DirectoryExists(path)

	def get_listing(self, path: str) -> typing.List[FtpListItem]:
		'''Returns the files and folders at the specified path on the controller. The root contains one folder per file type (JOB, DAT, CND, SYS, PRM, LST, CSV, LOG, TXT).

		:param path: Full path of the folder to list (e.g. "/JOB"). Use "/" or an empty string for the root.
		:returns: Array of FtpListItem objects describing each entry.
		'''
		return [FtpListItem(x) for x in self._instance.GetListing(path)]

	@property
	def address(self) -> str:
		return self._instance.Address

	@property
	def connected(self) -> bool:
		return self._instance.Connected

	@property
	def user(self) -> str:
		'''FTP user name used for the current connection.'''
		return self._instance.User

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
