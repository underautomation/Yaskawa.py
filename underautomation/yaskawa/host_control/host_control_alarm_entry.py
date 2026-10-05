from __future__ import annotations
import typing
from UnderAutomation.Yaskawa.HostControl import HostControlAlarmEntry as host_control_alarm_entry

class HostControlAlarmEntry:
	'''Represents a single alarm entry with code, sub-code and text description.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_alarm_entry()
		else:
			self._instance = _internal

	@property
	def code(self) -> int:
		'''Gets the alarm code number.'''
		return self._instance.Code

	@property
	def sub_code(self) -> int:
		'''Gets the alarm sub-code (data).'''
		return self._instance.SubCode

	@property
	def message(self) -> str:
		'''Gets the alarm text message.'''
		return self._instance.Message

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlAlarmEntry):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
