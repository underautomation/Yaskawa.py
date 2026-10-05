from __future__ import annotations
import typing
from underautomation.yaskawa.host_control.host_control_alarm_entry import HostControlAlarmEntry
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from UnderAutomation.Yaskawa.HostControl import HostControlAlarmStringData as host_control_alarm_string_data

class HostControlAlarmStringData(HostControlResponse):
	'''Contains alarm information with text messages retrieved from the robot controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_alarm_string_data()
		else:
			self._instance = _internal

	@property
	def alarm_count(self) -> int:
		'''Gets the number of active alarms (entries of alarms with a code other than 0).'''
		return self._instance.AlarmCount

	@property
	def error(self) -> HostControlAlarmEntry:
		'''Gets the active error. Its code is 0 when no error is active.'''
		return HostControlAlarmEntry(self._instance.Error)

	@property
	def alarms(self) -> typing.List[HostControlAlarmEntry]:
		'''Gets the alarm entries with codes and text messages (always 4 entries, the code of an unused entry is 0).'''
		return [HostControlAlarmEntry(x) for x in self._instance.Alarms]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlAlarmStringData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
