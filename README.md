# Yaskawa Communication SDK for Python

[![UnderAutomation Yaskawa communication SDK](https://raw.githubusercontent.com/underautomation/yaskawa.NET/refs/heads/main/.github/assets/banner.png)](https://underautomation.com)

[![PyPI](https://img.shields.io/pypi/v/UnderAutomation.Yaskawa?label=PyPI&logo=pypi)](https://pypi.org/project/UnderAutomation.Yaskawa/)
[![Python](https://img.shields.io/badge/Python-3.7_|_3.8_|_3.9_|_3.10_|_3.11_|_3.12-blue?logo=python)](#)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue)](#)
[![License](https://img.shields.io/badge/License-Commercial-red)](https://underautomation.com/yaskawa/eula)

### 🤖 Effortlessly Communicate with Yaskawa Motoman Robots

The **Yaskawa SDK for Python** enables seamless integration with Yaskawa Motoman robots for automation, data exchange, and remote control through the **High-Speed Ethernet Server (HSES)** protocol.

> Whether you're building a custom application, integrating with a MES/SCADA system, or performing advanced diagnostics, this SDK provides the tools you need.

🔗 **More Information:** [https://underautomation.com/yaskawa](https://underautomation.com/yaskawa)  
🔗 Also available in **[🟦 .NET](https://github.com/underautomation/yaskawa.NET)** and **[🟨 LabVIEW](https://github.com/underautomation/yaskawa.vi)**

---

[⭐ Star this repo if it's useful to you!](https://github.com/underautomation/yaskawa.py/stargazers)  
[👁️ Watch for updates](https://github.com/underautomation/yaskawa.py/watchers)

---

## 🚀 TL;DR

- 📡 **High-Speed Ethernet Server** - real-time UDP communication
- 🤖 **Move robot** in Cartesian or joint space
- 📊 **Read robot status** - mode, servo, alarms, hold state
- 🔔 **Alarm management** - read active alarms, reset
- ⚡ **I/O control** - read/write general, external, network I/O
- 💾 **Variable access** - registers, bytes, integers, reals, strings, positions
- 🧠 **Job control** - select, start, monitor executing jobs
- 📂 **File management** - list, upload, download, delete files
- ✍️ **Pendant display** - send messages to the teach pendant
- ⏱️ **Management time** - operating time, servo time, playback time
- 🔧 **System information** - software version, configuration, parameters

> No custom robot options or additional hardware required. The SDK uses the **standard HSES protocol** available on Yaskawa controllers.

---

## 🛠 Installation & Getting Started

### Prerequisites

- **Python 3.7** or higher
- A Yaskawa Motoman robot (DX200, YRC1000, YRC1000 Micro)

### Step 1 - Create a Virtual Environment

We recommend using a virtual environment to keep your project dependencies isolated.

```bash
# Create a project folder
mkdir my-yaskawa-project
cd my-yaskawa-project

# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt, indicating the virtual environment is active.

### Step 2 - Install the SDK

The SDK is published on PyPI. Install it with a single command:

```bash
pip install UnderAutomation.Yaskawa
```

That's it! All dependencies (including `pythonnet`) are installed automatically.

On **Linux**, you should also install .NET Core and set environment variable PYTHONNET_RUNTIME to coreclr:

```bash
sudo apt-get install -y dotnet-runtime-8.0
PYTHONNET_RUNTIME=coreclr
```

> **Alternative: install from source**
>
> ```bash
> git clone https://github.com/underautomation/Yaskawa.py.git
> cd Yaskawa.py
> pip install -e .
> ```

### Step 3 - Connect to Your Robot

Create a Python file (e.g. `main.py`) and write:

```python
from underautomation.yaskawa.yaskawa_robot import YaskawaRobot
from underautomation.yaskawa.connect_parameters import ConnectParameters
from underautomation.yaskawa.high_speed_e_server.alarm_reset_type import AlarmResetType

# Create a robot instance
robot = YaskawaRobot()

# Connect (replace with your robot's IP address)
params = ConnectParameters("192.168.0.1")
params.ping_before_connect = True

# Connect to the robot
# If you get a license exception, ask a trial license here: https://underautomation.com/license
# and call YaskawaRobot.register_license(...) before connecting
robot.connect(params)

if robot.high_speed_e_server.connected:
    print("Connected!")

    # Get robot status
    status = robot.high_speed_e_server.get_status_information()
    print(f"  Servo ON   : {status.servo_on}")
    print(f"  Running    : {status.running}")
    print(f"  Mode       : {'Teach' if status.teach else 'Play'}")
    print(f"  Alarming   : {status.alarming}")

    # Get current Cartesian position
    pos = robot.high_speed_e_server.get_robot_cartesian_position()
    print(f"\nCartesian Position:")
    print(f"  X={pos.x:.3f}  Y={pos.y:.3f}  Z={pos.z:.3f}")
    print(f"  Rx={pos.rx:.3f}  Ry={pos.ry:.3f}  Rz={pos.rz:.3f}")

    # Get current joint position
    joint = robot.high_speed_e_server.get_robot_joint_position()
    print(f"\nJoint Position: {joint.axes}")

    # Read registers
    reg = robot.high_speed_e_server.read_register(0, count=5)
    print(f"\nRegisters: {reg.values}")

    # Write registers
    robot.high_speed_e_server.write_register(0, [100, 200])

    # Reset alarms
    robot.high_speed_e_server.alarm_reset(AlarmResetType.Reset)

# Don't forget to disconnect
robot.disconnect()
```

Run it:

```bash
python main.py
```

---

## 🔑 Licensing

The SDK works out of the box for **30 days** (trial period) - no registration needed.

After the trial, you can:

- **Buy a license** at [underautomation.com/order](https://underautomation.com/order?sdk=yaskawa)
- **Get a new trial period immediately by email** at [underautomation.com/license](https://underautomation.com/license?sdk=yaskawa)

To register a license in code:

```python
from underautomation.yaskawa.yaskawa_robot import YaskawaRobot

license_info = YaskawaRobot.register_license("your-licensee", "your-license-key")
print(license_info)
```

---

## 📂 Examples

The repository includes a complete set of ready-to-run examples in the [`examples/`](https://github.com/underautomation/yaskawa.py/tree/main/examples) folder, organized by category.

### How the Examples Work

| File                                                                                                   | Role                                                                                                                     |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| [`examples/launcher.py`](https://github.com/underautomation/yaskawa.py/blob/main/examples/launcher.py) | **Interactive menu** - browse and run any example from a single launcher                                                 |
| [`examples/__init__.py`](https://github.com/underautomation/yaskawa.py/blob/main/examples/__init__.py) | **Shared helpers** - sets up the Python path, manages robot connection settings, and handles license registration        |
| `examples/robot_config.json`                                                                           | **Saved settings** (git-ignored) - remembers your robot IP and license key so you don't have to re-enter them every time |

**Run any example directly:**

> The first time you run an example, it will ask for your robot IP. This is saved in `robot_config.json` so you only enter it once.

```bash
# Run any example directly
python examples/high_speed_e_server/hses_get_status.py
```

**Or browse examples with the launcher:**

Use the launcher to easily browse and run any example without needing to open each file.

```bash
# Launch the interactive menu
python examples/launcher.py
```

### 📡 High Speed Ethernet Server Examples

| Example                                                                                           | Description                                             |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| [`hses_get_status.py`](examples/high_speed_e_server/hses_get_status.py)                           | Read robot status: mode, servo, alarms, hold state      |
| [`hses_get_cartesian_position.py`](examples/high_speed_e_server/hses_get_cartesian_position.py)   | Read current TCP position (X, Y, Z, Rx, Ry, Rz)         |
| [`hses_get_joint_position.py`](examples/high_speed_e_server/hses_get_joint_position.py)           | Read current joint position (pulse values)              |
| [`hses_read_alarms.py`](examples/high_speed_e_server/hses_read_alarms.py)                         | Read active alarms with code, type, and message         |
| [`hses_alarm_reset.py`](examples/high_speed_e_server/hses_alarm_reset.py)                         | Reset alarms (standard or error reset)                  |
| [`hses_get_executing_job.py`](examples/high_speed_e_server/hses_get_executing_job.py)             | Get currently executing job name, line, and speed       |
| [`hses_select_start_job.py`](examples/high_speed_e_server/hses_select_start_job.py)               | Select a job by name and start it                       |
| [`hses_read_write_registers.py`](examples/high_speed_e_server/hses_read_write_registers.py)       | Read and write numeric registers                        |
| [`hses_read_write_integers.py`](examples/high_speed_e_server/hses_read_write_integers.py)         | Read and write integer variables                        |
| [`hses_read_write_reals.py`](examples/high_speed_e_server/hses_read_write_reals.py)               | Read and write real (float) variables                   |
| [`hses_read_write_bytes.py`](examples/high_speed_e_server/hses_read_write_bytes.py)               | Read and write byte variables                           |
| [`hses_read_write_strings.py`](examples/high_speed_e_server/hses_read_write_strings.py)           | Read and write string variables (16 & 32 bytes)         |
| [`hses_read_write_io.py`](examples/high_speed_e_server/hses_read_write_io.py)                     | Read and write I/O signals (general, external, network) |
| [`hses_read_position_variables.py`](examples/high_speed_e_server/hses_read_position_variables.py) | Read position variables from the controller             |
| [`hses_move_cartesian.py`](examples/high_speed_e_server/hses_move_cartesian.py)                   | Move robot to a Cartesian position                      |
| [`hses_move_joints.py`](examples/high_speed_e_server/hses_move_joints.py)                         | Move robot by specifying joint pulse values             |
| [`hses_servo_command.py`](examples/high_speed_e_server/hses_servo_command.py)                     | Send servo ON/OFF commands                              |
| [`hses_display_message.py`](examples/high_speed_e_server/hses_display_message.py)                 | Display a message on the teach pendant                  |
| [`hses_get_system_info.py`](examples/high_speed_e_server/hses_get_system_info.py)                 | Read system information (software version, name)        |
| [`hses_position_error_torque.py`](examples/high_speed_e_server/hses_position_error_torque.py)     | Read position error and torque for each axis            |
| [`hses_get_management_time.py`](examples/high_speed_e_server/hses_get_management_time.py)         | Read management time (operating, servo, playback)       |
| [`hses_file_operations.py`](examples/high_speed_e_server/hses_file_operations.py)                 | List, download, upload, and delete files                |
| [`hses_get_configuration.py`](examples/high_speed_e_server/hses_get_configuration.py)             | Read axis configuration information                     |

### 🔑 License Examples

| Example                                                               | Description                                            |
| --------------------------------------------------------------------- | ------------------------------------------------------ |
| [`license_info_example.py`](examples/license/license_info_example.py) | Display license state and details, handle registration |

---

## 🔧 Robot Configuration

Some features require specific controller settings.

### ✅ Enable Remote Control

1. Go to `IN/OUT > PSEUDO INPUT SIGNAL`
2. Set `#82015 CMD REMOTE SEL` via `INTERLOCK + SELECT`

### ✅ Key Position for Commands

- Use physical pendant key in remote position
- Optional Ladder setup: copy `#80011` to `#40042`

### ✅ Job Select

1. Go to `SETUP > FUNCTION ENABLE`
2. Set `JOB SELECT WHEN REMOTE AND PLAY` to `PERMIT`

### ✅ File Overwrite Permissions

1. Go to `PARAMETER > RS`
2. Set `RS029 = 1`, `RS214 = 1`

---

## 🔍 Compatibility

|                       | Supported                                   |
| --------------------- | ------------------------------------------- |
| **Robot Controllers** | DX200, YRC1000, YRC1000 Micro               |
| **OS**                | Windows, Linux, macOS                       |
| **Python**            | 3.7+                                        |
| **Dependency**        | `pythonnet 3.0.5` (installed automatically) |

---

## 📢 Contributing

We welcome your feedback and contributions!

- Report issues via [GitHub Issues](https://github.com/underautomation/Yaskawa.py/issues)
- Submit pull requests with enhancements
- Suggest features and improvements

---

## 📜 License

**⚠️ This SDK requires a commercial license.**

- 🆓 **30-day free trial** included out of the box
- 🔄 **Get a new trial immediately** at [underautomation.com/license](https://underautomation.com/license?sdk=yaskawa)
- 🛒 **Buy a license** at [underautomation.com/yaskawa](https://underautomation.com/yaskawa)
- 📄 **EULA**: [underautomation.com/yaskawa/eula](https://underautomation.com/yaskawa/eula)

---

## 📬 Need Help?

- 📖 **Documentation**: [underautomation.com/yaskawa/documentation](https://underautomation.com/yaskawa/documentation)
- 🐍 **Python Get Started Guide**: [underautomation.com/yaskawa/documentation/get-started-python](https://underautomation.com/yaskawa/documentation/get-started-python)
- 📦 **PyPI Package**: [pypi.org/project/UnderAutomation.Yaskawa](https://pypi.org/project/UnderAutomation.Yaskawa/)
- 📩 **Contact Us**: [underautomation.com/contact](https://underautomation.com/contact)
