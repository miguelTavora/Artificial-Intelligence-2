from operators.perception import Perception
from operators.move_action import MoveAction

class Agent:

	def __init__(self, filename):

		file = open(filename, "r")
		text = file.read()
		lines = text.split("\n")
		
		# converts the string to char list
		for line in range(len(lines)):
			lines[line] = [*lines[line]]

		self.__world = lines
		
		self.__perception = Perception(self.__world)
		self.__move_action = MoveAction(self.__world, self.__perception)


	@property
	def perception(self):
		return self.__perception

	@property
	def move_action(self):
		return self.__move_action

	@property
	def world(self):
		return self.__world