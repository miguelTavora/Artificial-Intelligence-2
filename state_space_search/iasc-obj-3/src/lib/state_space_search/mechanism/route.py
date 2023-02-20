from state_space_search.solution import Solution

class Route(Solution):

    def __init__(self):
        self.__solution = []
        
    def add_beginning(self, node):
        self.__solution.append(node)

    def cost(self):
        return self.__solution[0].cost
    
    def dimension(self):
        return len(self.__solution)

    @property
    def solution(self):
        return self.__solution

    def __str__(self):
        return str(self.__solution)
