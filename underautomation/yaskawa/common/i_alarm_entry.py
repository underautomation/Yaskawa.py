from __future__ import annotations
import typing
from UnderAutomation.Yaskawa.Common import IAlarmEntry as i_alarm_entry

class IAlarmEntry:
	'''Represents an active alarm on a Yaskawa robot controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_alarm_entry()
		else:
			self._instance = _internal

	@property
	def code(self) -> int:
		'''Alarm code identifying the alarm type.'''
		return self._instance.Code

	@property
	def sub_code(self) -> int:
		'''Alarm sub-code providing additional context.'''
		return self._instance.SubCode

	@property
	def message(self) -> str:
		'''Human-readable alarm message text.'''
		return self._instance.Message

	@property
	def occurring_time(self) -> str:
		'''Timestamp of alarm occurrence (format depends on protocol).'''
		return self._instance.OccurringTime

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IAlarmEntry):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
