import typing
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from UnderAutomation.Yaskawa.HostControl import HostControlJobData as host_control_job_data

class HostControlJobData(HostControlResponse):
	'''Contains information about the currently executing job (program). Retrieved using the RJSEQ command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_job_data()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Gets or sets the name of the currently executing job.'''
		return self._instance.Name

	@property
	def line(self) -> int:
		'''Gets or sets the current line number within the job (0-9999).'''
		return self._instance.Line

	@property
	def step(self) -> int:
		'''Gets or sets the current step number within the job (1-9998).'''
		return self._instance.Step

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlJobData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
