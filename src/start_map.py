import RPi.GPIO as GPIO
from time import sleep
import os
import sys

class Park:
	park_count = 0
	park_list = []

	def __init__(self, park_name, park_id, park_visited):
		self.park_name = park_name
		self.park_id = park_id
		self.park_visited = park_visited
		self.park_list.append(self)
		Park.park_count += 1

	def get_count(self):
		return Parks.park_count

	def get_name(self):
		return self.park_name

class Map:

	def __init__(self, map_name, map_park_list):
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

	def compute_bitmask(self):
		map_bitmask = [0, 0, 0, 0, 0, 0, 0, 0,
					   0, 0, 0, 0, 0, 0, 0, 0,
					   0, 0, 0, 0, 0, 0, 0, 0,
					   0, 0, 0, 0, 0, 0, 0, 0,
					   0, 0, 0, 0, 0, 0, 0, 0,
					   0, 0, 0, 0, 0, 0, 0, 0,
					   0, 0, 0, 0, 0, 0, 0, 0,
					   0, 0, 0, 0, 0, 0, 0, 0]

		for park in self.map_park_list:
			park_visited = park.park_visited
			park_id = park.park_id

			if park_visited:
				map_bitmask[park_id] = 1

		return map_bitmask


if __name__ == '__main__':
	# Initialize the list of parks
	arcadia = Park('Arcadia', 0, False)
	american_samoa = Park('American Samoa', 1, Flase)
	arches = Park('Arches', 2, False)
	badlands = Park('Badlands', 3, False)
	big_bend = Park('Big Bend', 4, False)
	biscayne = Park('Biscayne', 5, False)
	black_canyon = Park('Black Canyon of the Gunnison', 6, False)
	bryce_canyon = Park('Bryce Canyon', 7, False)
	canyonlands = Park('Canyonlands', 8, False)
	capitol_reef = Park('Capitol Reef', 9, False)
	carlsbad_caverns = Park('Carlsbad Caverns', 10, False)
	channel_islands = Park('Channel Islands', 11, False)
	conagree = Park('Conagree', 12, False)
	crater_lake = Park('Crater Lake', 13, False)
	cuyahoga_valley = Park('Cuyahoga Valley', 14, True)
	death_valley = Park('Death Valley', 15, True)
	denali = Park('Denali', 16, False)
	dry_tortugas = Park('Dry Tortugas', 17, False)
	everglades =Park('Everglades', 18, False)
	gates_of_the_artic = Park('Gates of Arctic', 19, False)
	glacier = Park('Glacier', 20, False)
	glacier_bay = Park('Glacier Bay', 21, False)
	grand_canyon = Park('Grand Canyon', 22, True)
	grand_teton = Park('Grand Teton', 23, False)
	great_basin = Park('Great Basin', 24, False)
	great_sand_dunes = Park('Great Sand Dunes', 25, False)
	great_smokey_mountains = Park('Great Smokey Mountains', 26, False)
	guadalupe_mountains = Park('Guadalupe Mountains', 27, False)
	haleakala = Park('Haleakala', 28, False)
	hawaii_volcanoes = Park('Hawaii Volcanoes', 29, False)
	hot_springs = Park('Hot Springs', 30, False)
	isle_royale = Park('Isle Royale', 31, False)
	joshua_tree = Park('Joshua Tree', 32, True)
	katamai = Park('Katamai', 33, False)
	kenai_fjords = Park('Kenai Fjords', 34, False)
	kings_canyon = Park('Kings Canyon', 35, False)
	kobuk_valley = Park('Kobuk Valley', 36, False)
	lake_clark = Park('Lake Clark', 37, False)
	lassen_volcanic = Park('Lassen Volcanic', 38, False)
	mammoth_cave = Park('Mammoth Cave', 39, False)
	mesa_verde = Park('Mesa Verde', 40, False)
	mount_rainer = Park('Mount Rainer', 41, True)
	north_cascades = Park('North Cascades', 42, False)
	olympic = Park('Olympic', 43, True)
	petrified_forest = Park('Petrified Forest', 44, False)
	pinnacles = Park('Pinnacles', 45, False)
	redwood = Park('Redwood', 46, False)
	rocky_mountain = Park('Rocky Mountain', 47, True)
	saguaro = Park('Saguaro', 48, True)
	sequoia = Park('Sequoia', 49, True)
	shenandoah = Park('Shenandoah', 50, True)
	theodore_roosevelt = Park('Theodor Roosevelt', 51, False)
	virgin_islands = Park('Virgin Islands', 52, False)
	voyageurs = Park('Voyageurs', 53, False)
	wind_cave = Park('Wind Cave', 54, False)
	wrangell_st_elias = Park('Wrangell-St. Elias', 55, False)
	yellowstone = Park('Yellowstone', 56, False)
	yosemite = Park('Yosemite', 57, True)
	zion = Park('Zion', 58, True)



	base_map = Map('National Park Map', Park.park_list)

	print base_map.compute_bitmask()


