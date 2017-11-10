#import RPi.GPIO as GPIO
from time import sleep
import os
import sys

class Park:
	park_count = 0
	park_list = []

	def __init__(self, park_name, park_bitmask):
		self.park_name = park_name
		self.park_bitmask = park_bitmask
		self.park_list.append(self)
		Park.park_count += 1

	def get_count(self):
		return Parks.park_count

	def get_name(self):
		return self.park_name

	def get_bitmask(self):
		return self.park_bitmask

class Map:

	def __init__(self, map_name, park_list):
		self.map_name = map_name
		self.map_park_list = map_park_list
		self.map_park_count = len(map_park_list)

	def add_park(self, park):
		self.map_park_list.append(park)

	def reset_map(self):
		self.map_park_list = []

	def park_count(self):
		self.map_park_count = len(self.map_park_list)
		return self.map_park_count





if __name__ == '__main__':
	# Initialize the list of parks
	arcadia = Park('Arcadia', 1)
	american_samoa = Park('American Samoa', 2)
	arches = Park('Arches', 4)
	badlands = Park('Badlands', 8)
	big_bend = Park('Big Bend', 16)
	biscayne = Park('Biscayne', 32)

	print Park.park_list


