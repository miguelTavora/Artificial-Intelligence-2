from state_space_search.best_first.search_best_first import SearchBestFirst

class AASearch(SearchBestFirst):

    # @args -> node : Node
    # returns double
    def f(self, node):

        return node.cost + self.problem.heuristic(node.state)