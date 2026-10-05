from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_alarm_entry import IAlarmEntry
from UnderAutomation.Yaskawa.Common import AlarmEntry as alarm_entry

class AlarmEntry(IAlarmEntry):
	'''Default implementation of IAlarmEntry.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = alarm_entry()
		else:
			self._instance = _internal

	@property
	def code(self) -> int:
		return self._instance.Code

	@property
	def sub_code(self) -> int:
		return self._instance.SubCode

	@property
	def message(self) -> str:
		return self._instance.Message

	@property
	def occurring_time(self) -> str:
		return self._instance.OccurringTime

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AlarmEntry):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
