import RPi.GPIO as GPIO
from time import sleep
import os
import sys
from park import Park
from map import Map
import park_list

if __name__ == '__main__':

	print(zion.get_namer())

	base_map = Map('National Park Map', Park.park_list)

	print(base_map.compute_bitmask())


