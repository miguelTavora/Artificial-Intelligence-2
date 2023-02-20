import random as rd

class RunHillClimbing:

    def __init__(self, operator, problem, algorithm):
        
        self.__operator = operator
        self.__problem = problem
        self.__algorithm = algorithm


    def calculate(self, max_iter = 100_000):
        
        solution = self.__problem.generate_random_solution()
        cost = self.__problem.cost_solution(solution)
        
        neighbours = self.__operator.obtain_neighbours(solution)
        best_neighbour, best_cost = self.__algorithm.obtain_path(self.__problem, neighbours, solution)

        iterations = 0
        while best_cost < cost and max_iter > iterations:

            solution = best_neighbour
            cost = best_cost

            neighbours_obt = self.__operator.obtain_neighbours(solution)
            new_solution = self.__algorithm.obtain_path(self.__problem, neighbours_obt, solution)[0]


            next_neighbor = self.__operator.obtain_neighbours(new_solution)
            best_neighbour, best_cost = self.__algorithm.obtain_path(self.__problem, next_neighbor, new_solution)

            iterations += 1


        print("Solution:", solution, "cost:", cost, "Iter:", iterations)
        return solution, cost, iterations



    

    





		


