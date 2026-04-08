from __future__ import annotations
import typing
from underautomation.yaskawa.high_speed_e_server.orientation_flip_information import OrientationFlipInformation
from underautomation.yaskawa.high_speed_e_server.arm_flip_information import ArmFlipInformation
from underautomation.yaskawa.high_speed_e_server.flip_no_flip_information import FlipNoFlipInformation
from underautomation.yaskawa.high_speed_e_server.axis_flip_information import AxisFlipInformation
from underautomation.yaskawa.high_speed_e_server.regarded_reverse_position_specified import RegardedReversePositionSpecified
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotPosture as robot_posture
from UnderAutomation.Yaskawa.HighSpeedEServer import OrientationFlipInformation as orientation_flip_information
from UnderAutomation.Yaskawa.HighSpeedEServer import ArmFlipInformation as arm_flip_information
from UnderAutomation.Yaskawa.HighSpeedEServer import FlipNoFlipInformation as flip_no_flip_information
from UnderAutomation.Yaskawa.HighSpeedEServer import AxisFlipInformation as axis_flip_information
from UnderAutomation.Yaskawa.HighSpeedEServer import RegardedReversePositionSpecified as regarded_reverse_position_specified

class RobotPosture:
	'''Represents the complete robot posture (form) configuration. Encodes the kinematic configuration choices that determine which of multiple inverse kinematics solutions is used to reach a Cartesian position.'''
	def __init__(self, orientation: OrientationFlipInformation, arm: ArmFlipInformation, flip: FlipNoFlipInformation, rAxis: AxisFlipInformation, tAxis: AxisFlipInformation, sAxis: AxisFlipInformation, redundant: OrientationFlipInformation, regardedReversePositionSpecified: RegardedReversePositionSpecified, lAxis: AxisFlipInformation, uAxis: AxisFlipInformation, bAxis: AxisFlipInformation, eAxis: AxisFlipInformation, wAxis: AxisFlipInformation, _internal = 0):
		'''Creates a new RobotPosture with specified configuration values.

		:param orientation: Front/back orientation configuration.
		:param arm: Upper/lower arm configuration.
		:param flip: Flip/no-flip wrist configuration.
		:param rAxis: R-axis angle range configuration.
		:param tAxis: T-axis angle range configuration.
		:param sAxis: S-axis angle range configuration.
		:param redundant: Redundant axis orientation configuration.
		:param regardedReversePositionSpecified: Reverse position specification mode.
		:param lAxis: L-axis angle range configuration.
		:param uAxis: U-axis angle range configuration.
		:param bAxis: B-axis angle range configuration.
		:param eAxis: E-axis angle range configuration.
		:param wAxis: W-axis angle range configuration.
		'''
		if(_internal == 0):
			self._instance = robot_posture(orientation, arm, flip, rAxis, tAxis, sAxis, redundant, regardedReversePositionSpecified, lAxis, uAxis, bAxis, eAxis, wAxis)
		else:
			self._instance = _internal

	def to_integer(self) -> int:
		'''Converts the posture to a single 16-bit integer value. Form is stored in the low byte, ExtendedForm in the high byte.

		:returns: Combined integer representation of the posture.
		'''
		return self._instance.ToInteger()

	@staticmethod
	def from_integer(value: int) -> 'RobotPosture':
		'''Creates a RobotPosture from a combined 16-bit integer value.

		:param value: Combined integer with Form in low byte and ExtendedForm in high byte.
		:returns: A new RobotPosture instance.
		'''
		return RobotPosture(None, None, None, None, None, None, None, None, None, None, None, None, None, robot_posture.FromInteger(value))

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	@property
	def form(self) -> int:
		'''Gets or sets the primary form byte encoding basic posture flags. Bit-encoded: orientation, arm, flip, R-axis, T-axis, S-axis, redundant, reverse position.'''
		return self._instance.Form

	@form.setter
	def form(self, value: int):
		self._instance.Form = value

	@property
	def extended_form(self) -> int:
		'''Gets or sets the extended form byte for additional axis configurations. Bit-encoded: L-axis, U-axis, B-axis, E-axis, W-axis range flags.'''
		return self._instance.ExtendedForm

	@extended_form.setter
	def extended_form(self, value: int):
		self._instance.ExtendedForm = value

	@property
	def orientation(self) -> OrientationFlipInformation:
		'''Gets or sets the front/back orientation configuration. Specifies where the B-axis rotation center locates relative to the S-axis when viewing the L and U axes from the right-hand side.'''
		return OrientationFlipInformation(int(self._instance.Orientation))

	@orientation.setter
	def orientation(self, value: OrientationFlipInformation):
		self._instance.Orientation = orientation_flip_information(int(value))

	@property
	def arm(self) -> ArmFlipInformation:
		'''Gets or sets the upper/lower arm configuration based on L and U axis positions.'''
		return ArmFlipInformation(int(self._instance.Arm))

	@arm.setter
	def arm(self, value: ArmFlipInformation):
		self._instance.Arm = arm_flip_information(int(value))

	@property
	def flip(self) -> FlipNoFlipInformation:
		'''Gets or sets the flip/no-flip wrist configuration.'''
		return FlipNoFlipInformation(int(self._instance.Flip))

	@flip.setter
	def flip(self, value: FlipNoFlipInformation):
		self._instance.Flip = flip_no_flip_information(int(value))

	@property
	def r_axis(self) -> AxisFlipInformation:
		'''Gets or sets the R-axis (wrist rotation) angle range configuration.'''
		return AxisFlipInformation(int(self._instance.RAxis))

	@r_axis.setter
	def r_axis(self, value: AxisFlipInformation):
		self._instance.RAxis = axis_flip_information(int(value))

	@property
	def t_axis(self) -> AxisFlipInformation:
		'''Gets or sets the T-axis (tool rotation) angle range configuration.'''
		return AxisFlipInformation(int(self._instance.TAxis))

	@t_axis.setter
	def t_axis(self, value: AxisFlipInformation):
		self._instance.TAxis = axis_flip_information(int(value))

	@property
	def s_axis(self) -> AxisFlipInformation:
		'''Gets or sets the S-axis (base rotation) angle range configuration.'''
		return AxisFlipInformation(int(self._instance.SAxis))

	@s_axis.setter
	def s_axis(self, value: AxisFlipInformation):
		self._instance.SAxis = axis_flip_information(int(value))

	@property
	def redundant(self) -> OrientationFlipInformation:
		'''Gets or sets the redundant axis orientation configuration (for 7+ axis robots).'''
		return OrientationFlipInformation(int(self._instance.Redundant))

	@redundant.setter
	def redundant(self, value: OrientationFlipInformation):
		self._instance.Redundant = orientation_flip_information(int(value))

	@property
	def regarded_reverse_position_specified(self) -> RegardedReversePositionSpecified:
		'''Gets or sets the reverse position specification mode.'''
		return RegardedReversePositionSpecified(int(self._instance.RegardedReversePositionSpecified))

	@regarded_reverse_position_specified.setter
	def regarded_reverse_position_specified(self, value: RegardedReversePositionSpecified):
		self._instance.RegardedReversePositionSpecified = regarded_reverse_position_specified(int(value))

	@property
	def l_axis(self) -> AxisFlipInformation:
		'''Gets or sets the L-axis (lower arm) angle range configuration from extended form.'''
		return AxisFlipInformation(int(self._instance.LAxis))

	@l_axis.setter
	def l_axis(self, value: AxisFlipInformation):
		self._instance.LAxis = axis_flip_information(int(value))

	@property
	def u_axis(self) -> AxisFlipInformation:
		'''Gets or sets the U-axis (upper arm) angle range configuration from extended form.'''
		return AxisFlipInformation(int(self._instance.UAxis))

	@u_axis.setter
	def u_axis(self, value: AxisFlipInformation):
		self._instance.UAxis = axis_flip_information(int(value))

	@property
	def b_axis(self) -> AxisFlipInformation:
		'''Gets or sets the B-axis (wrist bend) angle range configuration from extended form.'''
		return AxisFlipInformation(int(self._instance.BAxis))

	@b_axis.setter
	def b_axis(self, value: AxisFlipInformation):
		self._instance.BAxis = axis_flip_information(int(value))

	@property
	def e_axis(self) -> AxisFlipInformation:
		'''Gets or sets the E-axis (external/elbow) angle range configuration from extended form.'''
		return AxisFlipInformation(int(self._instance.EAxis))

	@e_axis.setter
	def e_axis(self, value: AxisFlipInformation):
		self._instance.EAxis = axis_flip_information(int(value))

	@property
	def w_axis(self) -> AxisFlipInformation:
		'''Gets or sets the W-axis angle range configuration from extended form.'''
		return AxisFlipInformation(int(self._instance.WAxis))

	@w_axis.setter
	def w_axis(self, value: AxisFlipInformation):
		self._instance.WAxis = axis_flip_information(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotPosture):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default posture with Form=0 and ExtendedForm=0.
RobotPosture.Default = RobotPosture(None, None, None, None, None, None, None, None, None, None, None, None, None, robot_posture.Default)
