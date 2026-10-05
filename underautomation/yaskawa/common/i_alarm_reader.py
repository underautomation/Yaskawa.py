from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_yaskawa_client import IYaskawaClient
from underautomation.yaskawa.common.i_alarm_entry import IAlarmEntry
from UnderAutomation.Yaskawa.Common import IAlarmReader as i_alarm_reader

class IAlarmReader(IYaskawaClient):
	'''Provides access to active alarm information from the robot controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_alarm_reader()
		else:
			self._instance = _internal

	def get_active_alarms(self) -> typing.List[IAlarmEntry]:
		'''Reads the currently active alarms from the robot controller. Returns an array of active alarm entries. Empty array if no alarms are active.

		:returns: Array of active alarm entries.
		'''
		return [IAlarmEntry(x) for x in self._instance.GetActiveAlarms()]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IAlarmReader):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
