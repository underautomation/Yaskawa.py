import typing
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotManagementTimeData as robot_management_time_data

class RobotManagementTimeData(RobotData):
	'''Contains management time information for tracking robot operation statistics. Provides uptime and usage metrics for maintenance planning and reporting.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_management_time_data()
		else:
			self._instance = _internal

	@property
	def start_time(self) -> str:
		'''Gets the start time of the tracked period. Format: "YYYY/MM/DD HH:MM" (16 characters).'''
		return self._instance.StartTime

	@property
	def ellapse_time(self) -> str:
		'''Gets the elapsed time for the tracked metric. Format: "HHHH:MM:SS.ss" or similar time duration format (12 characters).'''
		return self._instance.EllapseTime

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotManagementTimeData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
