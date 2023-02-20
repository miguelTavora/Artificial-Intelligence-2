from state_space_search.components.problem import Problem

class HeuristicProblem(Problem):

    def __init__(self, state, operators):

        super().__init__(state, operators)

    def heuristic(self, state):

        raise NotImplementedError("Abstract Method")
