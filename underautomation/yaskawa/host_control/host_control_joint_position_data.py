import typing
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from UnderAutomation.Yaskawa.HostControl import HostControlJointPositionData as host_control_joint_position_data

class HostControlJointPositionData(HostControlResponse):
	'''Contains joint position data in pulse (encoder) values. Retrieved using the RPOSJ command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_joint_position_data()
		else:
			self._instance = _internal

	@property
	def s(self) -> int:
		'''Gets or sets the S axis position in pulses.'''
		return self._instance.S

	@property
	def l(self) -> int:
		'''Gets or sets the L axis position in pulses.'''
		return self._instance.L

	@property
	def u(self) -> int:
		'''Gets or sets the U axis position in pulses.'''
		return self._instance.U

	@property
	def r(self) -> int:
		'''Gets or sets the R axis position in pulses.'''
		return self._instance.R

	@property
	def b(self) -> int:
		'''Gets or sets the B axis position in pulses.'''
		return self._instance.B

	@property
	def t(self) -> int:
		'''Gets or sets the T axis position in pulses.'''
		return self._instance.T

	@property
	def e(self) -> int:
		'''Gets or sets the E axis (7th axis) position in pulses.'''
		return self._instance.E

	@property
	def axis8(self) -> int:
		'''Gets or sets the 8th axis position in pulses.'''
		return self._instance.Axis8

	@property
	def axis9(self) -> int:
		'''Gets or sets the 9th axis position in pulses.'''
		return self._instance.Axis9

	@property
	def axis10(self) -> int:
		'''Gets or sets the 10th axis position in pulses.'''
		return self._instance.Axis10

	@property
	def axis11(self) -> int:
		'''Gets or sets the 11th axis position in pulses.'''
		return self._instance.Axis11

	@property
	def axis12(self) -> int:
		'''Gets or sets the 12th axis position in pulses.'''
		return self._instance.Axis12

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlJointPositionData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
