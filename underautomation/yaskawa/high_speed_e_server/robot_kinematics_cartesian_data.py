import typing
from __future__ import annotation
from underautomation.yaskawa.high_speed_e_server.robot_kinematics_position_data import RobotKinematicsPositionData
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotKinematicsCartesianData as robot_kinematics_cartesian_data

class RobotKinematicsCartesianData(RobotKinematicsPositionData):
	'''Cartesian position result from a kinematics conversion. Provides named X/Y/Z and orientation properties in engineering units in addition to the raw axis values.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_kinematics_cartesian_data()
		else:
			self._instance = _internal

	@property
	def x(self) -> float:
		'''Gets the X position in millimetres (derived from the raw µm axis value).'''
		return self._instance.X

	@property
	def y(self) -> float:
		'''Gets the Y position in millimetres.'''
		return self._instance.Y

	@property
	def z(self) -> float:
		'''Gets the Z position in millimetres.'''
		return self._instance.Z

	@property
	def rx(self) -> float:
		'''Gets the Rx orientation in degrees (derived from the raw 0.0001° axis value).'''
		return self._instance.Rx

	@property
	def ry(self) -> float:
		'''Gets the Ry orientation in degrees.'''
		return self._instance.Ry

	@property
	def rz(self) -> float:
		'''Gets the Rz orientation in degrees.'''
		return self._instance.Rz

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotKinematicsCartesianData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
