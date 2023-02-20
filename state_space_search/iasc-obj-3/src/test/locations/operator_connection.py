from state_space_search.components.operator import Operator
from state_loc import StateLoc

class OperatorConnection(Operator):

    def __init__(self, start_loc, final_loc, cost):

        self.__start_loc = StateLoc(start_loc)
        self.__final_loc = StateLoc(final_loc)
        self.__cost = cost

    def apply(self, state):

        if hash(state) == hash(self.__start_loc):
            return self.__final_loc

        return None

    def cost(self, state, second_state):
        return self.__cost


    def __str__(self):
        return "Initial Loc: "+str(self.__start_loc)+", Final Loc: "+str(self.__final_loc)+", cost: "+str(self.__cost)

    @property
    def path_cost(self):
        return self.__cost

    @property
    def initial_loc(self):
        return self.__start_loc