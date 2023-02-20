from typing import TypeVar, Generic
from state_space_search.mechanism.node import Node
from state_space_search.mechanism.route import Route
from state_space_search.search import Search

P = TypeVar('P')

class SearchMechanism(Search, Generic[P]):

    def __init__(self):
        
        self.__time_cost = 0
        self.__spacial_cost = 0
        self.__problem = None
        self.__search_memory = self.initialize_memory()


    def initialize_memory(self):

        raise NotImplementedError("Abstract method")

    # @args -> problem : Problem
    # returns Solution
    def resolve(self, problem: P, max_depth = 1_999_999):

        self.__problem = problem
        self.__search_memory.clear()
        initial_node = Node(problem.initial_state)
        
        self.__search_memory.insert(initial_node)

        while not self.__search_memory.empty_frontier():
            node = self.__search_memory.remove()

            if problem.objective(node.state):
                return self.generate_solution(node)

            elif node.depth < max_depth:
                self.expand(node)

            else:
                return self.generate_solution(node)


    # @args -> node : Node
    def expand(self, node):

        state = node.state 
        operators = self.__problem.operators

        for operator in operators:
            second_state = operator.apply(state)
            if second_state is not None:
                second_node = Node(second_state, operator, node)
                self.__search_memory.insert(second_node)

            # cost of the time
            self.__time_cost += 1
            

        # cost of the the space
        if len(self.__search_memory.frontier) > self.__spacial_cost:
            self.__spacial_cost = len(self.__search_memory.frontier)

    # @args -> final_node : None
    # returns Solution
    def generate_solution(self, final_node):

        route = Route()
        node = final_node

        while node is not None:
            route.add_beginning(node)
            predecessor =  node.predecessor 
            node = predecessor
            
        return route


    @property
    def time_cost(self):
        return self.__time_cost

    @property
    def spacial_cost(self):
        return self.__spacial_cost

    @property
    def problem(self):
        return self.__problem

    @property
    def search_memory(self):
        return self.__search_memory

