import typing
from underautomation.yaskawa.high_speed_e_server.robot_kinematics_position_data import RobotKinematicsPositionData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotKinematicsJointData as robot_kinematics_joint_data

class RobotKinematicsJointData(RobotKinematicsPositionData):
	'''Joint-space position result from a kinematics conversion. Provides the 8 joint axis values in both raw 0.0001° units and as a ready-to-use degrees array.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_kinematics_joint_data()
		else:
			self._instance = _internal

	@property
	def axis_degrees(self) -> typing.List[float]:
		'''Gets the 8 joint axis values converted to degrees. Each element equals the corresponding Axes value divided by 10 000.'''
		return self._instance.AxisDegrees

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotKinematicsJointData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
