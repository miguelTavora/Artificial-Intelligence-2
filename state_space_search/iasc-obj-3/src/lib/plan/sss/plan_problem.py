from state_space_search.components.heuristic_problem import HeuristicProblem
import math

class PlanProblem(HeuristicProblem):

    def __init__(self, initial_state, final_state, operators):
        super().__init__(initial_state, operators)
        self.__final_state = final_state

    def objective(self, state):
        return (state == self.__final_state)

    def heuristic(self, state):
        current_x, current_y = state
        final_x, final_y = self.__final_state
        vector = (current_x - final_x, current_y - final_y)
        result = math.sqrt((vector[0] ** 2) + (vector[1] ** 2))
        return result

    def __str__(self):
        return "Final state: "+str(self.__final_state)