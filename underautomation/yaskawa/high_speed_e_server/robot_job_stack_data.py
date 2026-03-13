import typing
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotJobStackData as robot_job_stack_data

class RobotJobStackData(RobotData):
	'''Contains the job call stack for a specific task on the robot controller. Represents the current nesting of CALL instructions, from the outermost job to the currently executing one. Only supported on DX200 (AY/BY/YN) controllers.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_job_stack_data()
		else:
			self._instance = _internal

	@property
	def jobs(self) -> typing.List[str]:
		'''Gets the job names in the call stack, outermost first. The first entry is the root job, the last entry is the currently executing job. Empty if no nested calls are active.'''
		return self._instance.Jobs

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotJobStackData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
