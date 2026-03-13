import typing
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from UnderAutomation.Yaskawa.HostControl import HostControlCartesianPositionData as host_control_cartesian_position_data

class HostControlCartesianPositionData(HostControlResponse):
	'''Contains Cartesian position data (TCP position and orientation). Retrieved using the RPOSC command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_cartesian_position_data()
		else:
			self._instance = _internal

	@property
	def x(self) -> float:
		'''Gets or sets the X position in millimeters.'''
		return self._instance.X

	@property
	def y(self) -> float:
		'''Gets or sets the Y position in millimeters.'''
		return self._instance.Y

	@property
	def z(self) -> float:
		'''Gets or sets the Z position in millimeters.'''
		return self._instance.Z

	@property
	def rx(self) -> float:
		'''Gets or sets the Rx (rotation around X axis) in degrees.'''
		return self._instance.Rx

	@property
	def ry(self) -> float:
		'''Gets or sets the Ry (rotation around Y axis) in degrees.'''
		return self._instance.Ry

	@property
	def rz(self) -> float:
		'''Gets or sets the Rz (rotation around Z axis) in degrees.'''
		return self._instance.Rz

	@property
	def re(self) -> float:
		'''Gets or sets the Re (7th axis rotation) in degrees or millimeters.'''
		return self._instance.Re

	@property
	def axis8(self) -> float:
		'''Gets or sets the 8th external axis value.'''
		return self._instance.Axis8

	@property
	def axis9(self) -> float:
		'''Gets or sets the 9th external axis value.'''
		return self._instance.Axis9

	@property
	def axis10(self) -> float:
		'''Gets or sets the 10th external axis value.'''
		return self._instance.Axis10

	@property
	def axis11(self) -> float:
		'''Gets or sets the 11th external axis value.'''
		return self._instance.Axis11

	@property
	def axis12(self) -> float:
		'''Gets or sets the 12th external axis value.'''
		return self._instance.Axis12

	@property
	def type(self) -> int:
		'''Gets or sets the robot posture/configuration type. Defines arm configuration (flip, upper/lower arm, front/back, etc.).'''
		return self._instance.Type

	@property
	def coordinate_system(self) -> int:
		'''Gets or sets the coordinate system index. 0: Base, 1-65: User coordinates.'''
		return self._instance.CoordinateSystem

	@property
	def is_flip(self) -> bool:
		'''Gets whether the robot is in flip configuration.'''
		return self._instance.IsFlip

	@property
	def is_upper_arm(self) -> bool:
		'''Gets whether the robot is in upper arm configuration.'''
		return self._instance.IsUpperArm

	@property
	def is_front(self) -> bool:
		'''Gets whether the robot is in front configuration.'''
		return self._instance.IsFront

	@property
	def is_r_less_than180(self) -> bool:
		'''Gets whether R axis is less than 180 degrees.'''
		return self._instance.IsRLessThan180

	@property
	def is_t_less_than180(self) -> bool:
		'''Gets whether T axis is less than 180 degrees.'''
		return self._instance.IsTLessThan180

	@property
	def is_s_less_than180(self) -> bool:
		'''Gets whether S axis is less than 180 degrees.'''
		return self._instance.IsSLessThan180

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlCartesianPositionData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
