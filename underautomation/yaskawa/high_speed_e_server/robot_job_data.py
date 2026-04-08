from __future__ import annotations
import typing
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotJobData as robot_job_data

class RobotJobData(RobotData):
	'''Contains information about the currently executing job (program) on the robot controller. Retrieved using the executing job information reading command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_job_data()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Gets the name of the currently selected/executing job. Job names can be up to 32 characters. Returns empty string if no job is selected.'''
		return self._instance.Name

	@property
	def line(self) -> int:
		'''Gets the current line number being executed within the job. Line numbers are 1-based and correspond to the job listing.'''
		return self._instance.Line

	@property
	def step(self) -> int:
		'''Gets the current step number within the job. Step numbers track the execution progress through motion instructions.'''
		return self._instance.Step

	@property
	def speed_override(self) -> float:
		'''Gets the current speed override percentage (0-100). This is the global speed multiplier applied to all motions.'''
		return self._instance.SpeedOverride

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotJobData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
