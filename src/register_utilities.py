from time import sleep
import sys
from gpiozero import *
import re

# input gpio2
# latch gpio3
# clock gpio4
# Shift Reg 8: ouputs 2,3,4,5

# Initialize the variables
delay = 0.01
clock_pin = 4
latch_pin = 3
output_pin = 2


# Initialize the GPIO
clock = DigitalOutputDevice(clock_pin, initial_value=False)
output = DigitalOutputDevice(output_pin, initial_value=False)
latch = DigitalOutputDevice(latch_pin, initial_value=False)


def initialize_gpio():

	return None

def single_update_registers(register_mask, output, clock, latch):
	
	# Update the registers
	for value in register_mask:
		if value == 1:
			output.on()
		else:
			output.off()
	
		# Cycle the clock
		clock.on()
		sleep(delay)
		clock.off()

	# Latch the register
	latch.on()
	sleep(delay)
	latch.off()


def incremental_update_register()

	return None



