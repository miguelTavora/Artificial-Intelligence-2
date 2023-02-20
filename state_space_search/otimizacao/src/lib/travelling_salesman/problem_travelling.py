import random as rd
from components.problem import Problem

class ProblemTravelling(Problem):

    def __init__(self, data):

        self.__city_costs = data.data
        self.__initial_solution = list(self.__city_costs.keys())

    # obtain the cost with the matrix of cost
    def cost_solution(self, solution):
        
        cost = 0
        for i in range(len(solution)):
            cost += self.__city_costs[solution[i]][self.__initial_solution.index(solution[i-1])]

        return cost

    def random_neighbour(self, neighbours):
        return rd.choice(neighbours)

    # returns -> list
    def generate_random_solution(self):
        
        # shuffle the data
        rd_solution = self.__initial_solution.copy()
        rd.shuffle(rd_solution) # shuffle the data

        return rd_solution