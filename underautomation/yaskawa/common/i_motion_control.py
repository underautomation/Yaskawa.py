from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_yaskawa_client import IYaskawaClient
from UnderAutomation.Yaskawa.Common import IMotionControl as i_motion_control

class IMotionControl(IYaskawaClient):
	'''Provides motion commands to move the robot.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_motion_control()
		else:
			self._instance = _internal

	def move_cartesian(self, x: float, y: float, z: float, rx: float, ry: float, rz: float, speed: float, tool: int=0) -> None:
		'''Moves the robot to a Cartesian position.

		:param x: X position in mm.
		:param y: Y position in mm.
		:param z: Z position in mm.
		:param rx: Rx rotation in degrees.
		:param ry: Ry rotation in degrees.
		:param rz: Rz rotation in degrees.
		:param speed: Speed value (interpretation depends on protocol defaults).
		:param tool: Tool number (0-63).
		'''
		self._instance.MoveCartesian(x, y, z, rx, ry, rz, speed, tool)

	def move_joints(self, axesPulse: typing.List[int], speed: float, tool: int=0) -> None:
		'''Moves the robot to a joint (pulse) position.

		:param axesPulse: Target axis positions in encoder pulses.
		:param speed: Speed value (interpretation depends on protocol defaults).
		:param tool: Tool number (0-63).
		'''
		self._instance.MoveJoints(axesPulse, speed, tool)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IMotionControl):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
