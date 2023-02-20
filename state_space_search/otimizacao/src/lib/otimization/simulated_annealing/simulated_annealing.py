import random as rd
import math

class SimulatedAnnealing():

    def __init__(self, operator, problem, schedule):

        self.__operator = operator
        self.__problem = problem
        self.__schedule = schedule # represents a mapping from time to "temperature"

        self.__path = None
        self.__cost = 0 
        self.__iterations = 0

    # @args -> max_iter  : int (number max of iterations of the algorithm)
    # returns solution found and cost
    def calculate(self, max_iter = 100_000):

        self.__path = self.__problem.generate_random_solution() #self.__path
        self.__cost = self.__problem.cost_solution(self.__path)

        T = self.__schedule

        for i in range(max_iter):
            self.__iterations = i

            T = T * 0.99 # must add the factor to performe better

            # returns the current when T == 0
            if T == 0: return self.__path, self.__cost

            new_neighbours = self.__operator.obtain_neighbours(self.__path)
            rd_neighbour = self.__problem.random_neighbour(new_neighbours) 
            cost = self.__problem.cost_solution(rd_neighbour)

            # when the difference is bigger than 0
            if cost < self.__cost:
                self.__path = rd_neighbour
                self.__cost = cost

            else:
                rd_number = rd.uniform(0, 1)
                prob = math.exp( (self.__cost - cost) / T)
                if prob > rd_number:
                    self.__path = rd_neighbour
                    self.__cost = cost
        
        print("Solution:", self.__path, "Cost:", self.__cost, "Iterations:", self.__iterations)
        return self.__path, self.__cost

