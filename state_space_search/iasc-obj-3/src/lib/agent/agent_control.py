from operators.perception import Perception
from operators.move_action import MoveAction


class AgentControl():

	def __init__(self, control, filename="amb1.txt", reset=False):

		# to access the methods and varibles of the extended class
		self.__control = control
		self.__perception = Perception(filename)
		self.__move_action = MoveAction(self.__perception)
		self.__reset = reset

	def execute(self):

		# updates the varibles 
		self.__update_perception()
		action = self.__process(self.__perception)
		print("action:",action)
		self.__act(action)

		# resets the world if the argument reset on the constructor is true
		if self.__reset and len(self.__perception.targets) == 0:
			self.__move_action.reset_world()


	def __update_perception(self):
		
		self.__perception.detect()

	def __process(self, perception):

		return self.__control.execute(perception)

	def __act(self, action):

		if action is not None:
			self.__move_action.act(action)

	@property
	def world(self):
		return self.__perception.world

	@property
	def route(self):
		return self.__control.route

	@property
	def route_values(self):
		x = self.__control.route_values
		return x
		


