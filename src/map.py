
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


