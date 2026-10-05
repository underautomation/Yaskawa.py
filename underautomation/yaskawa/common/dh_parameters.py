from __future__ import annotations
import typing
from underautomation.yaskawa.common.i_dh_parameters import IDhParameters
from underautomation.yaskawa.common.kinematics_category import KinematicsCategory
from underautomation.yaskawa.kinematics.arm_kinematic_models import ArmKinematicModels
from UnderAutomation.Yaskawa.Common import DhParameters as dh_parameters
from UnderAutomation.Yaskawa.Common import KinematicsCategory as kinematics_category
from UnderAutomation.Yaskawa.Kinematics import ArmKinematicModels as arm_kinematic_models

class DhParameters(IDhParameters):
	'''Denavit-Hartenberg parameters of a 6-axis Yaskawa arm (axes S, L, U, R, B, T).'''
	def __init__(self, a1: float, a2: float, a3: float, d4: float, d5: float, d6: float, theta2: float, theta3: float, theta5: float, _internal = 0):
		'''Initializes a new instance of DhParameters with the specified values.

		:param a1: Offset between the S axis and the L axis (mm).
		:param a2: Lower arm length (mm).
		:param a3: Elbow offset (mm).
		:param d4: Forearm length (mm).
		:param d5: Wrist offset along the B axis (mm).
		:param d6: Distance between the wrist and the flange (mm).
		:param theta2: DH angle of the L axis at zero pulse (degrees).
		:param theta3: DH angle of the U axis at zero pulse (degrees).
		:param theta5: DH angle of the B axis at zero pulse (degrees).
		'''
		if(_internal == 0):
			self._instance = dh_parameters(a1, a2, a3, d4, d5, d6, theta2, theta3, theta5)
		else:
			self._instance = _internal

	@staticmethod
	def from_arm_kinematic_model_name(modelName: str) -> 'DhParameters':
		'''Returns the DH parameters of a known robot model, from its name (for example "GP7" or "HC10DTP"). The comparison ignores case.

		:param modelName: Robot model name, as given by the description of ArmKinematicModels members.
		:returns: The DH parameters, or null if the model is not known.
		'''
		return DhParameters(None, None, None, None, None, None, None, None, None, dh_parameters.FromArmKinematicModelName(modelName))

	@staticmethod
	def from_arm_kinematic_model(model: ArmKinematicModels) -> 'DhParameters':
		'''Returns the DH parameters of a known robot model.

		:param model: Robot model.
		:returns: The DH parameters of this model.
		'''
		return DhParameters(None, None, None, None, None, None, None, None, None, dh_parameters.FromArmKinematicModel(arm_kinematic_models(int(model))))

	@staticmethod
	def from_prm_file(path: str) -> 'DhParameters':
		'''Reads the DH parameters of robot group 1 from an ALL.PRM parameter file saved from a controller. DX100, DX200, FS100, YRC1000 and YRC1000micro files are supported.

		:param path: Path of the .prm file.
		:returns: The DH parameters of the robot.
		'''
		return DhParameters(None, None, None, None, None, None, None, None, None, dh_parameters.FromPrmFile(path))

	@staticmethod
	def from_prm_content(content: str) -> 'DhParameters':
		'''Reads the DH parameters of robot group 1 from the text content of an ALL.PRM parameter file. DX100, DX200, FS100, YRC1000 and YRC1000micro files are supported.

		:param content: Text content of the .prm file.
		:returns: The DH parameters of the robot.
		'''
		return DhParameters(None, None, None, None, None, None, None, None, None, dh_parameters.FromPrmContent(content))

	@property
	def a1(self) -> float:
		return self._instance.A1

	@a1.setter
	def a1(self, value: float):
		self._instance.A1 = value

	@property
	def a2(self) -> float:
		return self._instance.A2

	@a2.setter
	def a2(self, value: float):
		self._instance.A2 = value

	@property
	def a3(self) -> float:
		return self._instance.A3

	@a3.setter
	def a3(self, value: float):
		self._instance.A3 = value

	@property
	def d4(self) -> float:
		return self._instance.D4

	@d4.setter
	def d4(self, value: float):
		self._instance.D4 = value

	@property
	def d5(self) -> float:
		return self._instance.D5

	@d5.setter
	def d5(self, value: float):
		self._instance.D5 = value

	@property
	def d6(self) -> float:
		return self._instance.D6

	@d6.setter
	def d6(self, value: float):
		self._instance.D6 = value

	@property
	def theta2(self) -> float:
		return self._instance.Theta2

	@theta2.setter
	def theta2(self, value: float):
		self._instance.Theta2 = value

	@property
	def theta3(self) -> float:
		return self._instance.Theta3

	@theta3.setter
	def theta3(self, value: float):
		self._instance.Theta3 = value

	@property
	def theta5(self) -> float:
		return self._instance.Theta5

	@theta5.setter
	def theta5(self, value: float):
		self._instance.Theta5 = value

	@property
	def kinematics_category(self) -> KinematicsCategory:
		'''Kinematic structure of the arm: Opw when d5 is 0, J5OffsetWrist otherwise.'''
		return KinematicsCategory(int(self._instance.KinematicsCategory))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DhParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
