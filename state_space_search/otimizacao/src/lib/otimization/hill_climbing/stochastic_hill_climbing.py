import random as rd
from otimization.hill_climbing.algorithm import Algorithm

class StochasticHillClimbing(Algorithm):

    def __init__(self):

        self.__initial_path = None 
        self.__initial_cost = 0 

    # does not examine before moving
    # selects a random node and decide as current state or move to another
    def obtain_path(self, problem, neighours, solution, max_iter = 10_000):

        self.__initial_path = solution
        self.__initial_cost = problem.cost_solution(solution)

        for i in range(max_iter):

            best_path = problem.random_neighbour(neighours)
            best_cost = problem.cost_solution(best_path)

            # decide it as the current state
            if best_cost < self.__initial_cost:
                self.__initial_path = best_path
                self.__initial_cost = best_cost
                return best_path, best_cost
        
        return self.__initial_path, self.__initial_cost

    
