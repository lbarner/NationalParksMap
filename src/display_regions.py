import sys
import os
import re
import time
import park_list
from park import Park
import register_utilities

#print(Park.park_list)

# Initialize the variables
park_regions = ['Alaska', 'Intermountain', 'Midwest', 'Northeast', 'Pacific West', 'Southeast']
park_list = Park.park_list


def find_region_parks(park_list, region):

	# Initialize variables
	region_park_list = []

	# Iterate through every park in the list
	for park in park_list:
		if park.region == region:
			region_park_list.append(park)

	return region_park_list


def create_region_mask(region_park_list):

	# Initialize variables
	region_park_mask = [0]*64

	# Iterate through every park in the region
	for park in region_park_list:
		region_park_mask[63-(park.id-1)] = 1

	return region_park_mask


if __name__ == '__main__':

	# Initialize the variables
	delay = 0.00001
	clock_pin = 4
	latch_pin = 3
	output_pin = 2

	map_gpio = register_utilities.MapGPIO(output_pin, clock_pin, latch_pin, delay)

	print(map_gpio)

	while 1:

		for region in park_regions:
			region_parks = find_region_parks(park_list, region)

			print(region)
			print(region_parks)

			region_mask = create_region_mask(region_parks)
			print(region_mask)

			register_utilities.clear_all(map_gpio)

			register_utilities.incremental_update_register(region_mask, map_gpio)

			time.sleep(10)
