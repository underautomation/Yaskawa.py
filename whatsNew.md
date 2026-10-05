## Ethernet Server

`robot.e_server` reads and commands the controller through its Ethernet Server, over TCP (port 80), next to the High Speed Ethernet Server. It reads the status, the alarms with their text, the positions in the base, robot, user or tool frame, the torque and the encoder temperatures. It switches the servo, holds the robot, selects the cycle and the mode, lists, selects and starts the jobs, waits for the end of a job in one call, moves the robot, and reads and writes the B, I, D, R and S variables and the I/O. Commands that the controller refuses raise a `HostControlException`.

```python
parameters = ConnectParameters("192.168.0.1")
parameters.e_server.enable = True

robot = YaskawaRobot()
robot.connect(parameters)

robot.e_server.select_job("PICK", 0)
robot.e_server.set_servo(True)
robot.e_server.start_job()
completed = robot.e_server.wait_for_job_completion(60)
```

`EServerClient` is the standalone client.

## FTP

`robot.ftp` transfers files with the FTP server of the controller (port 21): list the folders, download and upload text, bytes, local files or several files at once, test and delete files, with a progress callback. `FtpConnectParameters` sets the account (`anonymous`, `ftp` or `rcmaster`). Each failure raises an `FtpException` with the reason (`AccessDenied`, `JobAlreadyExists`...). `FtpClient` is the standalone client. The FTP client is based on FluentFTP 39.4.0 (MIT), listed in `THIRD-PARTY-NOTICES.txt`.

```python
parameters = ConnectParameters("192.168.0.1")
parameters.ftp.enable = True
parameters.ftp.ftp_user = "ftp"

robot = YaskawaRobot()
robot.connect(parameters)

robot.ftp.download_files_to_local(["/JOB/TEST.JBI", "/DAT/VAR.DAT"], r"C:\Backup")
robot.ftp.upload_file_from_local(r"C:\Jobs\PICK.JBI")
```

On a YRC1000micro, FTP downloads `ALL.PRM` (1.4 MB) in about 13 s, against about 45 s with the High Speed Ethernet Server.

## HTTP

`robot.http` reads the web server of the controller (port 80): `get_file_list(FileExtension.DAT)` lists the files of a type with their description, `get_file("TEST.JBI")` returns the text of a file. No account and no remote mode are needed. `HttpClient` is the standalone client.

## Offline kinematics

`KinematicsUtils.forward_kinematics` computes the flange position from joint angles in degrees, and `KinematicsUtils.inverse_kinematics` returns every joint solution for a position: up to 8 for the arms with a spherical wrist, up to 16 for the cobots with a wrist offset (HC10, HC10DT, HC20SDT...). The geometry is a `DhParameters`: from the catalog of 169 models (`ArmKinematicModels`), from the `ALL.PRM` file of a controller (`DhParameters.from_prm_file`, `from_prm_content`), or from your own values. The computation runs on the PC, without a controller.

```python
dh = DhParameters.from_arm_kinematic_model(ArmKinematicModels.GP7)
flange = KinematicsUtils.forward_kinematics(JointsAngles(0, 0, 0, 0, -90, 0), dh)
solutions = KinematicsUtils.inverse_kinematics(CartesianPosition(400, 100, 300, 180, 0, 0), dh)
```

## Common interfaces

The High Speed Ethernet Server and the Ethernet Server clients have the same method names for the common functions: `get_status_information()`, `get_robot_cartesian_position()`, `set_servo()`, `read_integer()`... A function written for one protocol works with the other. The interfaces of `underautomation.yaskawa.common` (`IRobotClient`, `IFileManager`...) describe these functions.

## Servo, hold and cycle

`robot.high_speed_e_server` has `set_servo(bool)`, `set_hold(bool)`, `set_teach_pendant_lock_state(bool)` and `set_cycle(RobotCycleType)`, with the same names as the Ethernet Server. `servo_command` and `switching_command` still work and are marked obsolete in .NET. Replace `servo_command(OnOffCommandType.Servo, True)` by `set_servo(True)`, and `switching_command(SwitchingCommands.Cycle)` by `set_cycle(RobotCycleType.OneCycle)`.

## Position variables

`read_position_variable`, `read_base_position` and `read_external_position` set `is_defined` to `False` for a variable that was never taught. `to_cartesian()` of a position variable converts a Cartesian position to mm and degrees.

## Package information

The PyPI page links to the release notes and to the issues of `Yaskawa.py`. The package declares Python 3.7 to 3.13, the versions supported by pythonnet 3.0.5. Python 3.14 is not supported yet.

## Linux and macOS

The README gives the right command to use the .NET runtime: `export PYTHONNET_RUNTIME=coreclr`, before you start Python. Without `export`, the variable does not reach Python and pythonnet uses Mono.

## Overloads

The methods that have several overloads in .NET accept each of them in Python. For example, `read_io(1001, 2)` reads with the number of the first group, `read_io(IOType.GeneralOutput, 1, 2)` with the I/O type, and `get_position_error()`, `get_torque()` and `get_system_information()` read the first robot without argument. The calls of the previous versions keep working, with one exception: `connect` also takes the IP address (`robot.connect("192.168.0.1")`), and its argument is now named `ip_or_parameters`. Pass the `ConnectParameters` by position: `robot.connect(parameters)`, not `robot.connect(parameters=parameters)`.

## Callbacks

`load_file` and `get_file` take a Python function for the progress, for example `get_file("JOB.JBI", lambda progress: print(progress.downloaded_bytes))`. The function receives a `LoadFileProgress` or a `GetFileProgress`.

## Enumerations in constructors

The constructors convert the Python enumerations: `RobotControlGroup(ControlGroup.RobotPulseValue, 2)` and the constructor of `RobotPosture` with its 13 arguments work with the enumerations of the package.

## Fixes

- `RobotControlGroup(ControlGroup.StationPulseValue, 1)` now reads the first station, and `get_management_time(ManagementTimeType.MotionTimeS1ToS24, n)` the station `n`. Before, they read the next station.
- `get_configuration_information()` now returns the names of the axes.
- The progress of `load_file` now ends at the size of the file.
