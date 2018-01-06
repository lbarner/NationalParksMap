from time import sleep
import sys
from gpiozero import *
import re

# input gpio2
# latch gpio3
# clock gpio4
# Shift Reg 8: ouputs 2,3,4,5

delay = 0.01

# Create the list of clear and parks
parks = [0]*64

# Import the database
with open(sys.argv[1], 'r') as input_fh:
	database = input_fh.readlines()

# Set the park values as needed
for line in database:
	line_split = re.split(',', line)
	park_name = line_split[0].strip()
	park_index = int(line_split[1].strip())
	park_visited = line_split[-1].strip()

	if park_visited == 'True':
		parks[63-(park_index-1)] = 1
		print(park_name)

print(parks)

# Initialize the GPIO
clock = DigitalOutputDevice(4, initial_value=False)
output = DigitalOutputDevice(2, initial_value=False)
latch = DigitalOutputDevice(3, initial_value=False)

# Set the park
for i in parks:
	# Set the input value
        if i == 1:
                output.on()
        else:
                output.off()

	# Cycle the clock
        clock.on()
        sleep(delay)
        clock.off()

# Latch the data
latch.on()
sleep(delay)
latch.off()

while 1:
	sleep(5)


# Clean the pins
clock.close()
output.close()
latch.close()

