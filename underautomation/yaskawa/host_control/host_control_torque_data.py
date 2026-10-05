from __future__ import annotations
import typing
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from UnderAutomation.Yaskawa.HostControl import HostControlTorqueData as host_control_torque_data

class HostControlTorqueData(HostControlResponse):
	'''Contains torque values for each robot axis. Retrieved using the RTRQ (current torque) or RMAXTRQ (maximum torque) commands.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_torque_data()
		else:
			self._instance = _internal

	@property
	def values(self) -> typing.List[float]:
		'''Gets the torque values for each axis (up to 12 axes). Values are in percentage of maximum rated torque.'''
		return self._instance.Values

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlTorqueData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
