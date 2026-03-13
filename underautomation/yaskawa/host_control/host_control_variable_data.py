import typing
from underautomation.yaskawa.host_control.host_control_variable_type import HostControlVariableType
from underautomation.yaskawa.host_control.host_control_cartesian_position_data import HostControlCartesianPositionData
from underautomation.yaskawa.host_control.host_control_joint_position_data import HostControlJointPositionData
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from UnderAutomation.Yaskawa.HostControl import HostControlVariableData as host_control_variable_data
from UnderAutomation.Yaskawa.HostControl import HostControlVariableType as host_control_variable_type

class HostControlVariableData(HostControlResponse):
	'''Contains variable data retrieved from the robot controller. Retrieved using the SAVEV command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_variable_data()
		else:
			self._instance = _internal

	@property
	def variable_type(self) -> HostControlVariableType:
		'''Gets or sets the variable type.'''
		return HostControlVariableType(int(self._instance.VariableType))

	@property
	def variable_number(self) -> int:
		'''Gets or sets the variable number/index.'''
		return self._instance.VariableNumber

	@property
	def string_value(self) -> str:
		'''Gets or sets the variable value as string.'''
		return self._instance.StringValue

	@property
	def int_value(self) -> int:
		'''Gets or sets the variable value as integer (for B, I, D types).'''
		return self._instance.IntValue

	@property
	def double_value(self) -> float:
		'''Gets or sets the variable value as double (for R type).'''
		return self._instance.DoubleValue

	@property
	def position_value(self) -> HostControlCartesianPositionData:
		'''Gets or sets the position variable data (for P type).'''
		return HostControlCartesianPositionData(self._instance.PositionValue)

	@property
	def base_position_value(self) -> HostControlCartesianPositionData:
		'''Gets or sets the base position variable data (for BP type).'''
		return HostControlCartesianPositionData(self._instance.BasePositionValue)

	@property
	def external_position_value(self) -> HostControlJointPositionData:
		'''Gets or sets the external position variable data (for EX type).'''
		return HostControlJointPositionData(self._instance.ExternalPositionValue)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlVariableData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
