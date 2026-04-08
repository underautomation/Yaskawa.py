from __future__ import annotations
import typing
from underautomation.yaskawa.high_speed_e_server.control_group import ControlGroup
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotControlGroup as robot_control_group
from UnderAutomation.Yaskawa.HighSpeedEServer import ControlGroup as control_group

class RobotControlGroup:
	'''Represents a robot control group combining a group type with an index. Used to specify which robot or station to query in multi-robot systems.'''
	def __init__(self, group: ControlGroup, index: int, _internal = 0):
		'''Creates a new RobotControlGroup with the specified group type and index.

		:param group: The control group type.
		:param index: The index within the group (1-based).
		'''
		if(_internal == 0):
			self._instance = robot_control_group(group, index)
		else:
			self._instance = _internal

	@property
	def group(self) -> ControlGroup:
		'''The control group type (robot, base, station).'''
		return ControlGroup(int(self._instance.Group))

	@property
	def index(self) -> int:
		'''The index within the control group (e.g., robot number 1-8).'''
		return self._instance.Index

	@property
	def byte_value(self) -> int:
		'''The combined byte value sent to the robot controller (Group + Index).'''
		return self._instance.ByteValue

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotControlGroup):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default control group for Cartesian position of robot 1.
RobotControlGroup.DefaultRobotCartesian = RobotControlGroup(None, None, robot_control_group.DefaultRobotCartesian)

# Default control group for pulse position of robot 1.
RobotControlGroup.DefaultRobotPulse = RobotControlGroup(None, None, robot_control_group.DefaultRobotPulse)
