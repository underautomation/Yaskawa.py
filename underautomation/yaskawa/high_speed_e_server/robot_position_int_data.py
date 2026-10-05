from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_joint_pulses import IJointPulses
from underautomation.yaskawa.high_speed_e_server.robot_data_header import RobotDataHeader
from underautomation.yaskawa.high_speed_e_server.robot_position_cartesian_data import RobotPositionCartesianData
from underautomation.yaskawa.high_speed_e_server.robot_position_data_1 import RobotPositionData1
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotPositionIntData as robot_position_int_data

class RobotPositionIntData(RobotPositionData1[int], IJointPulses):
	'''Represents robot position data with 32-bit integer axis values. This is the primary type used for pulse-based position data from the High Speed Ethernet Server. Axis values are in pulse units (encoder counts) or scaled coordinate values.'''
	def __init__(self, header: RobotDataHeader, _internal = 0):
		'''Creates a new instance of RobotPositionIntData with the specified header information.

		:param header: Response header containing metadata about the communication.
		'''
		if(_internal == 0):
			self._instance = robot_position_int_data(header._instance if header else None)
		else:
			self._instance = _internal

	def to_cartesian(self) -> RobotPositionCartesianData:
		'''Converts a Cartesian position to millimeters and degrees.

		:returns: The position with X, Y, Z in millimeters and Rx, Ry, Rz in degrees, in the frame given by data_type.
		'''
		return RobotPositionCartesianData(self._instance.ToCartesian())

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotPositionIntData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
