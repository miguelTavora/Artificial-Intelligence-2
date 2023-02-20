from state_space_search.components.problem import Problem
from operator_connection import OperatorConnection
from state_loc import StateLoc

class ProblemLoc(Problem):

    def __init__(self, initial_state, final_state, operators):

        super().__init__(StateLoc(initial_state), operators)
        self.__final_state = final_state

    
    def objective(self, state):

        return state == self.__final_state