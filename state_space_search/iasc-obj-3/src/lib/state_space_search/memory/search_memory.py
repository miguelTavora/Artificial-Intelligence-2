class SearchMemory():


    # @args -> frontier : Queue<E -> Node>
    # explored -> map key -> State, value -> Node
    def __init__(self):
        self.__frontier = []
        self.__explored = {}

    # clear all the memory
    def clear(self):
        self.__frontier.clear()
        self.__explored.clear()

    # @args node -> Node
    def insert(self, node):

        state = node.state
        memory_node = self.__explored.get(state)

        if memory_node == None or node.cost < memory_node.cost:
            #self.__frontier.append(node)
            self.insert_node(node)
            self.__explored[state] = node

    # returns Node if the frontier has elements otherwise returns None
    def remove(self):
        if len(self.__frontier) > 0:
            return self.__frontier.pop(0)
        return None

    # returns boolean true if frontier is empty
    def empty_frontier(self):
        return len(self.__frontier) == 0

    @property
    def frontier(self):
        return self.__frontier

    def insert_node(self, node):
        self.__frontier.append(node)