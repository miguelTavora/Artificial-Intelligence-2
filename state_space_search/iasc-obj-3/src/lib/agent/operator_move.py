from state_space_search.components.operator import Operator
from operators.enviroment import Enviroment
import math


class OperatorMove(Operator):

	def __init__(self, world_model, move_dist):

		self.__world_model = world_model
		self.__move_dist = move_dist

	# allow to apply a operator to a state to make a transition on the state
	 # @args -> state : State
	 # returns State
	def apply(self, state):

		new_state = (state[0] + self.__move_dist[0], state[1] + self.__move_dist[1])
		element = self.__world_model.obtain_elements(new_state)
		if element in [Enviroment.EMPTY.value, Enviroment.TARGET.value]:
			return new_state

	 
	 # allows obtain the cost associated with state transaction
	 # @args -> state : State, second_state : State
	 # returns float
	def cost(self, state, second_state):

		cost_pos_x = (second_state[0] - state.state[0]) ** 2
		cost_pos_y = (second_state[1] - state.state[1]) ** 2
		return math.sqrt( cost_pos_y + cost_pos_x)

	
	@property
	def move_dist(self):
		return self.__move_dist


	def __str__(self):
		return "Opr: "+str(self.__move_dist) 



		