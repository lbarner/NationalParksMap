from time import sleep
import sys
from gpiozero import *
import re

# input gpio2
# latch gpio3
# clock gpio4
# Shift Reg 8: ouputs 2,3,4,5

# Initialize the variables
default_delay = 0.01
default_clock_pin = 4
default_latch_pin = 3
default_output_pin = 2

class MapGPIO:

	def __init__(self, output_pin=default_output_pin, clock_pin=default_clock_pin, latch_pin=default_latch_pin, delay=default_delay):
		self.clock = DigitalOutputDevice(clock_pin, initial_value=False)
		self.output = DigitalOutputDevice(output_pin, initial_value=False)
		self.latch = DigitalOutputDevice(latch_pin, initial_value=False)
		self.delay = delay

def clear_all(map_gpio):

        # Initialize the variables
        register_mask = [0]*64

        for value in register_mask:
                if value == 1:
                        map_gpio.output.on()
                else:
                        map_gpio.output.off()

                # Cycle the clock
                map_gpio.clock.on()
                sleep(0.0001)
                map_gpio.clock.off()

        # Latch the register
        map_gpio.latch.on()
        sleep(0.0001)
        map_gpio.latch.off()


def update_registers(register_mask, map_gpio):
	
	# Update the registers
	clear_all(map_gpio)
	for value in register_mask:
		if value == 1:
			map_gpio.output.on()
		else:
			map_gpio.output.off()
	
		# Cycle the clock
		map_gpio.clock.on()
		sleep(map_gpio.delay)
		map_gpio.clock.off()

	# Latch the register
	map_gpio.latch.on()
	sleep(map_gpio.delay)
	map_gpio.latch.off()
	sleep(1)


def incremental_update_register(register_mask, map_gpio):

	# Initialize the variables
	incremental_mask = [0]*64

	# Iterate through every
	for i in range(0,len(register_mask)):
		value = register_mask[i]		

		if value == 1:
			incremental_mask[i] = 1

			update_registers(incremental_mask, map_gpio)


def clear_all(map_gpio):

        # Initialize the variables
        register_mask = [0]*64

        for value in register_mask:
                if value == 1:
                        map_gpio.output.on()
                else:
                        map_gpio.output.off()

                # Cycle the clock
                map_gpio.clock.on()
                sleep(0.0001)
                map_gpio.clock.off()

        # Latch the register
        map_gpio.latch.on()
        sleep(0.0001)
        map_gpio.latch.off()
