from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_yaskawa_client import IYaskawaClient
from underautomation.yaskawa.common.i_status_data import IStatusData
from underautomation.yaskawa.common.i_job_data import IJobData
from UnderAutomation.Yaskawa.Common import IStatusReader as i_status_reader

class IStatusReader(IYaskawaClient):
	'''Provides access to robot status and executing job information.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_status_reader()
		else:
			self._instance = _internal

	def get_status_information(self) -> IStatusData:
		'''Reads the current operational status of the robot controller.

		:returns: Status data containing boolean flags for various robot states.
		'''
		return IStatusData(self._instance.GetStatusInformation())

	def get_executing_job_information(self) -> IJobData:
		'''Reads the currently executing job information.

		:returns: Job data containing name, line number, and step.
		'''
		return IJobData(self._instance.GetExecutingJobInformation())

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IStatusReader):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
