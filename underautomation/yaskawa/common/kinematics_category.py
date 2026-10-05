from enum import IntEnum

class KinematicsCategory(IntEnum):
	'''Kinematic structure of a 6-axis arm. It decides which inverse kinematics solver is used.'''
	Opw = 0 # Ortho-parallel base with a spherical wrist: the R, B and T axes meet at one point (D5 = 0). Most industrial arms (GP, MH, ES, HC20DT, HC30PL...). Up to 8 inverse kinematics solutions.
	J5OffsetWrist = 1 # Ortho-parallel base with a wrist offset along the B axis (D5 is not 0): the R and T axes do not meet. Collaborative robots such as HC10, HC10DT, HC20SDT. Up to 16 inverse kinematics solutions.
