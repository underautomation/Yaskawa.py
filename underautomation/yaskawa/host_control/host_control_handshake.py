from enum import IntEnum

class HostControlHandshake(IntEnum):
	'''Specifies the control protocol used in establishing serial port communication.'''
	XOnXOff = 1 # The XON/XOFF software control protocol is used.
	RequestToSend = 2 # Request-to-Send (RTS) hardware flow control is used.
	RequestToSendXOnXOff = 3 # Both RTS and XON/XOFF are used.
