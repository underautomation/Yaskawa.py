import typing
from underautomation.yaskawa.high_speed_e_server.robot_data import RobotData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotAxisRawData as robot_axis_raw_data_1

T = typing.TypeVar('T')
class RobotAxisRawData1(RobotData, typing.Generic[T]):
	'''Represents raw axis data with generic value type for up to 8 axes. This is the base class for position-related data structures.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_axis_raw_data_1()
		else:
			self._instance = _internal

	@property
	def axes(self) -> typing.List[T]:
		'''Gets the array containing all axis values. Index 0-5 typically represent robot axes (S, L, U, R, B, T). Index 6-7 may be used for additional axes if available.'''
		return list(self._instance.Axes)

	@property
	def axis1(self) -> T:
		'''Gets or sets the value for axis 1 (typically S-axis / base rotation).'''
		return self._instance.Axis1

	@axis1.setter
	def axis1(self, value: T):
		self._instance.Axis1 = value

	@property
	def axis2(self) -> T:
		'''Gets or sets the value for axis 2 (typically L-axis / lower arm).'''
		return self._instance.Axis2

	@axis2.setter
	def axis2(self, value: T):
		self._instance.Axis2 = value

	@property
	def axis3(self) -> T:
		'''Gets or sets the value for axis 3 (typically U-axis / upper arm).'''
		return self._instance.Axis3

	@axis3.setter
	def axis3(self, value: T):
		self._instance.Axis3 = value

	@property
	def axis4(self) -> T:
		'''Gets or sets the value for axis 4 (typically R-axis / wrist rotation).'''
		return self._instance.Axis4

	@axis4.setter
	def axis4(self, value: T):
		self._instance.Axis4 = value

	@property
	def axis5(self) -> T:
		'''Gets or sets the value for axis 5 (typically B-axis / wrist bend).'''
		return self._instance.Axis5

	@axis5.setter
	def axis5(self, value: T):
		self._instance.Axis5 = value

	@property
	def axis6(self) -> T:
		'''Gets or sets the value for axis 6 (typically T-axis / tool rotation).'''
		return self._instance.Axis6

	@axis6.setter
	def axis6(self, value: T):
		self._instance.Axis6 = value

	@property
	def axis7(self) -> T:
		'''Gets or sets the value for axis 7 (optional additional axis).'''
		return self._instance.Axis7

	@axis7.setter
	def axis7(self, value: T):
		self._instance.Axis7 = value

	@property
	def axis8(self) -> T:
		'''Gets or sets the value for axis 8 (optional additional axis).'''
		return self._instance.Axis8

	@axis8.setter
	def axis8(self, value: T):
		self._instance.Axis8 = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotAxisRawData1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
