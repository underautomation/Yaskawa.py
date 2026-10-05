from __future__ import annotations
import typing
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from UnderAutomation.Yaskawa.HostControl import HostControlUserFrameData as host_control_user_frame_data

class HostControlUserFrameData(HostControlResponse):
	'''Contains user coordinate frame data defined by three reference points (ORG, XX, XY). Retrieved using the RUFRAME command, written using the WUFRAME command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_user_frame_data()
		else:
			self._instance = _internal

	@property
	def user_coordinate_number(self) -> int:
		'''Gets or sets the user coordinate number (2-64).'''
		return self._instance.UserCoordinateNumber

	@property
	def org_x(self) -> float:
		'''ORG X coordinate value in mm.'''
		return self._instance.OrgX

	@property
	def org_y(self) -> float:
		'''ORG Y coordinate value in mm.'''
		return self._instance.OrgY

	@property
	def org_z(self) -> float:
		'''ORG Z coordinate value in mm.'''
		return self._instance.OrgZ

	@property
	def org_tx(self) -> float:
		'''ORG wrist angle TX in degrees.'''
		return self._instance.OrgTx

	@property
	def org_ty(self) -> float:
		'''ORG wrist angle TY in degrees.'''
		return self._instance.OrgTy

	@property
	def org_tz(self) -> float:
		'''ORG wrist angle TZ in degrees.'''
		return self._instance.OrgTz

	@property
	def org_type(self) -> int:
		'''ORG posture type.'''
		return self._instance.OrgType

	@property
	def xx_x(self) -> float:
		'''XX X coordinate value in mm.'''
		return self._instance.XxX

	@property
	def xx_y(self) -> float:
		'''XX Y coordinate value in mm.'''
		return self._instance.XxY

	@property
	def xx_z(self) -> float:
		'''XX Z coordinate value in mm.'''
		return self._instance.XxZ

	@property
	def xx_tx(self) -> float:
		'''XX wrist angle TX in degrees.'''
		return self._instance.XxTx

	@property
	def xx_ty(self) -> float:
		'''XX wrist angle TY in degrees.'''
		return self._instance.XxTy

	@property
	def xx_tz(self) -> float:
		'''XX wrist angle TZ in degrees.'''
		return self._instance.XxTz

	@property
	def xx_type(self) -> int:
		'''XX posture type.'''
		return self._instance.XxType

	@property
	def xy_x(self) -> float:
		'''XY X coordinate value in mm.'''
		return self._instance.XyX

	@property
	def xy_y(self) -> float:
		'''XY Y coordinate value in mm.'''
		return self._instance.XyY

	@property
	def xy_z(self) -> float:
		'''XY Z coordinate value in mm.'''
		return self._instance.XyZ

	@property
	def xy_tx(self) -> float:
		'''XY wrist angle TX in degrees.'''
		return self._instance.XyTx

	@property
	def xy_ty(self) -> float:
		'''XY wrist angle TY in degrees.'''
		return self._instance.XyTy

	@property
	def xy_tz(self) -> float:
		'''XY wrist angle TZ in degrees.'''
		return self._instance.XyTz

	@property
	def xy_type(self) -> int:
		'''XY posture type.'''
		return self._instance.XyType

	@property
	def tool_number(self) -> int:
		'''Tool number (0-63).'''
		return self._instance.ToolNumber

	@property
	def axis7(self) -> int:
		'''7th axis pulses (for travel axis, mm).'''
		return self._instance.Axis7

	@property
	def axis8(self) -> int:
		'''8th axis pulses (for travel axis, mm).'''
		return self._instance.Axis8

	@property
	def axis9(self) -> int:
		'''9th axis pulses (for travel axis, mm).'''
		return self._instance.Axis9

	@property
	def axis10(self) -> int:
		'''10th axis pulses.'''
		return self._instance.Axis10

	@property
	def axis11(self) -> int:
		'''11th axis pulses.'''
		return self._instance.Axis11

	@property
	def axis12(self) -> int:
		'''12th axis pulses.'''
		return self._instance.Axis12

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
