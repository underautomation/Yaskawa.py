# Yaskawa Robot Communication SDK for Python

[![UnderAutomation Yaskawa communication SDK](https://raw.githubusercontent.com/underautomation/Yaskawa.NET/refs/heads/main/.github/assets/banner.png)](https://underautomation.com/yaskawa)

[![PyPI](https://img.shields.io/pypi/v/UnderAutomation.Yaskawa?label=PyPI&logo=pypi)](https://pypi.org/project/UnderAutomation.Yaskawa/)
[![PyPI downloads](https://img.shields.io/pypi/dm/UnderAutomation.Yaskawa?label=Downloads&logo=pypi)](https://pypi.org/project/UnderAutomation.Yaskawa/)
[![Python](https://img.shields.io/badge/Python-3.7_to_3.13-blue)](#compatibility)
[![Platforms](https://img.shields.io/badge/OS-Windows_Linux_macOS-informational)](#compatibility)
[![License](https://img.shields.io/badge/license-commercial-blue)](https://underautomation.com/yaskawa/eula)

**UnderAutomation.Yaskawa** is a Python package that communicates with Yaskawa Motoman robot controllers
(**YRC1000 (micro)**, **MOTOMAN NEXT**, **DX100 / DX200**, **FS100**, **ERC / XRC / MRC**) through the **High Speed Ethernet Server** (HSES) of the
controller, over UDP. Nothing is installed on the controller, no Yaskawa option is needed.

Use it to read the status, the alarms and the positions, move the robot, select and start jobs, read and
write variables and I/O, and transfer files, from a Python script.

- Product page: [underautomation.com/yaskawa](https://underautomation.com/yaskawa)
- Documentation: [underautomation.com/yaskawa/documentation/get-started-python](https://underautomation.com/yaskawa/documentation/get-started-python)
- Also available for .NET: [Yaskawa.NET](https://github.com/underautomation/Yaskawa.NET), and LabVIEW: [Yaskawa.vi](https://github.com/underautomation/Yaskawa.vi).

## How it works

The package wraps the .NET library `UnderAutomation.Yaskawa.dll` with [pythonnet](https://github.com/pythonnet/pythonnet).
The DLL is inside the package: `pip install` installs everything, including pythonnet.

- **Windows:** the DLL runs on the .NET Framework 4.x of Windows. Nothing else to install.
- **Linux and macOS:** install the .NET runtime (for example .NET 8), then tell pythonnet to use it before
  you start Python:

  ```bash
  sudo apt-get install -y dotnet-runtime-8.0   # Ubuntu, for example
  export PYTHONNET_RUNTIME=coreclr
  ```

  Without this variable, pythonnet uses Mono, its default runtime on Linux and macOS. You can also choose
  the runtime in your code, before the first import of the package:

  ```python
  from pythonnet import load
  load("coreclr")
  ```

## Installation

Python 3.7 to 3.13 is supported (the limit of pythonnet 3.0.5). Install the package in a virtual
environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux and macOS
source .venv/bin/activate

pip install UnderAutomation.Yaskawa
```

Or install it from the sources of this repository:

```bash
git clone https://github.com/underautomation/Yaskawa.py.git
cd Yaskawa.py
pip install -e .
```

## Getting started

```python
from underautomation.yaskawa.yaskawa_robot import YaskawaRobot
from underautomation.yaskawa.connect_parameters import ConnectParameters

# The SDK runs in trial mode for 30 days. Register your key to remove the trial limit.
# YaskawaRobot.register_license("Your Company", "your-license-key")

robot = YaskawaRobot()
robot.connect(ConnectParameters("192.168.0.1"))

status = robot.high_speed_e_server.get_status_information()
print("Servo on:", status.servo_on, "Alarm:", status.alarming)

robot.disconnect()
```

`ConnectParameters` also gives the ping before the connection (`ping_before_connect`, True by default),
and the ports and timeouts of the High Speed Ethernet Server (`high_speed_e_server.data_port`,
`high_speed_e_server.data_timeout_milliseconds`...).

## From .NET names to Python names

The Python API is the .NET API with Python names. The [.NET documentation](https://underautomation.com/yaskawa/documentation)
applies to Python.

| .NET | Python |
| --- | --- |
| Method `GetStatusInformation()` | `get_status_information()` |
| Property `HighSpeedEServer` | `high_speed_e_server` |
| Static method `YaskawaRobot.RegisterLicense(...)` | `YaskawaRobot.register_license(...)` |
| Enum value `AlarmResetType.Reset` | `AlarmResetType.Reset` (an `IntEnum`) |
| Array `short[]` | list-like object, use `list(...)` to copy it |
| `Nullable<int>` | `int \| None` |

Each type is in the module named after it, in snake case:
`UnderAutomation.Yaskawa.HighSpeedEServer.AlarmResetType` is
`underautomation.yaskawa.high_speed_e_server.alarm_reset_type.AlarmResetType`.

## Features

Everything is reached through `robot.high_speed_e_server`.

### Status and alarms

```python
from underautomation.yaskawa.high_speed_e_server.robot_recent_alarm import RobotRecentAlarm
from underautomation.yaskawa.high_speed_e_server.alarm_reset_type import AlarmResetType

status = robot.high_speed_e_server.get_status_information()
print(status.teach, status.play, status.running)

alarm = robot.high_speed_e_server.get_alarm(RobotRecentAlarm.Latest)
print(alarm.code, alarm.text, alarm.occurring_time)

robot.high_speed_e_server.alarm_reset(AlarmResetType.Reset)
```

### Positions

```python
position = robot.high_speed_e_server.get_robot_cartesian_position()
print(position.x, position.y, position.z, position.rx, position.ry, position.rz)

joints = robot.high_speed_e_server.get_robot_joint_position()
print(list(joints.axes))  # pulses of each axis
```

### Motion

The robot must be in remote mode, see "Configure the robot" below.

```python
from underautomation.yaskawa.high_speed_e_server.on_off_command_type import OnOffCommandType
from underautomation.yaskawa.high_speed_e_server.position_command_classification import PositionCommandClassification
from underautomation.yaskawa.high_speed_e_server.position_command_operation_coordinate import PositionCommandOperationCoordinate

robot.high_speed_e_server.servo_command(OnOffCommandType.Servo, True)

# Cartesian move: mm and degrees, speed in mm/s, in the robot coordinate system
robot.high_speed_e_server.move_cartesian(
    1000, 10, 0, 0, 0, 0,
    PositionCommandClassification.Cartesian_MM_S, 10,
    PositionCommandOperationCoordinate.Robot)

# Joint move: pulses of each axis, speed in % of the maximum speed
robot.high_speed_e_server.move_joints([1000, 0, 0, 0, 0, 0], PositionCommandClassification.LinkPercent, 10)
```

### Jobs

```python
robot.high_speed_e_server.select_job("PROGRAM", 0)
robot.high_speed_e_server.start_job()

job = robot.high_speed_e_server.get_executing_job_information()
print(job.name, job.line, job.step)
```

### Variables

```python
registers = robot.high_speed_e_server.read_register(0, 5)
print(list(registers.value))

robot.high_speed_e_server.write_register(0, [100, 200])

reals = robot.high_speed_e_server.read_real(0, 4)
strings = robot.high_speed_e_server.read16_bytes_char(0, 2)
positions = robot.high_speed_e_server.read_position_variable(1, 4)
```

### Files

```python
files = robot.high_speed_e_server.get_file_list("*.JBI").files
print(list(files))

content = robot.high_speed_e_server.get_file("PROGRAM.JBI").content
```

## Examples

The folder [`examples`](examples) contains scripts ready to run. The first run asks the IP address of the
robot and saves it in `examples/robot_config.json` (ignored by git). The shared helper
[`examples/__init__.py`](examples/__init__.py) sets the Python path, manages this file and registers the
license.

Run a script from the root of the repository, or browse them with the launcher:

```bash
python examples/high_speed_e_server/hses_get_status.py
python examples/launcher.py
```

| Script | What it does |
| --- | --- |
| [`hses_get_status.py`](examples/high_speed_e_server/hses_get_status.py) | Status of the controller: mode, servo, alarm, hold. |
| [`hses_get_cartesian_position.py`](examples/high_speed_e_server/hses_get_cartesian_position.py) | Cartesian position (X, Y, Z, Rx, Ry, Rz). |
| [`hses_get_joint_position.py`](examples/high_speed_e_server/hses_get_joint_position.py) | Joint position, in pulses. |
| [`hses_read_alarms.py`](examples/high_speed_e_server/hses_read_alarms.py) | Last alarms with their code, type and text. |
| [`hses_alarm_reset.py`](examples/high_speed_e_server/hses_alarm_reset.py) | Resets the alarm or cancels the error. |
| [`hses_get_executing_job.py`](examples/high_speed_e_server/hses_get_executing_job.py) | Name, line and speed override of the executing job. |
| [`hses_select_start_job.py`](examples/high_speed_e_server/hses_select_start_job.py) | Selects a job by name and starts it. |
| [`hses_read_write_registers.py`](examples/high_speed_e_server/hses_read_write_registers.py) | Reads and writes registers. |
| [`hses_read_write_integers.py`](examples/high_speed_e_server/hses_read_write_integers.py) | Reads and writes integer variables. |
| [`hses_read_write_reals.py`](examples/high_speed_e_server/hses_read_write_reals.py) | Reads and writes real variables. |
| [`hses_read_write_bytes.py`](examples/high_speed_e_server/hses_read_write_bytes.py) | Reads and writes byte variables. |
| [`hses_read_write_strings.py`](examples/high_speed_e_server/hses_read_write_strings.py) | Reads and writes string variables (16 and 32 bytes). |
| [`hses_read_write_io.py`](examples/high_speed_e_server/hses_read_write_io.py) | Reads and writes I/O signals (general, external, network). |
| [`hses_read_write_position_variables.py`](examples/high_speed_e_server/hses_read_write_position_variables.py) | Reads and writes position variables. |
| [`hses_move_cartesian.py`](examples/high_speed_e_server/hses_move_cartesian.py) | Moves the robot to a Cartesian position. |
| [`hses_move_joints.py`](examples/high_speed_e_server/hses_move_joints.py) | Moves the robot to joint pulse values. |
| [`hses_servo_command.py`](examples/high_speed_e_server/hses_servo_command.py) | Servo on and off. |
| [`hses_display_message.py`](examples/high_speed_e_server/hses_display_message.py) | Shows a message on the pendant. |
| [`hses_get_system_info.py`](examples/high_speed_e_server/hses_get_system_info.py) | Software version and name of the system. |
| [`hses_position_error_torque.py`](examples/high_speed_e_server/hses_position_error_torque.py) | Position error and torque of each axis. |
| [`hses_file_operations.py`](examples/high_speed_e_server/hses_file_operations.py) | Lists, downloads, uploads and deletes files. |
| [`license_info_example.py`](examples/license/license_info_example.py) | State of the license, and registration of a key. |

The motion examples move the robot. Check the surroundings of the robot first.

## Configure the robot

The read functions work in any mode. The commands (servo, motion, job start, file write) need these
settings on the controller, in Security mode. The [Yaskawa.NET README](https://github.com/underautomation/Yaskawa.NET#configure-the-robot)
shows them with screenshots.

- **Remote commands:** `IN/OUT` > `PSEUDO INPUT SIGNAL`, select `#82015 CMD REMOTE SEL` with
  `INTER LOCK` + `SELECT`.
- **Key in the remote position:** the commands need the key of the pendant in the remote position. With
  the ladder editor, copy `#80011` to `#40042`.
- **Job selection:** `SETUP` > `FUNCTION ENABLE`, set `JOB SELECT WHEN REMOTE AND PLAY` to `PERMIT`.
- **File overwrite:** `PARAMETER` > `RS`, set `RS029` to `1` and `RS214` to `1`.

## Compatibility

- **Python:** 3.7 to 3.13, with pythonnet 3.0.5.
- **Operating systems:** Windows (.NET Framework), Linux and macOS (.NET runtime and `export PYTHONNET_RUNTIME=coreclr`).
- **Controllers:** Yaskawa YRC1000 (micro), MOTOMAN NEXT, DX100 / DX200, FS100, ERC / XRC / MRC, with the High Speed Ethernet Server.

## License

This SDK needs a commercial license. A 30-day trial starts at the first use, no key needed. After the
trial, register your key in your code:

```python
from underautomation.yaskawa.yaskawa_robot import YaskawaRobot

license_info = YaskawaRobot.register_license("Your Company", "your-license-key")
print(license_info.state)
```

- License agreement: [underautomation.com/yaskawa/eula](https://underautomation.com/yaskawa/eula) and [License.md](License.md)
- Trial key: [underautomation.com/license](https://underautomation.com/license?sdk=yaskawa)
- Prices and quote: [underautomation.com/yaskawa](https://underautomation.com/yaskawa)

## Support

- Documentation: [underautomation.com/yaskawa/documentation](https://underautomation.com/yaskawa/documentation)
- Issues: [GitHub Issues](https://github.com/underautomation/Yaskawa.py/issues)
- Contact: [underautomation.com/contact](https://underautomation.com/contact)
