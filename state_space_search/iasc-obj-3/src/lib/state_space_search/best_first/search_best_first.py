from state_space_search.memory.priority_memory import PriorityMemory
from state_space_search.mechanism.search_mechanism import SearchMechanism

class SearchBestFirst(SearchMechanism):

    # returns -> PriorityMemory
    def initialize_memory(self):

        return PriorityMemory(self)

    # @args -> node_one : Node, node_two : Node
    def compare(self, node_one, node_two):

        return self.f(node_one) == self.f(node_two)

    def f(self, node):

        raise NotImplementedError("Abstract method")



