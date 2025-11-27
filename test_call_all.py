# test_high_speed_e_server_client_base.py

import pytest

from underautomation.yaskawa.high_speed_e_server.get_file_progress import GetFileProgress
from underautomation.yaskawa.high_speed_e_server.load_file_progress import LoadFileProgress
from underautomation.yaskawa.yaskawa_robot import YaskawaRobot

from underautomation.yaskawa.high_speed_e_server.alarm_reset_type import (
    AlarmResetType,
)
from underautomation.yaskawa.high_speed_e_server.on_off_command_type import (
    OnOffCommandType,
)
from underautomation.yaskawa.high_speed_e_server.switching_commands import (
    SwitchingCommands,
)
from underautomation.yaskawa.high_speed_e_server.robot_recent_alarm import (
    RobotRecentAlarm,
)
from underautomation.yaskawa.high_speed_e_server.position_command_classification import (
    PositionCommandClassification,
)
from underautomation.yaskawa.high_speed_e_server.position_command_operation_coordinate import (
    PositionCommandOperationCoordinate,
)
from underautomation.yaskawa.high_speed_e_server.position_command_type import (
    PositionCommandType,
)
from underautomation.yaskawa.high_speed_e_server.management_time_type import (
    ManagementTimeType,
)
from underautomation.yaskawa.high_speed_e_server.robot_system_type_data import (
    RobotSystemTypeData,
)
from underautomation.yaskawa.high_speed_e_server.robot_control_group import (
    RobotControlGroup,
)
from underautomation.yaskawa.high_speed_e_server.robot_base_position_data import (
    RobotBasePositionData,
)
from underautomation.yaskawa.high_speed_e_server.robot_axis_raw_data_1 import (
    RobotAxisRawData1,
)
from underautomation.yaskawa.high_speed_e_server.robot_position_data_1 import (
    RobotPositionData1,
)

from UnderAutomation.Yaskawa.HighSpeedEServer.Internal import HighSpeedEServerClientBase as high_speed_e_server_client_base



@pytest.fixture(scope="module")
def robot() -> YaskawaRobot:
    # We deliberately do not connect the robot here.
    # All calls should behave as "robot not connected".
    return YaskawaRobot()


@pytest.fixture(scope="module")
def hses(robot: YaskawaRobot):
    # High speed EServer client used in all tests
    return robot.high_speed_e_server


def assert_robot_not_connected(callable_obj, *args, **kwargs):
    """
    Helper to assert that a call raises an exception whose message
    starts with 'Robot is not connected'.
    """
    with pytest.raises(Exception) as excinfo:
        callable_obj(*args, **kwargs)
    msg = str(excinfo.value)
    assert msg.startswith(
        "Robot is not connected"
    ), f"Unexpected exception message: {msg}"


def test_initial_state_not_connected(robot: YaskawaRobot):
    # Sanity check: robot should start disconnected
    assert robot.high_speed_e_server.connected is False


def test_properties_do_not_crash(robot: YaskawaRobot):
    """
    Simple smoke test on properties. They should not throw.
    We do not enforce any particular value here.
    """
    _ = robot.high_speed_e_server.connected
    _ = robot.high_speed_e_server.ip


# Build some reusable sample values coming from the documentation

RECENT_ALARM_LATEST = RobotRecentAlarm.Latest

ALARM_RESET_RESET = AlarmResetType.Reset

ONOFF_SERVO = OnOffCommandType.Servo

SWITCHING_CYCLE = SwitchingCommands.Cycle

CLASSIFICATION_CART_MM = PositionCommandClassification.Cartesian_MM_S

CLASSIFICATION_LINK_PERCENT = PositionCommandClassification.LinkPercent

COORDINATE_BASE = PositionCommandOperationCoordinate.Base
COORDINATE_ROBOT = PositionCommandOperationCoordinate.Robot

POS_CMD_STRAIGHT_INC = PositionCommandType.StraightIncrement
POS_CMD_STRAIGHT_ABS = PositionCommandType.StraightAbsolute

MANAGEMENT_TIME_DEFAULT = ManagementTimeType.ControlPowerOnTime


ROBOT_CONTROL_GROUP_DEFAULT = RobotControlGroup.default_robot_cartesian


@pytest.mark.parametrize(
    "name, call",
    [
        # Alarms and status
        ("get_alarm", lambda h: h.get_alarm(RECENT_ALARM_LATEST)),
        ("get_status_information", lambda h: h.get_status_information()),
        ("get_executing_job_information", lambda h: h.get_executing_job_information()),
        # Configuration and positions
        (
            "get_configuration_information",
            lambda h: h.get_configuration_information(ROBOT_CONTROL_GROUP_DEFAULT),
        ),
        ("get_robot_cartesian_position", lambda h: h.get_robot_cartesian_position()),
        ("get_robot_joint_position", lambda h: h.get_robot_joint_position()),
        (
            "get_robot_position",
            lambda h: h.get_robot_position(ROBOT_CONTROL_GROUP_DEFAULT),
        ),
        (
            "get_position_error",
            lambda h: h.get_position_error(ROBOT_CONTROL_GROUP_DEFAULT),
        ),
        ("get_torque", lambda h: h.get_torque(ROBOT_CONTROL_GROUP_DEFAULT)),
        # Basic commands
        ("alarm_reset", lambda h: h.alarm_reset(ALARM_RESET_RESET)),
        (
            "servo_command_on",
            lambda h: h.servo_command(ONOFF_SERVO, True),
        ),
        (
            "servo_command_off",
            lambda h: h.servo_command(ONOFF_SERVO, False),
        ),
        ("switching_command", lambda h: h.switching_command(SWITCHING_CYCLE)),
        ("display", lambda h: h.display("Hello from tests")),
        ("start_job", lambda h: h.start_job()),
        ("select_job", lambda h: h.select_job("TESTJOB", line=0)),
        # Management time and system information
        (
            "get_management_time_default_index",
            lambda h: h.get_management_time(MANAGEMENT_TIME_DEFAULT),
        ),
        (
            "get_management_time_index_1",
            lambda h: h.get_management_time(MANAGEMENT_TIME_DEFAULT, index=1),
        ),
        # For get_system_information we pass None to use default info on .NET side
        ("get_system_information", lambda h: h.get_system_information(None)),
        # IO and registers
        ("read_io", lambda h: h.read_io(firstIndex=1001, count=4)),
        ("write_io", lambda h: h.write_io(firstIndex=1001, data=[1, 0, 1, 0])),
        ("read_register", lambda h: h.read_register(firstIndex=10, count=2)),
        ("write_register", lambda h: h.write_register(firstIndex=10, data=[100, 28])),
        ("read_byte", lambda h: h.read_byte(firstIndex=2001, count=4)),
        ("write_byte", lambda h: h.write_byte(firstIndex=2001, data=[0x01, 0x00, 0xFF, 0x00])),
        ("read_integer", lambda h: h.read_integer(firstIndex=5001, count=4)),
        ("write_integer", lambda h: h.write_integer(firstIndex=5001, data=[100, 10, 12, 150])),
        ("read_double", lambda h: h.read_double(firstIndex=6001, count=2)),
        ("write_double", lambda h: h.write_double(firstIndex=6001, data=[123.456, -78.9])),
        ("read_single", lambda h: h.read_single(firstIndex=7001, count=3)),
        ("write_single", lambda h: h.write_single(firstIndex=7001, data=[1.23, -4.56, 7.89])),
        ("read16_bytes_char", lambda h: h.read16_bytes_char(firstIndex=8001, count=2)),
        (
            "write16_bytes_char",
            lambda h: h.write16_bytes_char(firstIndex=8001, data=["HelloRobot", "MoveFaster"]),
        ),
        # Position variables
        ("read_position_variable", lambda h: h.read_position_variable(firstIndex=9001, count=1)),
        # For write_position_variable, use an empty list to avoid depending on
        # RobotPositionData1 construction while still exercising the wrapper.
        (
            "write_position_variable",
            lambda h: h.write_position_variable(firstIndex=9001, data=[]),
        ),
        # Base position
        ("read_base_position", lambda h: h.read_base_position(firstIndex=1, count=1)),
        (
            "write_base_position",
            lambda h: h.write_base_position(firstIndex=1, data=[]),
        ),
        # External position
        ("read_external_position", lambda h: h.read_external_position(firstIndex=1, count=1)),
        (
            "write_external_position",
            lambda h: h.write_external_position(firstIndex=1, data=[]),
        ),
        # Extended alarm
        ("get_alarm_extended", lambda h: h.get_alarm_extended(RECENT_ALARM_LATEST)),
        # 32 bytes char helpers
        ("read32_bytes_char", lambda h: h.read32_bytes_char(firstIndex=8101, count=2)),
        #("write32_bytes_char", lambda h: h.write32_bytes_char(firstIndex=8101, data=["Test32Char1", "Test32Char2"]),),
        # File handling
        ("delete_file", lambda h: h.delete_file("TEST.JBI")),
        ("get_file_list", lambda h: h.get_file_list("*.JBI")),
    ],
)
def test_all_methods_raise_robot_not_connected(name, call, hses):
    """
    Generic test that covers most methods.
    When the robot is not connected, every call should raise an exception
    whose message starts with 'Robot is not connected'.
    """
    assert_robot_not_connected(call, hses)


def test_move_cartesian_with_required_arguments(hses):
    """
    Call move_cartesian with required arguments only.
    """
    assert_robot_not_connected(
        hses.move_cartesian,
        1000.0,
        10.0,
        0.0,
        0.0,
        0.0,
        0.0,
        CLASSIFICATION_CART_MM,
        10.0,
        COORDINATE_BASE,
    )


def test_move_cartesian_with_all_arguments(hses):
    """
    Call move_cartesian with all optional arguments provided.
    We keep posture None to avoid depending on RobotPosture construction.
    """
    assert_robot_not_connected(
        hses.move_cartesian,
        500.0,
        20.0,
        30.0,
        1.0,
        2.0,
        3.0,
        CLASSIFICATION_CART_MM,
        50.0,
        COORDINATE_ROBOT,
        None,  # posture
        POS_CMD_STRAIGHT_ABS,
        1,     # RobotControlGroup
        0,     # StationControlGroup
        0,     # tool
        0,     # userCoordinate
    )


def test_move_joints_with_required_arguments(hses):
    """
    Call move_joints with required arguments only.
    """
    assert_robot_not_connected(
        hses.move_joints,
        [1000, 0, 0, 0, 0, 0],
        CLASSIFICATION_LINK_PERCENT,
        10.0,
    )


def test_move_joints_with_all_arguments(hses):
    """
    Call move_joints with all optional arguments provided.
    """
    assert_robot_not_connected(
        hses.move_joints,
        [500, 100, 0, 0, 0, 0],
        CLASSIFICATION_LINK_PERCENT,
        20.0,
        POS_CMD_STRAIGHT_INC,
        1,  # RobotControlGroup
        1,  # StationControlGroup
        0,  # tool
    )


def test_load_file_with_required_arguments(hses):
    """
    Call load_file with only required arguments.
    """
    content = "/// TEST PROGRAM\nNOP\nEND\n"
    assert_robot_not_connected(
        hses.load_file,
        "TEST_LOAD.JBI",
        content,
    )


def test_load_file_with_all_arguments(hses):
    """
    Call load_file with progress callback argument.
    """
    content = "/// TEST PROGRAM WITH PROGRESS\nNOP\nEND\n"

    def on_progress():
        # No need to do anything in tests
        pass


    assert_robot_not_connected(
        hses.load_file,
        "TEST_LOAD_WITH_PROGRESS.JBI",
        content,
        high_speed_e_server_client_base.LoadFileProgressDelegate(lambda x:on_progress(LoadFileProgress(x))),
    )


def test_get_file_with_required_arguments(hses):
    """
    Call get_file with only required arguments.
    """
    assert_robot_not_connected(
        hses.get_file,
        "TEST_GET.JBI",
    )


def test_get_file_with_all_arguments(hses):
    """
    Call get_file with progress callback argument.
    """

    def on_progress(*args, **kwargs):
        pass

    assert_robot_not_connected(
        hses.get_file,
        "TEST_GET_WITH_PROGRESS.JBI",
        high_speed_e_server_client_base.GetFileProgressDelegate(lambda x:on_progress(GetFileProgress(x))),
    )
