import heapq 
from state_space_search.memory.search_memory import SearchMemory


class PriorityMemory(SearchMemory):

    def __init__(self, reviewer):
        super().__init__()
        self._reviewer = reviewer

    # @Override the method to make a priority Queue
    # @args -> node : Node
    def insert_node(self, node):

        priority = self._reviewer.f(node)
        heapq.heappush(self.frontier, (priority, node))

    # @Override the method of SearchMemory
    def remove(self):

        _, node = heapq.heappop(self.frontier)
        return node



