from __future__ import annotations
import typing
from UnderAutomation.Yaskawa.Common import IDhParameters as i_dh_parameters

class IDhParameters:
	'''Denavit-Hartenberg parameters of a 6-axis Yaskawa arm (axes S, L, U, R, B, T).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_dh_parameters()
		else:
			self._instance = _internal

	@property
	def a1(self) -> float:
		'''Offset between the S axis and the L axis, along the arm (mm).'''
		return self._instance.A1

	@property
	def a2(self) -> float:
		'''Lower arm length, between the L axis and the U axis (mm).'''
		return self._instance.A2

	@property
	def a3(self) -> float:
		'''Elbow offset, between the U axis and the forearm axis (mm).'''
		return self._instance.A3

	@property
	def d4(self) -> float:
		'''Forearm length, between the U axis and the wrist (mm).'''
		return self._instance.D4

	@property
	def d5(self) -> float:
		'''Wrist offset along the B axis (mm). Zero for a spherical wrist.'''
		return self._instance.D5

	@property
	def d6(self) -> float:
		'''Distance between the wrist and the flange, along the T axis (mm).'''
		return self._instance.D6

	@property
	def theta2(self) -> float:
		'''DH angle of the L axis when the L axis is at zero pulse (degrees).'''
		return self._instance.Theta2

	@property
	def theta3(self) -> float:
		'''DH angle of the U axis when the U axis is at zero pulse (degrees).'''
		return self._instance.Theta3

	@property
	def theta5(self) -> float:
		'''DH angle of the B axis when the B axis is at zero pulse (degrees).'''
		return self._instance.Theta5

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IDhParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
