from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_dh_parameters import IDhParameters
from UnderAutomation.Yaskawa.Kinematics.Internal import ArmModelAttribute as arm_model_attribute

class ArmModelAttribute(IDhParameters):
	'''Attribute that associates DH parameters with an arm kinematic model enum value.'''
	def __init__(self, description: str, a1: float, a2: float, a3: float, d4: float, d5: float, d6: float, theta2: float, theta3: float, theta5: float, _internal = 0):
		'''Initializes a new instance of ArmModelAttribute with the specified description and DH parameters.

		:param description: The robot model name.
		:param a1: Offset between the S axis and the L axis (mm).
		:param a2: Lower arm length (mm).
		:param a3: Elbow offset (mm).
		:param d4: Forearm length (mm).
		:param d5: Wrist offset along the B axis (mm).
		:param d6: Distance between the wrist and the flange (mm).
		:param theta2: DH angle of the L axis at zero pulse (degrees).
		:param theta3: DH angle of the U axis at zero pulse (degrees).
		:param theta5: DH angle of the B axis at zero pulse (degrees).
		'''
		if(_internal == 0):
			self._instance = arm_model_attribute(description, a1, a2, a3, d4, d5, d6, theta2, theta3, theta5)
		else:
			self._instance = _internal

	@property
	def a1(self) -> float:
		return self._instance.A1

	@property
	def a2(self) -> float:
		return self._instance.A2

	@property
	def a3(self) -> float:
		return self._instance.A3

	@property
	def d4(self) -> float:
		return self._instance.D4

	@property
	def d5(self) -> float:
		return self._instance.D5

	@property
	def d6(self) -> float:
		return self._instance.D6

	@property
	def theta2(self) -> float:
		return self._instance.Theta2

	@property
	def theta3(self) -> float:
		return self._instance.Theta3

	@property
	def theta5(self) -> float:
		return self._instance.Theta5

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ArmModelAttribute):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
