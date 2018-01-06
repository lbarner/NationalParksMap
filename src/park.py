
class Park:
	park_count = 0
	park_list = []

	def __init__(self, park_name, park_id, park_region, park_visited):
		self.park_name = park_name
		self.park_id = park_id
		self.park_region = park_region
		self.park_visited = park_visited
		self.park_list.append(self)
		Park.park_count += 1

	def get_count(self):
		return Parks.park_count

	def get_name(self):
		return self.park_name

