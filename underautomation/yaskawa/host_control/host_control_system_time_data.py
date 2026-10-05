from __future__ import annotations
import typing
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from UnderAutomation.Yaskawa.HostControl import HostControlSystemTimeData as host_control_system_time_data

class HostControlSystemTimeData(HostControlResponse):
	'''Contains system time information from the robot controller. Retrieved using the RSYSTM command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_system_time_data()
		else:
			self._instance = _internal

	@property
	def year(self) -> str:
		'''Gets the year.'''
		return self._instance.Year

	@property
	def month_day(self) -> str:
		'''Gets the month and day (MM/DD format).'''
		return self._instance.MonthDay

	@property
	def hour_minute(self) -> str:
		'''Gets the hour and minute (HH:MM format).'''
		return self._instance.HourMinute

	@property
	def second(self) -> str:
		'''Gets the second.'''
		return self._instance.Second

	@property
	def day_of_week(self) -> str:
		'''Gets the day of the week.'''
		return self._instance.DayOfWeek

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlSystemTimeData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
