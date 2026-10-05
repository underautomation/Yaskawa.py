from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_yaskawa_client import IYaskawaClient
from underautomation.yaskawa.common.i_joint_pulses import IJointPulses
from underautomation.yaskawa.common.i_cartesian_position import ICartesianPosition
from UnderAutomation.Yaskawa.Common import IPositionReader as i_position_reader

class IPositionReader(IYaskawaClient):
	'''Provides access to current robot position readings.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_position_reader()
		else:
			self._instance = _internal

	def get_robot_joint_position(self) -> IJointPulses:
		'''Reads the current robot joint position in pulse (encoder) values.

		:returns: Joint position data with axis values in encoder pulses.
		'''
		return IJointPulses(self._instance.GetRobotJointPosition())

	def get_robot_cartesian_position(self) -> ICartesianPosition:
		'''Reads the current robot Cartesian position (TCP position and orientation).

		:returns: Cartesian position data with coordinates in mm and degrees.
		'''
		return ICartesianPosition(self._instance.GetRobotCartesianPosition())

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IPositionReader):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
