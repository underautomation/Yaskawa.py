from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_yaskawa_client import IYaskawaClient
from underautomation.yaskawa.common.robot_cycle_type import RobotCycleType
from UnderAutomation.Yaskawa.Common import IRobotControl as i_robot_control
from UnderAutomation.Yaskawa.Common import RobotCycleType as robot_cycle_type

class IRobotControl(IYaskawaClient):
	'''Provides robot control commands: alarm reset, servo, hold, cycle, job and display.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_robot_control()
		else:
			self._instance = _internal

	def alarm_reset(self) -> None:
		'''Resets the current alarm condition.'''
		self._instance.AlarmReset()

	def set_servo(self, enable: bool) -> None:
		'''Enables or disables servo power. Servo must be ON for the robot to move.

		:param enable: True to enable servo power, false to disable.
		'''
		self._instance.SetServo(enable)

	def set_hold(self, enable: bool) -> None:
		'''Sets the hold state of the robot. When hold is ON, robot motion is paused.

		:param enable: True to hold (pause), false to release hold.
		'''
		self._instance.SetHold(enable)

	def set_teach_pendant_lock_state(self, locked: bool) -> None:
		'''Locks or unlocks the teach pendant.

		:param locked: True to lock the teach pendant, false to unlock.
		'''
		self._instance.SetTeachPendantLockState(locked)

	def set_cycle(self, cycle: RobotCycleType) -> None:
		'''Sets the execution cycle type (Step, One Cycle, or Automatic).

		:param cycle: The target cycle type.
		'''
		self._instance.SetCycle(robot_cycle_type(int(cycle)))

	def start_job(self) -> None:
		'''Starts execution of the currently selected job.'''
		self._instance.StartJob()

	def select_job(self, jobName: str, line: int) -> None:
		'''Selects a job for execution and positions to a specific line.

		:param jobName: Job name to select.
		:param line: Line number to position to.
		'''
		self._instance.SelectJob(jobName, line)

	def display(self, message: str) -> None:
		'''Displays a popup message on the robot programming pendant.

		:param message: The message to display.
		'''
		self._instance.Display(message)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IRobotControl):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
