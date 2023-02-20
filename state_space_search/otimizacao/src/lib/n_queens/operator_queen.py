from components.operator import Operator

class OperatorQueen(Operator):

    def obtain_neighbours(self, solution):

        neighbours = []

        for i in range(len(solution)):
            available_pos = [*range(8)] # create a list with 0 to 7
            available_pos.remove(solution[i]) # remove the current pos of the queen
            for j in range(len(available_pos)):
                neighbour = solution.copy()
                neighbour[i] = available_pos[j]
                neighbours.append(neighbour)

        return neighbours