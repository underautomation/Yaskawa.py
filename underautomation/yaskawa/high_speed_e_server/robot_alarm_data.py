from __future__ import annotations
import typing
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotAlarmData as robot_alarm_data

class RobotAlarmData(RobotData):
	'''Contains information about a robot alarm retrieved from the controller. Alarms indicate error conditions that may require operator intervention.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_alarm_data()
		else:
			self._instance = _internal

	@property
	def code(self) -> int:
		'''Gets the alarm code identifying the specific alarm type. Alarm codes are documented in the robot's maintenance manual.'''
		return self._instance.Code

	@property
	def data(self) -> int:
		'''Gets additional alarm data providing context about the alarm. The meaning depends on the specific alarm code.'''
		return self._instance.Data

	@property
	def type(self) -> int:
		'''Gets the alarm type/category classification.'''
		return self._instance.Type

	@property
	def occurring_time(self) -> str:
		'''Gets the timestamp when the alarm occurred. Format: "YYYY/MM/DD HH:MM:SS" (16 characters).'''
		return self._instance.OccurringTime

	@property
	def text(self) -> str:
		'''Gets the alarm message text describing the alarm condition. Maximum 32 characters.'''
		return self._instance.Text

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotAlarmData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
