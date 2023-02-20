from state_space_search.components.problem import Problem

class PlanProblem(Problem):

    def __init__(self, initial_state, operators, objectives):
        super().__init__(initial_state, operators)
        self.__objectives = objectives

    def objective(self, state):
        return self.__objectives 


    def __str__(self):
        return "Objectives: "+str(self.__objectives)