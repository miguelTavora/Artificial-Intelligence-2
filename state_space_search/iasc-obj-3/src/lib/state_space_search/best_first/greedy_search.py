from state_space_search.best_first.search_best_first import SearchBestFirst

class GreedySearch(SearchBestFirst):

    # @args -> node : Node
    # returns double
    def f(self, node):

        return self.problem.heuristic(node.state)
