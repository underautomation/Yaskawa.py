from __future__ import annotations
import typing
from UnderAutomation.Yaskawa.Common import ICartesianPosition as i_cartesian_position

class ICartesianPosition:
	'''Represents a robot Cartesian position (TCP position and orientation).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_cartesian_position()
		else:
			self._instance = _internal

	@property
	def x(self) -> float:
		'''X position in millimeters.'''
		return self._instance.X

	@property
	def y(self) -> float:
		'''Y position in millimeters.'''
		return self._instance.Y

	@property
	def z(self) -> float:
		'''Z position in millimeters.'''
		return self._instance.Z

	@property
	def rx(self) -> float:
		'''Rotation around X axis in degrees.'''
		return self._instance.Rx

	@property
	def ry(self) -> float:
		'''Rotation around Y axis in degrees.'''
		return self._instance.Ry

	@property
	def rz(self) -> float:
		'''Rotation around Z axis in degrees.'''
		return self._instance.Rz

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ICartesianPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
