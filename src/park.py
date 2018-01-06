
class Park:
	park_count = 0
	park_list = []

	def __init__(self, park_name, park_region, park_state, park_founded, park_id, park_visited):
		self.name = park_name
		self.region = park_region
		self.state = park_state
		self.founded = park_founded
		self.id = park_id
		self.park_visited = park_visited
		self.park_list.append(self)
		Park.park_count += 1

	def get_count(self):
		return Parks.park_count

	def get_name(self):
		return self.park_name

