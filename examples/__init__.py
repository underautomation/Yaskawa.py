"""
Helper for Yaskawa.py examples
- Automatic sys.path setup
- Persistent robot configuration management
- License management
"""
import sys
import json
from pathlib import Path

# ==============================================================================
# Path setup for imports
# ==============================================================================
def setup_path():
    root = Path(__file__).parent.parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

setup_path()

# ==============================================================================
# Configuration file management
# ==============================================================================
_config_file = Path(__file__).parent / "robot_config.json"

def _load_config():
    """Load saved configuration from file."""
    if _config_file.exists():
        try:
            with open(_config_file, 'r') as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def _save_config(config):
    """Save configuration to file."""
    with open(_config_file, 'w') as f:
        json.dump(config, f, indent=2)

def _get_setting(key, prompt, default=None, hide_default=False):
    """
    Generic helper to get a setting from the user.
    If already saved, proposes it as default. Otherwise, asks the user and saves it.
    """
    config = _load_config()
    saved = config.get(key, default)

    if saved is not None:
        display = "****" if hide_default and saved else saved
        user_input = input(f"{prompt} [{display}]: ").strip()
        value = user_input if user_input else saved
    else:
        value = input(f"{prompt}: ").strip()

    if value != config.get(key):
        config[key] = value
        _save_config(config)

    return value

# ==============================================================================
# Robot IP / Connection
# ==============================================================================
def get_robot_ip():
    """
    Gets the robot IP address.
    If already saved, proposes it as default.

    Returns:
        str: Robot IP address
    """
    return _get_setting("robot_ip", "Robot IP address")

# ==============================================================================
# License management
# ==============================================================================
def setup_license():
    """
    Checks the current license state and handles registration.

    - If already licensed or in trial: prints license info
    - If expired or invalid: asks user for licensee/key and registers
    - If user has no key: shows URL to request a free trial

    Returns:
        LicenseInfo: The current license information
    """
    from underautomation.yaskawa.yaskawa_robot import YaskawaRobot
    from underautomation.yaskawa.license.license_state import LicenseState

    config = _load_config()
    saved_licensee = config.get("licensee", "")
    saved_key = config.get("license_key", "")

    if saved_licensee and saved_key:
        license_info = YaskawaRobot.register_license(saved_licensee, saved_key)
    else:
        robot = YaskawaRobot()
        license_info = robot.license_info

    state = license_info.state

    if state == LicenseState.Licensed or state == LicenseState.Trial or state == LicenseState.ExtraTrial:
        print("=" * 60)
        print("LICENSE INFO")
        print("=" * 60)
        print(license_info)
        print("=" * 60)
        return license_info

    print("=" * 60)
    print("LICENSE REGISTRATION REQUIRED")
    print("=" * 60)
    print(f"Current license state: {license_info}")
    print()
    print("If you don't have a license key, you can request a free")
    print("trial license immediately by email from:")
    print("  https://underautomation.com/license")
    print()

    licensee = input("Enter licensee (company/name) [leave empty to skip]: ").strip()
    if not licensee:
        print("Skipping license registration. Running in current mode.")
        return license_info

    key = input("Enter license key: ").strip()
    if not key:
        print("No key provided. Skipping registration.")
        return license_info

    license_info = YaskawaRobot.register_license(licensee, key)

    config["licensee"] = licensee
    config["license_key"] = key
    _save_config(config)

    print()
    print("LICENSE REGISTERED:")
    print(license_info)
    print("=" * 60)

    return license_info

# ==============================================================================
# Helper: Connect to robot
# ==============================================================================
def connect_robot():
    """
    Creates a YaskawaRobot, sets up license, asks for connection settings,
    and connects via the High Speed Ethernet Server protocol.

    Returns:
        YaskawaRobot: Connected robot instance
    """
    from underautomation.yaskawa.yaskawa_robot import YaskawaRobot
    from underautomation.yaskawa.connect_parameters import ConnectParameters

    setup_license()

    robot_ip = get_robot_ip()

    robot = YaskawaRobot()
    params = ConnectParameters(robot_ip)
    params.ping_before_connect = True

    print(f"\nConnecting to {robot_ip} (High Speed Ethernet Server)...")

    try:
        robot.connect(params)
    except Exception as e:
        error_msg = str(e)
        if "license" in error_msg.lower() or "trial" in error_msg.lower() or "expired" in error_msg.lower():
            readable = error_msg.split("\n")[0].strip() if "\n" in error_msg else error_msg
            safe_msg = readable.encode("ascii", errors="replace").decode("ascii")
            print(f"\nLicense error: {safe_msg}")
            print("\nPlease register a valid license first.")
            print("Get a free trial at: https://underautomation.com/license")
            raise SystemExit(1)
        raise

    print("Connected successfully!\n")

    return robot
