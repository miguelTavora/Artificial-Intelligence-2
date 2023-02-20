import random as rd
from components.problem import Problem

class ProblemQueen(Problem):

    def __init__(self, data):

        self.__initial_solution = data.initial_solution
        self.__size = len(self.__initial_solution)

    # returns the cost of a solution
    def cost_solution(self, solution):

        return self.__cost_perpendicular(solution) + self.__cost_diagonal(solution)

    # generates a random solution for the problem
    def generate_random_solution(self):
        random_solution = []

        for i in range(self.__size):
            random_solution.append(rd.randint(0, self.__size-1))
            
        return random_solution

    # chooses a random neigbour from all neighbours
    def random_neighbour(self, neighbours):
        return rd.choice(neighbours)


    def __cost_perpendicular(self, solution):
        
        found = []
        cost = 0
        for i in range(len(solution) - 1):

            # not found already detected pieces
            if solution[i] not in found:

                for j in range(i + 1, len(solution)):
                    # when the number is equal is a colision
                    if solution[i] == solution[j]:
                        cost += 1

                # add to the list to prevent double count 
                found.append(solution[i])

        return cost


    def __cost_diagonal(self, solution):
    
        cost = 0
        found = []
        for pos in range(len(solution) -1):

            # check the negative and positive diagonal
            compared_pos = solution[pos] + 1
            compared_neg = solution[pos] - 1
            if pos not in found:

                #iterate through the perpendicular and check if is the value
                for pos_2 in range(pos + 1, len(solution)):

                    if solution[pos_2] == compared_pos: 
                        cost += 1
                        found.append(pos_2)

                    if solution[pos_2] == compared_neg:
                        cost += 1
                        found.append(pos_2)

                    compared_pos += 1
                    compared_neg -= 1

        return cost