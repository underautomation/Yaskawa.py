import typing
from underautomation.yaskawa.high_speed_e_server.robot_alarm_data import RobotAlarmData
from underautomation.yaskawa.high_speed_e_server.robot_recent_alarm import RobotRecentAlarm
from underautomation.yaskawa.high_speed_e_server.robot_status_data import RobotStatusData
from underautomation.yaskawa.high_speed_e_server.robot_job_data import RobotJobData
from underautomation.yaskawa.high_speed_e_server.robot_job_stack_data import RobotJobStackData
from underautomation.yaskawa.high_speed_e_server.robot_axis_config_data import RobotAxisConfigData
from underautomation.yaskawa.high_speed_e_server.robot_control_group import RobotControlGroup
from underautomation.yaskawa.high_speed_e_server.robot_position_cartesian_data import RobotPositionCartesianData
from underautomation.yaskawa.high_speed_e_server.robot_position_int_data import RobotPositionIntData
from underautomation.yaskawa.high_speed_e_server.robot_axis_int_data import RobotAxisIntData
from underautomation.yaskawa.high_speed_e_server.robot_data_header import RobotDataHeader
from underautomation.yaskawa.high_speed_e_server.alarm_reset_type import AlarmResetType
from underautomation.yaskawa.high_speed_e_server.on_off_command_type import OnOffCommandType
from underautomation.yaskawa.high_speed_e_server.switching_commands import SwitchingCommands
from underautomation.yaskawa.high_speed_e_server.robot_management_time_data import RobotManagementTimeData
from underautomation.yaskawa.high_speed_e_server.management_time_type import ManagementTimeType
from underautomation.yaskawa.high_speed_e_server.robot_system_information import RobotSystemInformation
from underautomation.yaskawa.high_speed_e_server.robot_system_type_data import RobotSystemTypeData
from underautomation.yaskawa.high_speed_e_server.robot_system_param_data import RobotSystemParamData
from underautomation.yaskawa.high_speed_e_server.system_parameter_types import SystemParameterTypes
from underautomation.yaskawa.high_speed_e_server.robot_io_data import RobotIOData
from underautomation.yaskawa.common.io_type import IOType
from underautomation.yaskawa.high_speed_e_server.robot_register_data import RobotRegisterData
from underautomation.yaskawa.high_speed_e_server.robot_byte_variable_data import RobotByteVariableData
from underautomation.yaskawa.high_speed_e_server.robot_integer_variable_data import RobotIntegerVariableData
from underautomation.yaskawa.high_speed_e_server.robot_double_integer_variable_data import RobotDoubleIntegerVariableData
from underautomation.yaskawa.high_speed_e_server.robot_real_variable_data import RobotRealVariableData
from underautomation.yaskawa.high_speed_e_server.robot_string_variable_data import RobotStringVariableData
from underautomation.yaskawa.high_speed_e_server.robot_position_variable_data import RobotPositionVariableData
from underautomation.yaskawa.high_speed_e_server.robot_base_position_variable_data import RobotBasePositionVariableData
from underautomation.yaskawa.high_speed_e_server.robot_base_position_data import RobotBasePositionData
from underautomation.yaskawa.high_speed_e_server.robot_external_axis_variable_data import RobotExternalAxisVariableData
from underautomation.yaskawa.high_speed_e_server.robot_external_axis_data import RobotExternalAxisData
from underautomation.yaskawa.high_speed_e_server.robot_axis_raw_data_1 import RobotAxisRawData1
from underautomation.yaskawa.high_speed_e_server.robot_alarm_data_extended import RobotAlarmDataExtended
from underautomation.yaskawa.high_speed_e_server.position_command_classification import PositionCommandClassification
from underautomation.yaskawa.high_speed_e_server.position_command_operation_coordinate import PositionCommandOperationCoordinate
from underautomation.yaskawa.high_speed_e_server.robot_posture import RobotPosture
from underautomation.yaskawa.high_speed_e_server.position_command_type import PositionCommandType
from underautomation.yaskawa.high_speed_e_server.robot_file_list_data import RobotFileListData
from underautomation.yaskawa.high_speed_e_server.robot_file_content_data import RobotFileContentData
from UnderAutomation.Yaskawa.HighSpeedEServer.Internal import HighSpeedEServerClientBase as high_speed_e_server_client_base
from UnderAutomation.Yaskawa.HighSpeedEServer import RobotRecentAlarm as robot_recent_alarm
from UnderAutomation.Yaskawa.HighSpeedEServer import AlarmResetType as alarm_reset_type
from UnderAutomation.Yaskawa.HighSpeedEServer import OnOffCommandType as on_off_command_type
from UnderAutomation.Yaskawa.HighSpeedEServer import SwitchingCommands as switching_commands
from UnderAutomation.Yaskawa.HighSpeedEServer import ManagementTimeType as management_time_type
from UnderAutomation.Yaskawa.HighSpeedEServer import SystemParameterTypes as system_parameter_types
from UnderAutomation.Yaskawa.Common import IOType as io_type
from UnderAutomation.Yaskawa.HighSpeedEServer import PositionCommandClassification as position_command_classification
from UnderAutomation.Yaskawa.HighSpeedEServer import PositionCommandOperationCoordinate as position_command_operation_coordinate
from UnderAutomation.Yaskawa.HighSpeedEServer import PositionCommandType as position_command_type

class HighSpeedEServerClientBase:
	'''Base class implementing the High Speed Ethernet Server protocol for Yaskawa robot communication. Provides methods for reading robot status, positions, variables, and executing commands via UDP.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = high_speed_e_server_client_base()
		else:
			self._instance = _internal

	def close(self) -> None:
		'''Closes the connection to the robot controller and releases network resources.'''
		self._instance.Close()

	def get_alarm(self, alarm: RobotRecentAlarm) -> RobotAlarmData:
		'''Reads alarm information from the robot controller. Retrieves alarm code, type, occurrence time, and descriptive text.

		:param alarm: Which alarm to retrieve from the alarm history (latest, second latest, etc.).
		:returns: Alarm data containing code, type, time, and message text.
		'''
		return RobotAlarmData(self._instance.GetAlarm(robot_recent_alarm(int(alarm))))

	def get_status_information(self) -> RobotStatusData:
		'''Reads the current operational status of the robot controller. Returns information about mode (teach/play), running state, hold status, alarms, and servo power.

		:returns: Status data containing boolean flags for various robot states.
		'''
		return RobotStatusData(self._instance.GetStatusInformation())

	def get_executing_job_information(self) -> RobotJobData:
		'''Reads information about the currently selected and executing job (program). Returns job name, current line, step, and speed override percentage.

		:returns: Job data containing name, line number, step, and speed override.
		'''
		return RobotJobData(self._instance.GetExecutingJobInformation())

	def get_job_stack(self, taskNumber: int=0) -> RobotJobStackData:
		'''Reads the job call stack for a specific task on the robot controller. Returns the current nesting of CALL instructions, from the outermost job to the currently executing one.

		:param taskNumber: Task number to query 0 for Master Job, 1 to 15 for sub-tasks. Default: 0 (Master Job).
		:returns: Job stack data containing the array of job names, outermost first.
		'''
		return RobotJobStackData(self._instance.GetJobStack(taskNumber))

	def get_configuration_information(self, type: RobotControlGroup) -> RobotAxisConfigData:
		'''Reads axis configuration information for a specified control group. Returns axis type names (e.g., "S", "L", "U", "R", "B", "T") for each axis.

		:param type: Control group to query (robot, base, station).
		:returns: Axis configuration data with axis type names.
		'''
		return RobotAxisConfigData(self._instance.GetConfigurationInformation(type._instance if type else None))

	def get_robot_cartesian_position(self) -> RobotPositionCartesianData:
		'''Reads the current robot Cartesian position (TCP position and orientation). Coordinates are returned in millimeters for X, Y, Z and degrees for Rx, Ry, Rz.

		:returns: Cartesian position data with coordinates in mm and degrees.
		'''
		return RobotPositionCartesianData(self._instance.GetRobotCartesianPosition())

	def get_robot_joint_position(self) -> RobotPositionIntData:
		'''Reads the current robot joint position in pulse (encoder) values. Returns raw pulse values for all robot axes.

		:returns: Joint position data with axis values in encoder pulses.
		'''
		return RobotPositionIntData(None, self._instance.GetRobotJointPosition())

	def get_robot_position(self, type: RobotControlGroup) -> RobotPositionIntData:
		'''Reads position data for a specified control group. Can read robot, base, or station position data depending on the control group specified.

		:param type: Control group to query.
		:returns: Position data with axis values (format depends on control group type).
		'''
		return RobotPositionIntData(None, self._instance.GetRobotPosition(type._instance if type else None))

	def get_position_error(self, type: RobotControlGroup) -> RobotAxisIntData:
		'''Reads the position error for a specified control group. Position error indicates the difference between commanded and actual position.

		:param type: Control group to query.
		:returns: Position error data with axis error values in pulses.
		'''
		return RobotAxisIntData(self._instance.GetPositionError(type._instance if type else None))

	def get_torque(self, type: RobotControlGroup) -> RobotAxisIntData:
		'''Reads the current torque values for a specified control group's servo motors. Torque values indicate motor load as a percentage of rated torque.

		:param type: Control group to query.
		:returns: Torque data with axis torque values.
		'''
		return RobotAxisIntData(self._instance.GetTorque(type._instance if type else None))

	def alarm_reset(self, type: AlarmResetType) -> RobotDataHeader:
		'''Resets alarms or cancels errors on the robot controller. Use Reset to clear alarm conditions after resolving the cause. Use Cancel for recoverable errors that don't require alarm reset.

		:param type: Type of reset operation (Reset or Cancel).
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.AlarmReset(alarm_reset_type(int(type))))

	def servo_command(self, command: OnOffCommandType, value: bool) -> RobotDataHeader:
		'''Executes hold/servo/HLock on/off commands. For servo control, this enables or disables motor power to the robot. Servo must be ON for the robot to move.

		:param command: Type of command (Hold, Servo, or HLock).
		:param value: True to enable (ON), false to disable (OFF).
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.ServoCommand(on_off_command_type(int(command)), value))

	def switching_command(self, command: SwitchingCommands) -> RobotDataHeader:
		'''Switches the robot execution mode between Step, Cycle, and Continuous.

		:param command: Target execution mode.
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.SwitchingCommand(switching_commands(int(command))))

	def display(self, message: str) -> RobotDataHeader:
		'''Displays a popup message on the robot programming pendant. Message will appear as a notification to the operator.

		:param message: Message text to display (maximum 24 characters).
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.Display(message))

	def start_job(self) -> RobotDataHeader:
		'''Starts execution of the currently selected job. The job must be selected first using SelectJob before calling this method. Servo must be ON and the robot must not be in alarm state.

		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.StartJob())

	def select_job(self, job: str, line: int) -> RobotDataHeader:
		'''Selects a job for execution and optionally positions to a specific line. Call StartJob after selecting to begin execution.

		:param job: Job name (maximum 32 characters, typically ends with .JBI extension).
		:param line: Line number within the job to position to (1-based). Use 0 for beginning.
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.SelectJob(job, line))

	def get_management_time(self, type: ManagementTimeType, index: int=0) -> RobotManagementTimeData:
		'''Retrieves management time statistics from the robot controller. Can query various timing metrics like control power ON time, servo ON time, etc.

		:param type: Type of management time to retrieve (ControlPowerOnTime, ServoPowerOnTime, etc.).
		:param index: Index for job-specific timing (0 for main job, or job index).
		:returns: Management time data including start time and elapsed time strings.
		'''
		return RobotManagementTimeData(self._instance.GetManagementTime(management_time_type(int(type)), index))

	def get_system_information(self, type: RobotSystemTypeData) -> RobotSystemInformation:
		'''Retrieves system information for a specific robot system or control group. Use for multi-robot controllers or to query specific axes groups.

		:param type: Robot system type specifier (e.g., R1, R2, S1, etc.).
		:returns: System information including software version, robot name, and parameter file.
		'''
		return RobotSystemInformation(self._instance.GetSystemInformation(type._instance if type else None))

	def get_system_parameter(self, type: SystemParameterTypes, number: int, group: int=1) -> RobotSystemParamData:
		'''Reads a system parameter from the robot controller.

		:param type: Category of the system parameter.
		:param number: Parameter number within the category.
		:param group: Group number. Leave at 0 for types that do not require a group (S2C, S3C, S4C, RS). Must be specified for types S1CG, AP, and SE.
		:returns: System parameter data containing the raw value.
		'''
		return RobotSystemParamData(self._instance.GetSystemParameter(system_parameter_types(int(type)), number, group))

	def read_io(self, type: IOType, group: int, count: int) -> RobotIOData:
		'''Reads multiple I/O bytes from the robot controller using I/O group addressing. The starting byte index is computed from the I/O type and group number.

		:param type: The I/O signal category.
		:param group: 1-based group number within the I/O type.
		:param count: Number of bytes to read (will be rounded up to nearest even number).
		:returns: Plural data containing array of I/O byte values.
		'''
		return RobotIOData(self._instance.ReadIO(io_type(int(type)), group, count))

	def write_io(self, type: IOType, group: int, data: typing.List[int]) -> RobotDataHeader:
		'''Writes I/O bytes to the robot controller using I/O group addressing. By default, only Network Input can be written The starting byte index is computed from the I/O type and group number.

		:param type: The I/O signal category.
		:param group: 1-based group number within the I/O type.
		:param data: Data array to write (must contain an even number of elements).
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.WriteIO(io_type(int(type)), group, data))

	def write_io_network_input(self, group: int, data: typing.List[int]) -> RobotDataHeader:
		'''Writes network input bytes to the robot controller

		:param group: 1-based group number within the Network Inputs.
		:param data: Data array to write (must contain an even number of elements).
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.WriteIoNetworkInput(group, data))

	def read_register(self, firstIndex: int, count: int) -> RobotRegisterData:
		'''Reads multiple 16-bit register values (M variables) from the robot controller. Registers are used for general-purpose integer storage in robot programs.

		:param firstIndex: Starting register index.
		:param count: Number of registers to read.
		:returns: Plural data containing array of 16-bit register values.
		'''
		return RobotRegisterData(self._instance.ReadRegister(firstIndex, count))

	def write_register(self, firstIndex: int, data: typing.List[int]) -> RobotDataHeader:
		'''Writes multiple 16-bit register values (M variables) to the robot controller.

		:param firstIndex: Starting register index.
		:param data: Array of 16-bit values to write.
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.WriteRegister(firstIndex, data))

	def read_byte(self, firstIndex: int, count: int) -> RobotByteVariableData:
		'''Reads multiple byte variables (B variables) from the robot controller. Byte variables are 8-bit unsigned values used for compact data storage.

		:param firstIndex: Starting byte variable index.
		:param count: Number of bytes to read (will be rounded up to nearest even number).
		:returns: Plural data containing array of byte values.
		'''
		return RobotByteVariableData(self._instance.ReadByte(firstIndex, count))

	def write_byte(self, firstIndex: int, data: typing.List[int]) -> RobotDataHeader:
		'''Writes byte variables (B variables) to the robot controller.

		:param firstIndex: Starting byte variable index.
		:param data: Data to write (must contain an even number of elements).
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.WriteByte(firstIndex, data))

	def read_integer(self, firstIndex: int, count: int) -> RobotIntegerVariableData:
		'''Reads multiple integer variables (I variables) from the robot controller. Integer variables are 16-bit signed values (-32768 to 32767).

		:param firstIndex: Starting integer variable index.
		:param count: Number of integer variables to read.
		:returns: Plural data containing array of 16-bit integer values.
		'''
		return RobotIntegerVariableData(self._instance.ReadInteger(firstIndex, count))

	def write_integer(self, firstIndex: int, data: typing.List[int]) -> RobotDataHeader:
		'''Writes integer variables (I variables) to the robot controller.

		:param firstIndex: Starting integer variable index.
		:param data: Array of 16-bit integer values to write.
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.WriteInteger(firstIndex, data))

	def read_double_integer(self, firstIndex: int, count: int) -> RobotDoubleIntegerVariableData:
		'''Reads multiple double-precision variables (D variables) from the robot controller. Note: The protocol actually transmits float values which are then cast to double.

		:param firstIndex: Starting double variable index.
		:param count: Number of double variables to read.
		:returns: Plural data containing array of double values.
		'''
		return RobotDoubleIntegerVariableData(self._instance.ReadDoubleInteger(firstIndex, count))

	def write_double_integer(self, firstIndex: int, data: typing.List[int]) -> RobotDataHeader:
		'''Writes double-precision variables (D variables) to the robot controller.

		:param firstIndex: Starting double variable index.
		:param data: Array of double values to write.
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.WriteDoubleInteger(firstIndex, data))

	def read_real(self, firstIndex: int, count: int) -> RobotRealVariableData:
		'''Reads multiple real (single-precision float) variables (R variables) from the robot controller. Real variables are 32-bit IEEE 754 floating-point values.

		:param firstIndex: Starting real variable index.
		:param count: Number of real variables to read.
		:returns: Plural data containing array of float values.
		'''
		return RobotRealVariableData(self._instance.ReadReal(firstIndex, count))

	def write_real(self, firstIndex: int, data: typing.List[float]) -> RobotDataHeader:
		'''Writes real (single-precision float) variables (R variables) to the robot controller.

		:param firstIndex: Starting real variable index.
		:param data: Array of float values to write.
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.WriteReal(firstIndex, data))

	def read16_bytes_char(self, firstIndex: int, count: int) -> RobotStringVariableData:
		'''Reads multiple 16-byte string variables (S variables) from the robot controller. String variables are fixed-length, null-terminated ASCII strings.

		:param firstIndex: Starting string variable index.
		:param count: Number of string variables to read.
		:returns: Plural data containing array of string values.
		'''
		return RobotStringVariableData(self._instance.Read16BytesChar(firstIndex, count))

	def write16_bytes_char(self, firstIndex: int, data: typing.List[str]) -> RobotDataHeader:
		'''Writes 16-byte string variables (S variables) to the robot controller. Strings longer than 16 characters will be truncated.

		:param firstIndex: Starting string variable index.
		:param data: Array of string values to write.
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.Write16BytesChar(firstIndex, data))

	def read_position_variable(self, firstIndex: int, count: int) -> RobotPositionVariableData:
		'''Reads multiple position variables (P variables) from the robot controller. Position variables store complete robot poses including position, orientation, and configuration.

		:param firstIndex: Starting position variable index.
		:param count: Number of position variables to read.
		:returns: Plural data containing array of position data.
		'''
		return RobotPositionVariableData(self._instance.ReadPositionVariable(firstIndex, count))

	def write_position_variable(self, firstIndex: int, data: typing.List[RobotPositionIntData]) -> RobotDataHeader:
		'''Writes position variables (P variables) to the robot controller.

		:param firstIndex: Starting position variable index.
		:param data: Array of position data to write.
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.WritePositionVariable(firstIndex, [x._instance if x else None for x in data]))

	def read_base_position(self, firstIndex: int, count: int) -> RobotBasePositionVariableData:
		'''Reads multiple base position variables (BP variables) from the robot controller. Base position variables define reference coordinate frames for robot operations.

		:param firstIndex: Starting base position variable index.
		:param count: Number of base position variables to read.
		:returns: Plural data containing array of base position data.
		'''
		return RobotBasePositionVariableData(self._instance.ReadBasePosition(firstIndex, count))

	def write_base_position(self, firstIndex: int, data: typing.List[RobotBasePositionData]) -> RobotDataHeader:
		'''Writes base position variables (BP variables) to the robot controller.

		:param firstIndex: Starting base position variable index.
		:param data: Array of base position data to write.
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.WriteBasePosition(firstIndex, [x._instance if x else None for x in data]))

	def read_external_position(self, firstIndex: int, count: int) -> RobotExternalAxisVariableData:
		'''Reads multiple external axis variables (EX variables) from the robot controller. External axis variables store positions for additional axes beyond the main robot arm.

		:param firstIndex: Starting external axis variable index.
		:param count: Number of external axis variables to read.
		:returns: Plural data containing array of external axis position data.
		'''
		return RobotExternalAxisVariableData(self._instance.ReadExternalPosition(firstIndex, count))

	def write_external_position(self, firstIndex: int, data: typing.List[RobotAxisRawData1]) -> RobotDataHeader:
		return RobotDataHeader(self._instance.WriteExternalPosition(firstIndex, [x._instance if x else None for x in data]))

	def get_alarm_extended(self, alarm: RobotRecentAlarm) -> RobotAlarmDataExtended:
		'''Retrieves extended alarm information including sub-code character strings. Provides more detailed information than GetAlarm for troubleshooting.

		:param alarm: Alarm index to retrieve (Alarm1 through Alarm4).
		:returns: Extended alarm data including code, timing, text description, and additional information.
		'''
		return RobotAlarmDataExtended(self._instance.GetAlarmExtended(robot_recent_alarm(int(alarm))))

	def move_cartesian(self, x: float, y: float, z: float, rx: float, ry: float, rz: float, classification: PositionCommandClassification, speed: float, coordinate: PositionCommandOperationCoordinate, posture: RobotPosture=None, commandtype: PositionCommandType=PositionCommandType.StraightIncrement, RobotControlGroup: int=1, StationControlGroup: int=0, tool: int=0, userCoordinate: int=0) -> RobotDataHeader:
		'''Commands the robot to move to a Cartesian position (X, Y, Z, Rx, Ry, Rz). Movement is relative to the specified coordinate system.

		:param x: X coordinate in millimeters.
		:param y: Y coordinate in millimeters.
		:param z: Z coordinate in millimeters.
		:param rx: Rotation around X axis in degrees.
		:param ry: Rotation around Y axis in degrees.
		:param rz: Rotation around Z axis in degrees.
		:param classification: Speed unit classification (percent or linear speed).
		:param speed: Movement speed in the specified units.
		:param coordinate: Coordinate system for the movement (Base, Robot, User, Tool).
		:param posture: Robot posture/configuration (RCONF) for the target position. Null for default.
		:param commandtype: Type of motion command (increment, absolute, etc.).
		:param RobotControlGroup: Robot control group number (typically 1 for main robot).
		:param StationControlGroup: Station control group number (0 if not applicable).
		:param tool: Tool center point number to use.
		:param userCoordinate: User coordinate number (for User coordinate system).
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.MoveCartesian(x, y, z, rx, ry, rz, position_command_classification(int(classification)), speed, position_command_operation_coordinate(int(coordinate)), posture._instance if posture else None, position_command_type(int(commandtype)), RobotControlGroup, StationControlGroup, tool, userCoordinate))

	def move_joints(self, axesPulse: typing.List[int], classification: PositionCommandClassification, speed: float, commandtype: PositionCommandType=PositionCommandType.StraightIncrement, RobotControlGroup: int=1, StationControlGroup: int=1, tool: int=0) -> RobotDataHeader:
		'''Commands the robot to move using joint (pulse) positions. This specifies the position of each axis directly in encoder pulses.

		:param axesPulse: Array of axis positions in encoder pulses (up to 8 axes).
		:param classification: Speed unit classification (percent or angular speed).
		:param speed: Movement speed in the specified units.
		:param commandtype: Type of motion command (increment, absolute, etc.).
		:param RobotControlGroup: Robot control group number (typically 1 for main robot).
		:param StationControlGroup: Station control group number (typically 1 for station axes).
		:param tool: Tool center point number to use.
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.MoveJoints(axesPulse, position_command_classification(int(classification)), speed, position_command_type(int(commandtype)), RobotControlGroup, StationControlGroup, tool))

	def read32_bytes_char(self, firstIndex: int, count: int) -> RobotStringVariableData:
		'''Reads multiple 32-byte string variables (S variables) from the robot controller (DX200 only). Extended string variables for longer text storage than 16-byte variants.

		:param firstIndex: Starting string variable index.
		:param count: Number of string variables to read.
		:returns: Plural data containing array of string values.
		'''
		return RobotStringVariableData(self._instance.Read32BytesChar(firstIndex, count))

	def write32_bytes_char(self, firstIndex: int, data: typing.List[str]) -> RobotDataHeader:
		'''Writes 32-byte string variables (S variables) to the robot controller. Strings longer than 32 characters will be truncated.

		:param firstIndex: Starting string variable index.
		:param data: Array of string values to write.
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.Write32BytesChar(firstIndex, data))

	def delete_file(self, name: str) -> RobotDataHeader:
		'''Deletes a file from the robot controller's file system. Use with caution as deleted files cannot be recovered.

		:param name: File name to delete (e.g., "TEST.JBI" for a job file).
		:returns: Response header indicating success.
		'''
		return RobotDataHeader(self._instance.DeleteFile(name))

	def load_file(self, name: str, content: str, onLoadFileProgress: typing.Any=None) -> typing.List[RobotDataHeader]:
		return [RobotDataHeader(x) for x in self._instance.LoadFile(name, content, onLoadFileProgress)]

	def get_file_list(self, pattern: str) -> RobotFileListData:
		'''Retrieves a list of files matching a pattern from the robot controller. Supports wildcards for matching multiple files.

		:param pattern: File search pattern (e.g., "*.JBI" to list all job files, "*.DAT" for data files).
		:returns: File list data containing an array of matching file names.
		'''
		return RobotFileListData(self._instance.GetFileList(pattern))

	def get_file(self, name: str, onGetFileProgress: typing.Any=None) -> RobotFileContentData:
		return RobotFileContentData(self._instance.GetFile(name, onGetFileProgress))

	def batch_data_backup(self, file: str="/SPDRV/CMOSBK.BIN") -> RobotDataHeader:
		'''Performs a backup of the robot's CMOS. The CMOS.BIN file is copied locally in the robot controller to "/SPDRC/CMOSBK.BIN". The operation can take several seconds to complete. After this command, the backup file can be downloaded using GetFile("/SPDRC/CMOSBK.BIN"). To enable this command : in "MANAGEMENT MODE", select {SETUP} - {AUTO BACKUP SET} and set "DEVICE" to "RAMDISK". If this menu is not available, Reboot the controller in Maintenance Mode and set System / Setup / OPTION FUNCTION / AUTOBACKUP to "Used", then do a "Safety board flash reset" from File / Initialize

		:param file: Controller backup file path for CMOS.BIN copy
		'''
		return RobotDataHeader(self._instance.BatchDataBackup(file))

	@property
	def ip(self) -> str:
		'''Gets the IP address or hostname of the connected robot controller.'''
		return self._instance.IP

	@property
	def connected(self) -> bool:
		'''Gets a value indicating whether the client is connected to a robot controller. Note: Since UDP is connectionless, this only indicates if the socket is configured.'''
		return self._instance.Connected

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HighSpeedEServerClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
