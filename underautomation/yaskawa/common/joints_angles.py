from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_joint_angles import IJointAngles
from UnderAutomation.Yaskawa.Common import JointsAngles as joints_angles

class JointsAngles(IJointAngles):
	'''Joint angles of a 6-axis arm, in degrees, with the same signs as the pendant (axes S, L, U, R, B, T).'''
	def __init__(self, s: float, l: float, u: float, r: float, b: float, t: float, _internal = 0):
		'''Initializes a new instance of JointsAngles with the specified angles (degrees).

		:param s: S axis angle.
		:param l: L axis angle.
		:param u: U axis angle.
		:param r: R axis angle.
		:param b: B axis angle.
		:param t: T axis angle.
		'''
		if(_internal == 0):
			self._instance = joints_angles(s, l, u, r, b, t)
		else:
			self._instance = _internal

	@property
	def values(self) -> typing.List[float]:
		'''Angles of axes S, L, U, R, B, T in degrees.'''
		return self._instance.Values

	@property
	def s(self) -> float:
		'''S axis angle (degrees).'''
		return self._instance.S

	@s.setter
	def s(self, value: float):
		self._instance.S = value

	@property
	def l(self) -> float:
		'''L axis angle (degrees).'''
		return self._instance.L

	@l.setter
	def l(self, value: float):
		self._instance.L = value

	@property
	def u(self) -> float:
		'''U axis angle (degrees).'''
		return self._instance.U

	@u.setter
	def u(self, value: float):
		self._instance.U = value

	@property
	def r(self) -> float:
		'''R axis angle (degrees).'''
		return self._instance.R

	@r.setter
	def r(self, value: float):
		self._instance.R = value

	@property
	def b(self) -> float:
		'''B axis angle (degrees).'''
		return self._instance.B

	@b.setter
	def b(self, value: float):
		self._instance.B = value

	@property
	def t(self) -> float:
		'''T axis angle (degrees).'''
		return self._instance.T

	@t.setter
	def t(self, value: float):
		self._instance.T = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointsAngles):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
