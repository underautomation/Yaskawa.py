from enum import IntEnum

class HostControlParity(IntEnum):
	'''Specifies the parity bit setting for serial communication.'''
	Odd = 1 # Sets the parity bit so that the count of bits set is an odd number.
	Even = 2 # Sets the parity bit so that the count of bits set is an even number.
	Mark = 3 # Leaves the parity bit set to 1.
	Space = 4 # Leaves the parity bit set to 0.
