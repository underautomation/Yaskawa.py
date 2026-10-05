from __future__ import annotations
import typing
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from UnderAutomation.Yaskawa.HostControl import HostControlAlarmData as host_control_alarm_data

class HostControlAlarmData(HostControlResponse):
	'''Contains alarm information retrieved from the robot controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_alarm_data()
		else:
			self._instance = _internal

	@property
	def codes(self) -> typing.List[int]:
		'''Gets the codes (5 entries). Index 0 is the code of the active error, indexes 1 to 4 are the codes of the active alarms. A code of 0 means no error or no alarm.'''
		return self._instance.Codes

	@property
	def data(self) -> typing.List[int]:
		'''Gets the sub-codes (5 entries), at the same index as codes. Index 0 is the sub-code of the error, indexes 1 to 4 are the data of the alarms.'''
		return self._instance.Data

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlAlarmData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
