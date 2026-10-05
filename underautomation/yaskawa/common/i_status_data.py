from __future__ import annotations
import typing
from UnderAutomation.Yaskawa.Common import IStatusData as i_status_data

class IStatusData:
	'''Represents the operational status of a Yaskawa robot controller. Common status flags shared across all communication protocols.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_status_data()
		else:
			self._instance = _internal

	@property
	def step(self) -> bool:
		'''Step execution mode active.'''
		return self._instance.Step

	@property
	def cycle(self) -> bool:
		'''Cycle execution mode active.'''
		return self._instance.Cycle

	@property
	def automatic(self) -> bool:
		'''Automatic operation mode active.'''
		return self._instance.Automatic

	@property
	def running(self) -> bool:
		'''Currently executing a job.'''
		return self._instance.Running

	@property
	def teach(self) -> bool:
		'''Manual teach mode active.'''
		return self._instance.Teach

	@property
	def play(self) -> bool:
		'''Program playback mode active.'''
		return self._instance.Play

	@property
	def command_remote(self) -> bool:
		'''Remote command mode enabled.'''
		return self._instance.CommandRemote

	@property
	def servo_on(self) -> bool:
		'''Servo power is on.'''
		return self._instance.ServoOn

	@property
	def error_occurring(self) -> bool:
		'''An error condition is occurring.'''
		return self._instance.ErrorOccurring

	@property
	def alarming(self) -> bool:
		'''An alarm is active.'''
		return self._instance.Alarming

	@property
	def in_hold_status_by_command(self) -> bool:
		'''Hold state triggered by software command.'''
		return self._instance.InHoldStatusByCommand

	@property
	def in_hold_status_externally(self) -> bool:
		'''Hold state triggered by external signal.'''
		return self._instance.InHoldStatusExternally

	@property
	def in_hold_status_pendant(self) -> bool:
		'''Hold state triggered by teach pendant.'''
		return self._instance.InHoldStatusPendant

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IStatusData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
