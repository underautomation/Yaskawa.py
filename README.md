# Yaskawa Communication SDK for Python

[![UnderAutomation Yaskawa communication SDK](https://raw.githubusercontent.com/underautomation/yaskawa.NET/refs/heads/main/.github/assets/banner.png)](https://underautomation.com)

[![Python 3.7+](https://img.shields.io/badge/Language-Python-blue)](#)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue)](#)
[![License](https://img.shields.io/badge/License-Commercial-red)](https://underautomation.com/yaskawa/eula)

### 🤖 Communicate effortlessly with Yaskawa robots using Python

The **Yaskawa SDK for Python** enables real-time control and data exchange with Yaskawa Motoman robots via the **High-Speed Ethernet Server (HSES)** protocol.

Ideal for automation, research, and integration projects, it provides high-speed UDP communication, motion control, robot monitoring, job handling, and more.

🔗 **More Info:** [https://underautomation.com/yaskawa](https://underautomation.com/yaskawa)  
🔗 Also available in **[🟦 .NET](https://github.com/underautomation/yaskawa.NET)** and **[🟨 LabVIEW](https://github.com/underautomation/yaskawa.vi)**

---

[⭐ Star the project](https://github.com/underautomation/yaskawa.py/stargazers)  
[👁️ Watch for updates](https://github.com/underautomation/yaskawa.py/watchers)

---

## 🚀 TL;DR

- 📡 **High-Speed Ethernet Server**
- 🤖 **Move robot in Cartesian or joint space**
- 🛠️ **Access robot status, alarms, and I/O**
- 💾 **Read/write registers and data types**
- 🧠 **Control and monitor jobs**
- ✍️ **Send pendant messages, reset alarms, manage files**

**No Yaskawa options or additional hardware required.**

## Try it

From Pypi :

```
pip install UnderAutomation.Yaskawa
```

From this repo :

```
git clone https://github.com/underautomation/Yaskawa.py.git
pip install -e .
```

---

## ✨ Example Usage (Python)

```python
from underautomation.yaskawa.connect_parameters import ConnectParameters
from underautomation.yaskawa.high_speed_e_server.alarm_reset_type import AlarmResetType
from underautomation.yaskawa.yaskawa_robot import YaskawaRobot


robot = YaskawaRobot()
parameters = ConnectParameters("192.168.0.1")
parameters.ping_before_connect = True

robot.connect(parameters)


# Check connection
if robot.high_speed_e_server.connected:
    print("Connected!")

# Move in Cartesian
robot.high_speed_e_server.move_cartesian(
    x=1000, y=10, z=0,
    rx=0, ry=0, rz=0,
    speed=10,
)

# Get current joint position
joint_position = robot.high_speed_e_server.get_robot_joint_position()
print(joint_position.axes)

# Read and write register
reg = robot.high_speed_e_server.read_register(10, count=2)
robot.high_speed_e_server.write_register(10, [1234, 5678])

# Reset alarm
robot.high_speed_e_server.alarm_reset(AlarmResetType.Reset)
```

---

## 🔧 Robot Configuration (Required)

### ✅ Enable Remote Control

- `IN/OUT > PSEUDO INPUT SIGNAL`
- Set `#82015 CMD REMOTE SEL` via `INTERLOCK + SELECT`

### ✅ Key Position for Commands

- Use physical pendant key in remote position
- Optional Ladder setup: copy `#80011` to `#40042`

### ✅ Job Select

- `SETUP > FUNCTION ENABLE`
- Set `JOB SELECT WHEN REMOTE AND PLAY` to `PERMIT`

### ✅ File Overwrite Permissions

- `PARAMETER > RS`
- Set `RS029 = 1`, `RS214 = 1`

---

## 🛠 Installation

### 1. Clone the SDK

```bash
git clone https://github.com/underautomation/yaskawa.py.git
cd yaskawa.py
pip install -e .
```

### 2. Connect to your robot

```python
robot = YaskawaRobot()
parameters = ConnectParameters("192.168.0.1")
robot.connect(parameters)
```

---

## ✅ Compatibility

- **Robots:** DX200, YRC1000, YRC1000 Micro
- **OS:** Windows, Linux, macOS
- **Python:** 3.7+

---

## 🙌 Contributing

We welcome contributions!

- Report bugs via [Issues](https://github.com/underautomation/yaskawa.py/issues)
- Submit pull requests
- Share feature ideas

---

## 📜 License

**⚠️ Commercial license required**  
🔗 Details: [UnderAutomation Licensing](https://underautomation.com/yaskawa/eula)

---

## 📬 Need Help?

- 📖 [Documentation](https://underautomation.com/yaskawa/documentation)
- 📩 [Contact Support](https://underautomation.com/contact)
