from __future__ import annotations
import typing
from UnderAutomation.Yaskawa.Common import IJobData as i_job_data

class IJobData:
	'''Represents information about the currently executing job on a Yaskawa robot controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_job_data()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the current job.'''
		return self._instance.Name

	@property
	def line(self) -> int:
		'''Current line number being executed.'''
		return self._instance.Line

	@property
	def step(self) -> int:
		'''Current step number being executed.'''
		return self._instance.Step

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IJobData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
