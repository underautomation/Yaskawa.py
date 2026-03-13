from enum import IntEnum

class HostControlStopBits(IntEnum):
	'''Specifies the number of stop bits used on the serial port.'''
	One = 1 # One stop bit is used.
	OnePointFive = 3 # 1.5 stop bits are used.
	Two = 2 # Two stop bits are used.
