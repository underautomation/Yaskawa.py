import typing
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from UnderAutomation.Yaskawa.HostControl import HostControlGroupData as host_control_group_data

class HostControlGroupData(HostControlResponse):
	'''Contains control group information. Retrieved using the RGROUP command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_group_data()
		else:
			self._instance = _internal

	@property
	def robot_group(self) -> int:
		'''Gets or sets the robot group bits. Each bit represents a robot control group (R1, R2, etc.).'''
		return self._instance.RobotGroup

	@property
	def station_group(self) -> int:
		'''Gets or sets the station group bits. Each bit represents a station control group (S1, S2, etc.).'''
		return self._instance.StationGroup

	@property
	def task(self) -> int:
		'''Gets or sets the current task number. 0: Master task, 1-15: Sub tasks.'''
		return self._instance.Task

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlGroupData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
