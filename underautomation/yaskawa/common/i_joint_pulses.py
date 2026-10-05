from __future__ import annotations
import typing
from UnderAutomation.Yaskawa.Common import IJointPulses as i_joint_pulses

class IJointPulses:
	'''Represents a robot joint position in pulse (encoder) values.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_joint_pulses()
		else:
			self._instance = _internal

	@property
	def axes(self) -> typing.List[int]:
		'''Axis values in encoder pulses. Typically 8 to 12 elements depending on the robot configuration.'''
		return self._instance.Axes

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IJointPulses):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
