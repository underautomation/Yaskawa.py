from enum import IntEnum

class OnOffCommandType(IntEnum):
	'''Specifies the type of ON/OFF command to send to the robot controller. These commands control fundamental robot states that affect safety and operation.'''
	Hold = 1 # Hold command - pauses robot motion while maintaining servo power. Robot can resume from held position. Value: 1.
	Servo = 2 # Servo power command - enables or disables motor power to the robot. Servo must be ON for the robot to move. Value: 2.
	HLock = 3 # Lock Teach Pendant. Value: 3.
