from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_cartesian_position import ICartesianPosition
from UnderAutomation.Yaskawa.Common import CartesianPosition as cartesian_position

class CartesianPosition(ICartesianPosition):
	'''Cartesian position of the robot flange in the robot frame.'''
	def __init__(self, x: float, y: float, z: float, rx: float, ry: float, rz: float, _internal = 0):
		'''Initializes a new instance of CartesianPosition with the specified values.

		:param x: X position (mm).
		:param y: Y position (mm).
		:param z: Z position (mm).
		:param rx: Rotation around the X axis (degrees).
		:param ry: Rotation around the Y axis (degrees).
		:param rz: Rotation around the Z axis (degrees).
		'''
		if(_internal == 0):
			self._instance = cartesian_position(x, y, z, rx, ry, rz)
		else:
			self._instance = _internal

	def to_homogeneous_matrix(self) -> typing.List[float]:
		'''Returns the 4x4 homogeneous matrix of this position (rotation and translation in mm).

		:returns: A 4x4 matrix.
		'''
		return self._instance.ToHomogeneousMatrix()

	@staticmethod
	def from_homogeneous_matrix(matrix: typing.List[float]) -> 'CartesianPosition':
		return CartesianPosition(None, None, None, None, None, None, cartesian_position.FromHomogeneousMatrix(matrix))

	@property
	def x(self) -> float:
		'''X position in millimeters.'''
		return self._instance.X

	@x.setter
	def x(self, value: float):
		self._instance.X = value

	@property
	def y(self) -> float:
		'''Y position in millimeters.'''
		return self._instance.Y

	@y.setter
	def y(self, value: float):
		self._instance.Y = value

	@property
	def z(self) -> float:
		'''Z position in millimeters.'''
		return self._instance.Z

	@z.setter
	def z(self, value: float):
		self._instance.Z = value

	@property
	def rx(self) -> float:
		'''Rotation around the X axis in degrees.'''
		return self._instance.Rx

	@rx.setter
	def rx(self, value: float):
		self._instance.Rx = value

	@property
	def ry(self) -> float:
		'''Rotation around the Y axis in degrees.'''
		return self._instance.Ry

	@ry.setter
	def ry(self, value: float):
		self._instance.Ry = value

	@property
	def rz(self) -> float:
		'''Rotation around the Z axis in degrees.'''
		return self._instance.Rz

	@rz.setter
	def rz(self, value: float):
		self._instance.Rz = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CartesianPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
