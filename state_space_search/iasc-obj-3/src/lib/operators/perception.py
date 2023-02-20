from copy import deepcopy
from operators.enviroment import Enviroment

class Perception:

	def __init__(self, world_name):

		file = open(world_name, "r")
		text = file.read()
		lines = text.split("\n")
		
		# converts the string to char list
		for line in range(len(lines)):
			lines[line] = [*lines[line]]

		self.__world = lines
		print("Lines:", self.__world)
		self.__elements = {}
		self.detect()

	@property
	def position(self):
		return self.__position

	@property
	def targets(self):
		return self.__targets

	@property
	def world(self):
		return self.__world

	@property
	def elements(self):
		return self.__elements


	def detect(self):

		self.__targets = self.__detect_positions(self.__world, Enviroment.TARGET)
		self.__position = self.__obtain_agent_loc(self.__world)
		self.__elements = self.__detect_elements(self.__world)


	def __detect_elements(self, world):

		result = {}

		for line in range(len(world)):
			for column in range(len(world[line])):
				result[(line, column)] = world[column][line]

		return result


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


	def print_world(self):

		for line in self.__world:
			result = ""
			print(result.join(line))

		