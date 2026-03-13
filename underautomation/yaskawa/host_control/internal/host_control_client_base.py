import typing
from underautomation.yaskawa.host_control.host_control_alarm_data import HostControlAlarmData
from underautomation.yaskawa.host_control.host_control_status_data import HostControlStatusData
from underautomation.yaskawa.host_control.host_control_job_data import HostControlJobData
from underautomation.yaskawa.host_control.host_control_group_data import HostControlGroupData
from underautomation.yaskawa.host_control.host_control_joint_position_data import HostControlJointPositionData
from underautomation.yaskawa.host_control.host_control_cartesian_position_data import HostControlCartesianPositionData
from underautomation.yaskawa.host_control.host_control_coordinate_system import HostControlCoordinateSystem
from underautomation.yaskawa.host_control.host_control_response import HostControlResponse
from underautomation.yaskawa.host_control.host_control_robot_mode import HostControlRobotMode
from underautomation.yaskawa.host_control.host_control_cycle_type import HostControlCycleType
from underautomation.yaskawa.host_control.host_control_speed_type import HostControlSpeedType
from underautomation.yaskawa.host_control.host_control_io_data import HostControlIOData
from underautomation.yaskawa.host_control.host_control_variable_data import HostControlVariableData
from underautomation.yaskawa.host_control.host_control_variable_type import HostControlVariableType
from underautomation.yaskawa.host_control.host_control_job_directory_data import HostControlJobDirectoryData
from underautomation.yaskawa.host_control.host_control_user_frame_data import HostControlUserFrameData
from UnderAutomation.Yaskawa.HostControl.Internal import HostControlClientBase as host_control_client_base
from UnderAutomation.Yaskawa.HostControl import HostControlCoordinateSystem as host_control_coordinate_system
from UnderAutomation.Yaskawa.HostControl import HostControlRobotMode as host_control_robot_mode
from UnderAutomation.Yaskawa.HostControl import HostControlCycleType as host_control_cycle_type
from UnderAutomation.Yaskawa.HostControl import HostControlSpeedType as host_control_speed_type
from UnderAutomation.Yaskawa.HostControl import HostControlVariableType as host_control_variable_type

class HostControlClientBase:
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
		'''Reads alarm codes from the robot controller. Retrieves up to 10 alarm/error codes and their associated data.

		:returns: Alarm data containing codes and additional information.
		'''
		return HostControlAlarmData(self._instance.GetAlarm())

	def get_status(self) -> HostControlStatusData:
		'''Reads the current operational status of the robot controller. Returns information about mode (teach/play), running state, hold status, alarms, and servo power.

		:returns: Status data containing boolean flags for various robot states.
		'''
		return HostControlStatusData(self._instance.GetStatus())

	def get_executing_job(self) -> HostControlJobData:
		'''Reads information about the currently selected and executing job (program). Returns job name, current line, and step.

		:returns: Job data containing name, line number, and step.
		'''
		return HostControlJobData(self._instance.GetExecutingJob())

	def get_control_group(self) -> HostControlGroupData:
		'''Reads the current control group configuration. Returns robot group bits, station group bits, and current task number.

		:returns: Control group data.
		'''
		return HostControlGroupData(self._instance.GetControlGroup())

	def get_joint_position(self) -> HostControlJointPositionData:
		'''Reads the current robot joint position in pulse (encoder) values. Returns raw pulse values for all robot axes (S, L, U, R, B, T, and external axes).

		:returns: Joint position data with axis values in encoder pulses.
		'''
		return HostControlJointPositionData(self._instance.GetJointPosition())

	def get_cartesian_position(self, coordinateSystem: HostControlCoordinateSystem=HostControlCoordinateSystem.Base, includeExternalAxes: bool=False) -> HostControlCartesianPositionData:
		'''Reads the current robot Cartesian position (TCP position and orientation). Coordinates are returned in millimeters for X, Y, Z and degrees for Rx, Ry, Rz.

		:param coordinateSystem: The coordinate system for the position (default: Base).
		:param includeExternalAxes: Whether to include external axis positions (default: false).
		:returns: Cartesian position data with coordinates in mm and degrees.
		'''
		return HostControlCartesianPositionData(self._instance.GetCartesianPosition(host_control_coordinate_system(int(coordinateSystem)), includeExternalAxes))

	def set_hold(self, enable: bool) -> HostControlResponse:
		'''Sets the hold state of the robot. When hold is ON, robot motion is paused. When OFF, motion can resume.

		:param enable: True to hold (pause), false to release hold.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetHold(enable))

	def alarm_reset(self) -> HostControlResponse:
		'''Resets the current alarm condition. The cause of the alarm must be resolved before reset will succeed.

		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.AlarmReset())

	def error_cancel(self) -> HostControlResponse:
		'''Cancels the current error condition. Used for recoverable errors that don't require full alarm reset.

		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.ErrorCancel())

	def set_mode(self, mode: HostControlRobotMode) -> HostControlResponse:
		'''Sets the robot operation mode (Teach or Play).

		:param mode: The target mode.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetMode(host_control_robot_mode(int(mode))))

	def set_cycle(self, cycle: HostControlCycleType) -> HostControlResponse:
		'''Sets the execution cycle type (Step, One Cycle, or Automatic).

		:param cycle: The target cycle type.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetCycle(host_control_cycle_type(int(cycle))))

	def set_servo(self, enable: bool) -> HostControlResponse:
		'''Enables or disables servo power. Servo must be ON for the robot to move. Uses extended timeout for power-on.

		:param enable: True to enable servo power, false to disable.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetServo(enable))

	def set_interlock(self, enable: bool) -> HostControlResponse:
		'''Sets the interlock (H-Lock) state.

		:param enable: True to enable interlock, false to disable.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.SetInterlock(enable))

	def display_message(self, message: str) -> HostControlResponse:
		'''Displays a message on the robot pendant.

		:param message: The message to display (max 30 characters).
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.DisplayMessage(message))

	def start_job(self, jobName: str="None") -> HostControlResponse:
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
		'''Moves the robot to a Cartesian position using joint interpolation (MOVJ). Joint motion is faster but the path is not linear.

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
		'''Moves the robot to a Cartesian position using linear interpolation (MOVL). Linear motion follows a straight line path.

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
		'''Moves the robot incrementally using linear interpolation (IMOV). Movement is relative to the current position.

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
		'''Moves the robot to a pulse position using joint interpolation (PMOVJ).

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
		'''Moves the robot to a pulse position using linear interpolation (PMOVL).

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
		'''Reads I/O signals from the robot controller.

		:param startAddress: Starting I/O contact number (must be multiple of 10 + 1).
		:param count: Number of bytes to read (must be multiple of 8).
		:returns: I/O data containing the read values.
		'''
		return HostControlIOData(self._instance.ReadIO(startAddress, count))

	def write_io(self, startAddress: int, data: typing.List[int]) -> HostControlResponse:
		'''Writes I/O signals to the robot controller.

		:param startAddress: Starting I/O contact number (must be multiple of 10 + 1).
		:param data: Data bytes to write.
		:returns: Response indicating success or failure.
		'''
		return HostControlResponse(self._instance.WriteIO(startAddress, data))

	def read_variable(self, variableType: HostControlVariableType, variableNumber: int) -> HostControlVariableData:
		'''Reads a variable value from the robot controller.

		:param variableType: The type of variable to read.
		:param variableNumber: The variable number/index.
		:returns: Variable data containing the value.
		'''
		return HostControlVariableData(self._instance.ReadVariable(host_control_variable_type(int(variableType)), variableNumber))

	def get_job_directory(self, jobNameFilter: str="*") -> HostControlJobDirectoryData:
		'''Reads the job directory listing from the robot controller.

		:param jobNameFilter: Job name filter (use "*" for all jobs, or specify a pattern).
		:returns: Job directory data containing the list of job names.
		'''
		return HostControlJobDirectoryData(self._instance.GetJobDirectory(jobNameFilter))

	def get_user_frame(self, userCoordinateNumber: int) -> HostControlUserFrameData:
		'''Reads user coordinate frame data from the robot controller.

		:param userCoordinateNumber: User coordinate number (2-65).
		:returns: User frame data containing the coordinate transformation.
		'''
		return HostControlUserFrameData(self._instance.GetUserFrame(userCoordinateNumber))

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
