from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_status_reader import IStatusReader
from underautomation.yaskawa.common.i_yaskawa_client import IYaskawaClient
from underautomation.yaskawa.common.i_position_reader import IPositionReader
from underautomation.yaskawa.common.i_alarm_reader import IAlarmReader
from underautomation.yaskawa.common.i_robot_control import IRobotControl
from underautomation.yaskawa.common.iio_access import IIOAccess
from underautomation.yaskawa.common.i_variable_access import IVariableAccess
from underautomation.yaskawa.common.i_torque_reader import ITorqueReader
from underautomation.yaskawa.common.i_motion_control import IMotionControl
from UnderAutomation.Yaskawa.Common import IRobotClient as i_robot_client

class IRobotClient(IStatusReader, IPositionReader, IAlarmReader, IRobotControl, IIOAccess, IVariableAccess, ITorqueReader, IMotionControl):
	'''Super-interface that combines all robot control capabilities. Implemented by High Speed Ethernet Server and Host Control clients.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_robot_client()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IRobotClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
