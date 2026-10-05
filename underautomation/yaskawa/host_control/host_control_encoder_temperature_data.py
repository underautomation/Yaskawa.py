from __future__ import annotations
import typing
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from UnderAutomation.Yaskawa.HostControl import HostControlEncoderTemperatureData as host_control_encoder_temperature_data

class HostControlEncoderTemperatureData(HostControlResponse):
	'''Contains encoder temperature values for each robot axis. Retrieved using the RENCTMP command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_encoder_temperature_data()
		else:
			self._instance = _internal

	@property
	def values(self) -> typing.List[float]:
		'''Gets the temperature values for each axis encoder (up to 12 axes). Values are in degrees Celsius.'''
		return self._instance.Values

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlEncoderTemperatureData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
