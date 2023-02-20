import math
from operators.enviroment import Enviroment

class Perception:

	def __init__(self, world):

		self.__world = world
		self.detect()
		self.reset()

	@property
	def position(self):
		return self.__position


	@property
	def targets(self):
		return self.__targets


	def detect(self):

		self.__targets = self.__detect_positions(self.__world, Enviroment.TARGET)
		self.__position = self.__obtain_agent_loc(self.__world)
		

	def reset(self):

		self.collision = False
		self.load = False
		self.movement_cost = 0


	def __obtain_agent_loc(self, world):


		for line in range(len(world)):
			for column in range(len(world[line])):
				if Enviroment.CURRENT_POS.value == world[column][line]:
					return (line, column) # state is a tuple (pos x, pos y)

	

	def __detect_positions(self, world, type):

		pos = []

		for line in range(len(world)):
			for column in range(len(world[line])):
				if type.value == world[column][line]:
					pos.append((line, column))

		return pos


	# cost function is the pitagoras formula
	def cost(self, state, new_state):

		cost_pos_y = (new_state[1] - state[1]) ** 2
		cost_pos_x = (new_state[0] - state[0]) ** 2
		return math.sqrt( cost_pos_y + cost_pos_x)


	def __str__(self):
		return "position: "+str(self.__position)+", target: "+str(self.__targets)+", movement cost: "+str(self.movement_cost)


	def print_world(self, world):

		for line in world:
			result = ""
			print(result.join(line))

		