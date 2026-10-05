from __future__ import annotations
import typing
from UnderAutomation.Yaskawa.Common import IJointAngles as i_joint_angles

class IJointAngles:
	'''Represents a joint position of a 6-axis arm in degrees, with the same signs as the pendant.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_joint_angles()
		else:
			self._instance = _internal

	@property
	def values(self) -> typing.List[float]:
		'''Angles of axes S, L, U, R, B, T in degrees.'''
		return self._instance.Values

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IJointAngles):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
