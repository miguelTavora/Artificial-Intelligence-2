from components.operator import Operator

class OperatorTravelling(Operator):

    # generate neighbors of the random solution by swapping cities
    # @args -> list
    # returns - list
    def obtain_neighbours(self, solution):
        
        neighbours = []

        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                neighbour = solution.copy()
                neighbour[i] = solution[j]
                neighbour[j] = solution[i]
                neighbours.append(neighbour)
        
        return neighbours

