from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_robot_client import IRobotClient
from underautomation.yaskawa.common.i_status_reader import IStatusReader
from underautomation.yaskawa.common.i_yaskawa_client import IYaskawaClient
from underautomation.yaskawa.common.i_position_reader import IPositionReader
from underautomation.yaskawa.common.i_alarm_reader import IAlarmReader
from underautomation.yaskawa.common.i_robot_control import IRobotControl
from underautomation.yaskawa.common.iio_access import IIOAccess
from underautomation.yaskawa.common.i_variable_access import IVariableAccess
from underautomation.yaskawa.common.i_torque_reader import ITorqueReader
from underautomation.yaskawa.common.i_motion_control import IMotionControl
from underautomation.yaskawa.host_control.host_control_alarm_data import HostControlAlarmData
from underautomation.yaskawa.host_control.host_control_status_data import HostControlStatusData
from underautomation.yaskawa.host_control.host_control_job_data import HostControlJobData
from underautomation.yaskawa.host_control.host_control_group_data import HostControlGroupData
from underautomation.yaskawa.host_control.host_control_joint_position_data import HostControlJointPositionData
from underautomation.yaskawa.host_control.host_control_cartesian_position_data import HostControlCartesianPositionData
from underautomation.yaskawa.host_control.host_control_coordinate_system import HostControlCoordinateSystem
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from underautomation.yaskawa.common.robot_mode import RobotMode
from underautomation.yaskawa.common.robot_cycle_type import RobotCycleType
from underautomation.yaskawa.host_control.host_control_speed_type import HostControlSpeedType
from underautomation.yaskawa.host_control.host_control_io_data import HostControlIOData
from underautomation.yaskawa.host_control.host_control_job_directory_data import HostControlJobDirectoryData
from underautomation.yaskawa.host_control.host_control_user_frame_data import HostControlUserFrameData
from underautomation.yaskawa.host_control.host_control_torque_data import HostControlTorqueData
from underautomation.yaskawa.host_control.host_control_encoder_temperature_data import HostControlEncoderTemperatureData
from underautomation.yaskawa.host_control.host_control_system_time_data import HostControlSystemTimeData
from underautomation.yaskawa.host_control.host_control_alarm_string_data import HostControlAlarmStringData
from UnderAutomation.Yaskawa.HostControl.Internal import HostControlClientBase as host_control_client_base
from UnderAutomation.Yaskawa.HostControl import HostControlCoordinateSystem as host_control_coordinate_system
from UnderAutomation.Yaskawa.Common import RobotMode as robot_mode
from UnderAutomation.Yaskawa.Common import RobotCycleType as robot_cycle_type
from UnderAutomation.Yaskawa.HostControl import HostControlSpeedType as host_control_speed_type

class HostControlClientBase(IRobotClient):
	'''Base class implementing the Host Control protocol for Yaskawa robot communication. Provides methods for reading robot status, positions, variables, and executing commands.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_control_client_base()
		else:
			self._instance = _internal

	def close(self) -> None:
		'''Closes the connection to the robot controller and releases resources.'''
		self._instance.Close()

	def get_alarm(self) -> HostControlAlarmData:
		'''Reads the codes of the active error and alarms from the robot controller. Index 0 of the arrays is the error, indexes 1 to 4 are the alarms.

		:returns: Alarm data containing codes and additional information.
		'''
		return HostControlAlarmData(self._instance.GetAlarm())

	def get_status_information(self) -> HostControlStatusData:
		'''Reads the current operational status of the robot controller. Returns information about mode (teach/play), running state, hold status, alarms, and servo power.

		:returns: Status data containing boolean flags for various robot states.
		'''
		return HostControlStatusData(self._instance.GetStatusInformation())

	def get_executing_job_information(self) -> HostControlJobData:
		'''Reads information about the currently selected and executing job (program). Returns job name, current line, and step.

		:returns: Job data containing name, line number, and step.
		'''
		return HostControlJobData(self._instance.GetExecutingJobInformation())

	def get_control_group(self) -> HostControlGroupData:
		'''Reads the current control group configuration. Returns robot group bits, station group bits, and current task number.

		:returns: Control group data.
		'''
		return HostControlGroupData(self._instance.GetControlGroup())

	def get_robot_joint_position(self) -> HostControlJointPositionData:
		'''Reads the current robot joint position in pulse (encoder) values. Returns raw pulse values for all robot axes (S, L, U, R, B, T, and external axes).

		:returns: Joint position data with axis values in encoder pulses.
		'''
		return HostControlJointPositionData(self._instance.GetRobotJointPosition())

	def get_robot_cartesian_position(self, coordinateSystem: HostControlCoordinateSystem=HostControlCoordinateSystem.Base, includeExternalAxes: bool=False) -> HostControlCartesianPositionData:
		'''Reads the current robot Cartesian position (TCP position and orientation). Coordinates are returned in millimeters for X, Y, Z and degrees for Rx, Ry, Rz.

		:param coordinateSystem: The coordinate system for the position (default: Base).
		:param includeExternalAxes: Whether to include external axis positions (default: false).
		:returns: Cartesian position data with coordinates in mm and degrees.
		'''
		return HostControlCartesianPositionData(self._instance.GetRobotCartesianPosition(host_control_coordinate_system(int(coordinateSystem)), includeExternalAxes))

	def set_hold(self, enable: bool) -> HostControlResponse:
		'''Sets the hold state of the robot. When hold is ON, robot motion is paused. When OFF, motion can resume.

		:param enable: True to hold (pause), false to release hold.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetHold(enable))

	def alarm_reset(self) -> HostControlResponse:
		'''Resets the current alarm condition. The cause of the alarm must be resolved before reset will succeed. Command remote must be enabled on the controller.

		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.AlarmReset())

	def error_cancel(self) -> HostControlResponse:
		'''Cancels the current error condition. Used for recoverable errors that don't require full alarm reset.

		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.ErrorCancel())

	def set_mode(self, mode: RobotMode) -> HostControlResponse:
		'''Sets the robot operation mode (Teach or Play).

		:param mode: The target mode.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetMode(robot_mode(int(mode))))

	def set_cycle(self, cycle: RobotCycleType) -> HostControlResponse:
		'''Sets the execution cycle type (Step, One Cycle, or Automatic).

		:param cycle: The target cycle type.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetCycle(robot_cycle_type(int(cycle))))

	def set_servo(self, enable: bool) -> HostControlResponse:
		'''Enables or disables servo power. Servo must be ON for the robot to move. Uses extended timeout for power-on.

		:param enable: True to enable servo power, false to disable.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetServo(enable))

	def set_teach_pendant_lock_state(self, locked: bool) -> HostControlResponse:
		'''Locks or unlocks the operations from the teach pendant and from the I/O operation signals. The emergency stop of the teach pendant stays active. Command remote must be enabled on the controller.

		:param locked: True to enable interlock, false to disable.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetTeachPendantLockState(locked))

	def display(self, message: str) -> HostControlResponse:
		'''Displays a message on the remote display of the teach pendant. Command remote must be enabled on the controller.

		:param message: The message to display (max 30 characters).
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.Display(message))

	def start_job(self, jobName: str=None) -> HostControlResponse:
		'''Starts job execution. Starts the currently selected job, or starts a specific job if specified.

		:param jobName: Optional job name to start. If null, starts the current job.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.StartJob(jobName))

	def set_control_group(self, robotGroup: int, stationGroup: int) -> HostControlResponse:
		'''Changes the control group selection.

		:param robotGroup: Robot group bits (bit 0 = R1, bit 1 = R2, etc.).
		:param stationGroup: Station group bits (bit 0 = S1, bit 1 = S2, etc.).
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetControlGroup(robotGroup, stationGroup))

	def set_task(self, task: int) -> HostControlResponse:
		'''Changes the current task selection.

		:param task: Task number (0 = Master, 1-15 = Sub tasks).
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetTask(task))

	def move_joint(self, speedPercent: int, coordinateSystem: HostControlCoordinateSystem, x: float, y: float, z: float, rx: float, ry: float, rz: float, type: int=0, toolNumber: int=0) -> HostControlResponse:
		'''Moves the robot to a Cartesian position using joint interpolation. Joint motion is faster but the path is not linear.

		:param speedPercent: Speed percentage (0-100).
		:param coordinateSystem: Coordinate system for the target position.
		:param x: X position in mm.
		:param y: Y position in mm.
		:param z: Z position in mm.
		:param rx: Rx rotation in degrees.
		:param ry: Ry rotation in degrees.
		:param rz: Rz rotation in degrees.
		:param type: Robot posture/configuration type.
		:param toolNumber: Tool number (0-63).
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.MoveJoint(speedPercent, host_control_coordinate_system(int(coordinateSystem)), x, y, z, rx, ry, rz, type, toolNumber))

	def move_linear(self, speedType: HostControlSpeedType, speed: float, coordinateSystem: HostControlCoordinateSystem, x: float, y: float, z: float, rx: float, ry: float, rz: float, type: int=0, toolNumber: int=0) -> HostControlResponse:
		'''Moves the robot to a Cartesian position using linear interpolation. Linear motion follows a straight line path.

		:param speedType: Speed type (percentage or mm/s).
		:param speed: Speed value.
		:param coordinateSystem: Coordinate system for the target position.
		:param x: X position in mm.
		:param y: Y position in mm.
		:param z: Z position in mm.
		:param rx: Rx rotation in degrees.
		:param ry: Ry rotation in degrees.
		:param rz: Rz rotation in degrees.
		:param type: Robot posture/configuration type.
		:param toolNumber: Tool number (0-63).
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.MoveLinear(host_control_speed_type(int(speedType)), speed, host_control_coordinate_system(int(coordinateSystem)), x, y, z, rx, ry, rz, type, toolNumber))

	def move_incremental(self, speedType: HostControlSpeedType, speed: float, coordinateSystem: HostControlCoordinateSystem, dx: float, dy: float, dz: float, drx: float, dry: float, drz: float, toolNumber: int=0) -> HostControlResponse:
		'''Moves the robot incrementally using linear interpolation. Movement is relative to the current position.

		:param speedType: Speed type (percentage or mm/s).
		:param speed: Speed value.
		:param coordinateSystem: Coordinate system for the increment.
		:param dx: X increment in mm.
		:param dy: Y increment in mm.
		:param dz: Z increment in mm.
		:param drx: Rx increment in degrees.
		:param dry: Ry increment in degrees.
		:param drz: Rz increment in degrees.
		:param toolNumber: Tool number (0-63).
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.MoveIncremental(host_control_speed_type(int(speedType)), speed, host_control_coordinate_system(int(coordinateSystem)), dx, dy, dz, drx, dry, drz, toolNumber))

	def move_pulse_joint(self, speedPercent: int, s: int, l: int, u: int, r: int, b: int, t: int, toolNumber: int=0) -> HostControlResponse:
		'''Moves the robot to a pulse position using joint interpolation.

		:param speedPercent: Speed percentage (0-100).
		:param s: S axis position in pulses.
		:param l: L axis position in pulses.
		:param u: U axis position in pulses.
		:param r: R axis position in pulses.
		:param b: B axis position in pulses.
		:param t: T axis position in pulses.
		:param toolNumber: Tool number (0-63).
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.MovePulseJoint(speedPercent, s, l, u, r, b, t, toolNumber))

	def move_pulse_linear(self, speedType: HostControlSpeedType, speed: float, s: int, l: int, u: int, r: int, b: int, t: int, toolNumber: int=0) -> HostControlResponse:
		'''Moves the robot to a pulse position using linear interpolation.

		:param speedType: Speed type (percentage or mm/s).
		:param speed: Speed value.
		:param s: S axis position in pulses.
		:param l: L axis position in pulses.
		:param u: U axis position in pulses.
		:param r: R axis position in pulses.
		:param b: B axis position in pulses.
		:param t: T axis position in pulses.
		:param toolNumber: Tool number (0-63).
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.MovePulseLinear(host_control_speed_type(int(speedType)), speed, s, l, u, r, b, t, toolNumber))

	def read_io(self, startAddress: int, count: int) -> HostControlIOData:
		'''Reads I/O signals from the robot controller. Each byte holds 8 signals.

		:param startAddress: Contact number of the first signal, as displayed on the teach pendant (for example 10010 for #10010). Use a number that ends with 0, so that each byte is one group of 8 signals.
		:param count: Number of bytes to read (1 to 256).
		:returns: I/O data containing the read values.
		'''
		return HostControlIOData(self._instance.ReadIO(startAddress, count))

	def write_io(self, startAddress: int, data: typing.List[int]) -> HostControlResponse:
		'''Writes I/O signals to the robot controller. Each byte holds 8 signals. By default, the controller accepts only the network input signals (#27010 to #29567).

		:param startAddress: Contact number of the first signal, as displayed on the teach pendant (for example 27010 for #27010). Use a number that ends with 0, so that each byte is one group of 8 signals.
		:param data: Data bytes to write (1 to 256 bytes).
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.WriteIO(startAddress, data))

	def read_byte(self, firstIndex: int, count: int) -> typing.List[int]:
		'''Reads byte (B) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param count: Number of variables to read.
		:returns: Array of byte values.
		'''
		return self._instance.ReadByte(firstIndex, count)

	def write_byte(self, firstIndex: int, data: typing.List[int]) -> None:
		'''Writes byte (B) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param data: Byte values to write.
		'''
		self._instance.WriteByte(firstIndex, data)

	def read_integer(self, firstIndex: int, count: int) -> typing.List[int]:
		'''Reads integer (I) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param count: Number of variables to read.
		:returns: Array of 16-bit signed integer values.
		'''
		return self._instance.ReadInteger(firstIndex, count)

	def write_integer(self, firstIndex: int, data: typing.List[int]) -> None:
		'''Writes integer (I) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param data: Integer values to write.
		'''
		self._instance.WriteInteger(firstIndex, data)

	def read_double_integer(self, firstIndex: int, count: int) -> typing.List[int]:
		'''Reads double integer (D) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param count: Number of variables to read.
		:returns: Array of 32-bit signed integer values.
		'''
		return self._instance.ReadDoubleInteger(firstIndex, count)

	def write_double_integer(self, firstIndex: int, data: typing.List[int]) -> None:
		'''Writes double integer (D) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param data: Double integer values to write.
		'''
		self._instance.WriteDoubleInteger(firstIndex, data)

	def read_real(self, firstIndex: int, count: int) -> typing.List[float]:
		'''Reads real (R) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param count: Number of variables to read.
		:returns: Array of floating-point values.
		'''
		return self._instance.ReadReal(firstIndex, count)

	def write_real(self, firstIndex: int, data: typing.List[float]) -> None:
		'''Writes real (R) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param data: Real values to write.
		'''
		self._instance.WriteReal(firstIndex, data)

	def read16_bytes_char(self, firstIndex: int, count: int) -> typing.List[str]:
		'''Reads 16-byte string (S) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param count: Number of variables to read.
		:returns: Array of string values.
		'''
		return self._instance.Read16BytesChar(firstIndex, count)

	def write16_bytes_char(self, firstIndex: int, data: typing.List[str]) -> None:
		'''Writes 16-byte string (S) variables starting at the specified index.

		:param firstIndex: Starting variable index.
		:param data: String values to write.
		'''
		self._instance.Write16BytesChar(firstIndex, data)

	def get_job_directory(self, jobNameFilter: str="*") -> HostControlJobDirectoryData:
		'''Reads the job directory listing from the robot controller.

		:param jobNameFilter: Job name filter (use "*" for all jobs, or specify a pattern).
		:returns: Job directory data containing the list of job names.
		'''
		return HostControlJobDirectoryData(self._instance.GetJobDirectory(jobNameFilter))

	def get_user_frame(self, userCoordinateNumber: int) -> HostControlUserFrameData:
		'''Reads user coordinate frame data from the robot controller. Returns the three reference points (ORG, XX, XY) defining the user coordinate system.

		:param userCoordinateNumber: User coordinate number (2-64).
		:returns: User frame data containing the coordinate transformation.
		'''
		return HostControlUserFrameData(self._instance.GetUserFrame(userCoordinateNumber))

	def set_user_frame(self, userCoordinateNumber: int, frame: HostControlUserFrameData) -> HostControlResponse:
		'''Writes user coordinate frame data to the robot controller. Defines a user coordinate system using three reference points (ORG, XX, XY).

		:param userCoordinateNumber: User coordinate number (2-64).
		:param frame: User frame data containing the reference points.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetUserFrame(userCoordinateNumber, frame._instance if frame else None))

	def delete_job(self, jobName: str) -> HostControlResponse:
		'''Deletes a specified job from the robot controller.

		:param jobName: Job name to delete, or "*" to delete all jobs.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.DeleteJob(jobName))

	def set_master_job(self, jobName: str) -> HostControlResponse:
		'''Sets a specified job as the master job and execution job.

		:param jobName: Job name to set as master.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetMasterJob(jobName))

	def select_job(self, jobName: str, line: int) -> HostControlResponse:
		'''Sets the job name and line number for execution.

		:param jobName: Job name to select.
		:param line: Line number to set (0-9999).
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SelectJob(jobName, line))

	def wait_for_job_completion(self, timeoutSeconds: int=-1) -> bool:
		'''Waits for the current job to complete or the specified timeout to elapse. No response is sent until the job completes or the timeout expires.

		:param timeoutSeconds: Waiting time in seconds (-1 for infinite, up to 32767).
		:returns: True if the job completed, false if stopped or timed out.
		'''
		return self._instance.WaitForJobCompletion(timeoutSeconds)

	def convert_to_relative_job(self, jobName: str, coordinateSystem: HostControlCoordinateSystem) -> HostControlResponse:
		'''Converts a specified job to a relative job of a specified coordinate system. Requires the relative job function on the robot controller.

		:param jobName: Name of the job to convert.
		:param coordinateSystem: Target coordinate system for conversion.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.ConvertToRelativeJob(jobName, host_control_coordinate_system(int(coordinateSystem))))

	def convert_to_standard_job(self, jobName: str, convertingMethod: int, referencePositionVariable: int) -> HostControlResponse:
		'''Converts a specified job to a standard job (pulse job). Requires the relative job function on the robot controller.

		:param jobName: Name of the job to convert.
		:param convertingMethod: Converting method: 0 = Previous step (B-axis sign same), 1 = Type regarded, 2 = Previous step (R-axis travel minimum).
		:param referencePositionVariable: Position variable number for the first step conversion reference.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.ConvertToStandardJob(jobName, convertingMethod, referencePositionVariable))

	def get_torque(self) -> HostControlTorqueData:
		'''Reads the current torque values of all robot axes. Returns values as a percentage of the maximum rated torque.

		:returns: Torque data containing values for each axis.
		'''
		return HostControlTorqueData(self._instance.GetTorque())

	def get_max_torque(self) -> HostControlTorqueData:
		'''Reads the maximum torque values of all robot axes. Returns values as a percentage of the maximum rated torque.

		:returns: Torque data containing maximum values for each axis.
		'''
		return HostControlTorqueData(self._instance.GetMaxTorque())

	def get_encoder_temperature(self) -> HostControlEncoderTemperatureData:
		'''Reads the encoder temperature values of all robot axes.

		:returns: Encoder temperature data containing values for each axis in degrees Celsius.
		'''
		return HostControlEncoderTemperatureData(self._instance.GetEncoderTemperature())

	def get_system_time(self) -> HostControlSystemTimeData:
		'''Reads the system time from the robot controller.

		:returns: System time data containing year, date, time, seconds and day of week.
		'''
		return HostControlSystemTimeData(self._instance.GetSystemTime())

	def get_absolute_encoder_position(self, axisNumber: int) -> int:
		'''Reads the absolute encoder position of a specific axis.

		:param axisNumber: Axis number (0-based).
		:returns: The absolute encoder position value.
		'''
		return self._instance.GetAbsoluteEncoderPosition(axisNumber)

	def set_absolute_encoder_position(self, axisNumber: int, value: int) -> HostControlResponse:
		'''Writes the absolute encoder data for a specific axis.

		:param axisNumber: Axis number (0-based).
		:param value: The absolute encoder value to write.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetAbsoluteEncoderPosition(axisNumber, value))

	def set_frame_type(self, frameType: int) -> HostControlResponse:
		'''Sets the coordinate frame type used for position display on the pendant.

		:param frameType: Frame type (0 = Base, 1 = Robot, etc.).
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetFrameType(frameType))

	def get_alarm_with_messages(self) -> HostControlAlarmStringData:
		'''Reads the active error and alarms with their text messages from the robot controller. Returns the error and up to 4 alarms, each with its code, sub-code and message.

		:returns: Error and alarm data with the text message of each entry.
		'''
		return HostControlAlarmStringData(self._instance.GetAlarmWithMessages())

	@property
	def address(self) -> str:
		'''Gets the address of the connected robot controller (IP address).'''
		return self._instance.Address

	@property
	def connected(self) -> bool:
		'''Gets a value indicating whether the client is connected to a robot controller.'''
		return self._instance.Connected

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostControlClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
