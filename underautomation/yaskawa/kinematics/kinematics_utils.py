from __future__ import annotations
import typing
from underautomation.yaskawa.common.cartesian_position import CartesianPosition
from underautomation.yaskawa.common.i_joint_angles import IJointAngles
from underautomation.yaskawa.common.i_dh_parameters import IDhParameters
from underautomation.yaskawa.common.joints_angles import JointsAngles
from underautomation.yaskawa.common.i_cartesian_position import ICartesianPosition
from UnderAutomation.Yaskawa.Kinematics import KinematicsUtils as kinematics_utils

class KinematicsUtils:
	'''Forward and inverse kinematics of 6-axis Yaskawa arms.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = kinematics_utils()
		else:
			self._instance = _internal

	@staticmethod
	def forward_kinematics(joints: IJointAngles, parameters: IDhParameters) -> CartesianPosition:
		'''Computes the flange position for the given joint angles.

		:param joints: Joint angles in degrees (S, L, U, R, B, T), pendant signs.
		:param parameters: DH parameters of the robot.
		:returns: Flange position in the robot frame.
		'''
		return CartesianPosition(None, None, None, None, None, None, kinematics_utils.ForwardKinematics(joints._instance if joints else None, parameters._instance if parameters else None))

	@staticmethod
	def inverse_kinematics(position: ICartesianPosition, parameters: IDhParameters) -> typing.List[JointsAngles]:
		'''Computes all the joint solutions that put the flange at the given position. Joint limits are not checked. Angles are returned in the range (-180, 180].

		:param position: Flange position in the robot frame, for example a position read from the robot.
		:param parameters: DH parameters of the robot.
		:returns: All solutions found. Empty if the position cannot be reached.
		'''
		return [JointsAngles(None, None, None, None, None, None, x) for x in kinematics_utils.InverseKinematics(position._instance if position else None, parameters._instance if parameters else None)]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, KinematicsUtils):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
