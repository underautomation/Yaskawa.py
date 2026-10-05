from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_yaskawa_client import IYaskawaClient
from UnderAutomation.Yaskawa.Common import ITorqueReader as i_torque_reader

class ITorqueReader(IYaskawaClient):
	'''Provides access to robot axis torque readings.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_torque_reader()
		else:
			self._instance = _internal

	def get_torque(self) -> typing.List[float]:
		'''Reads the current torque values of all robot axes as a percentage of the maximum rated torque.

		:returns: Array of torque values as percentages (double). Array length depends on the protocol and robot configuration.
		'''
		return self._instance.GetTorque()

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ITorqueReader):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
