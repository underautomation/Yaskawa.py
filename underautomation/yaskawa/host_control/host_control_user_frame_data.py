import typing
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from UnderAutomation.Yaskawa.HostControl import HostControlUserFrameData as host_control_user_frame_data

class HostControlUserFrameData(HostControlResponse):
	'''Contains user coordinate frame data. Retrieved using the RUFRAME command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_user_frame_data()
		else:
			self._instance = _internal

	@property
	def user_coordinate_number(self) -> int:
		'''Gets or sets the user coordinate number (2-65).'''
		return self._instance.UserCoordinateNumber

	@property
	def x(self) -> float:
		'''Gets or sets the X origin position in millimeters.'''
		return self._instance.X

	@property
	def y(self) -> float:
		'''Gets or sets the Y origin position in millimeters.'''
		return self._instance.Y

	@property
	def z(self) -> float:
		'''Gets or sets the Z origin position in millimeters.'''
		return self._instance.Z

	@property
	def rx(self) -> float:
		'''Gets or sets the Rx rotation in degrees.'''
		return self._instance.Rx

	@property
	def ry(self) -> float:
		'''Gets or sets the Ry rotation in degrees.'''
		return self._instance.Ry

	@property
	def rz(self) -> float:
		'''Gets or sets the Rz rotation in degrees.'''
		return self._instance.Rz

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlUserFrameData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
