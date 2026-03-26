import typing
from __future__ import annotation
from underautomation.yaskawa.high_speed_e_server.robot_alarm_data import RobotAlarmData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotAlarmDataExtended as robot_alarm_data_extended

class RobotAlarmDataExtended(RobotAlarmData):
	'''Contains extended information about a robot alarm, including sub-code details. Provides more detailed diagnostic information than the basic RobotAlarmData.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_alarm_data_extended()
		else:
			self._instance = _internal

	@property
	def additionnal_information(self) -> str:
		'''Gets additional information about the alarm condition. Maximum 16 characters.'''
		return self._instance.AdditionnalInformation

	@property
	def sub_data(self) -> str:
		'''Gets the sub-code data providing detailed error context. Maximum 96 characters.'''
		return self._instance.SubData

	@property
	def sub_data_reverse(self) -> str:
		'''Gets the reversed sub-code data. Maximum 96 characters.'''
		return self._instance.SubDataReverse

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotAlarmDataExtended):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
