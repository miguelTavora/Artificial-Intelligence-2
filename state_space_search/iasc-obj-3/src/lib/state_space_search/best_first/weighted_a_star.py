from state_space_search.best_first.search_best_first import SearchBestFirst

class WeightedAStar(SearchBestFirst):

    def __init__(self, weight=0.5):
        super().__init__()
        self.__weight = weight

    # @args -> node : Node
    # returns double
    def f(self, node):

        #((1-self.__weight)*node.cost) + (self.__weight * self.problem.heuristic(node.state))
        return node.cost + ((1 + self.__weight)*self.problem.heuristic(node.state)) 