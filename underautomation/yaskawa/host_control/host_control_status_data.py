import typing
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from UnderAutomation.Yaskawa.HostControl import HostControlStatusData as host_control_status_data

class HostControlStatusData(HostControlResponse):
	'''Contains the current operational status of the robot controller. Provides information about the robot's mode, running state, and safety conditions. Retrieved using the RSTATS command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_status_data()
		else:
			self._instance = _internal

	@property
	def step(self) -> bool:
		'''Gets whether the robot is in step (single-step) execution mode. When true, the robot executes one instruction at a time.'''
		return self._instance.Step

	@property
	def cycle(self) -> bool:
		'''Gets whether the robot is in cycle execution mode. When true, the robot executes one complete cycle then stops.'''
		return self._instance.Cycle

	@property
	def automatic(self) -> bool:
		'''Gets whether the robot is in automatic operation mode. When true, the robot can operate automatically without pendant interaction.'''
		return self._instance.Automatic

	@property
	def running(self) -> bool:
		'''Gets whether the robot is currently running (executing a job).'''
		return self._instance.Running

	@property
	def speed_limit(self) -> bool:
		'''Gets whether speed limit is active.'''
		return self._instance.SpeedLimit

	@property
	def teach(self) -> bool:
		'''Gets whether the robot is in teach mode. In teach mode, the robot can be manually positioned and jobs can be edited.'''
		return self._instance.Teach

	@property
	def play(self) -> bool:
		'''Gets whether the robot is in play mode. In play mode, the robot can execute programmed jobs.'''
		return self._instance.Play

	@property
	def command_remote(self) -> bool:
		'''Gets whether remote command mode is enabled. When true, the robot accepts commands from external sources (including this API).'''
		return self._instance.CommandRemote

	@property
	def servo_on(self) -> bool:
		'''Gets whether servo power is enabled. Servo must be ON for the robot to move.'''
		return self._instance.ServoOn

	@property
	def error_occurring(self) -> bool:
		'''Gets whether an error condition is occurring. Errors may prevent normal operation until resolved.'''
		return self._instance.ErrorOccurring

	@property
	def alarming(self) -> bool:
		'''Gets whether an alarm is currently active. Check GetAlarm() for detailed alarm information.'''
		return self._instance.Alarming

	@property
	def in_hold_status_by_command(self) -> bool:
		'''Gets whether the robot is held by a command (software hold). A hold command was issued via the API or job instruction.'''
		return self._instance.InHoldStatusByCommand

	@property
	def in_hold_status_externally(self) -> bool:
		'''Gets whether the robot is held by an external hold signal. External safety circuit has triggered a hold condition.'''
		return self._instance.InHoldStatusExternally

	@property
	def in_hold_status_pendant(self) -> bool:
		'''Gets whether the robot is held by the programming pendant. Operator has pressed hold on the pendant.'''
		return self._instance.InHoldStatusPendant

	@property
	def raw_data1(self) -> int:
		'''Gets the raw value of data 1 (mode/cycle/operation bits).'''
		return self._instance.RawData1

	@property
	def raw_data2(self) -> int:
		'''Gets the raw value of data 2 (hold/alarm/servo bits).'''
		return self._instance.RawData2

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlStatusData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
