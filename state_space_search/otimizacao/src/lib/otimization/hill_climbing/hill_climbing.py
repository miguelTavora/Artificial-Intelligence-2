from otimization.hill_climbing.algorithm import Algorithm

class HillClimbing(Algorithm):


    def obtain_path(self, problem, neighours, solution):

        # it assumes at first the best neighbour is the first
        best_neighbour = neighours[0]
        best_cost = problem.cost_solution(best_neighbour)

        # iterate trhough all the neighbours
        for neighbour in neighours:
            cost_solution = problem.cost_solution(neighbour)
            if cost_solution < best_cost:
                best_neighbour = neighbour
                best_cost = cost_solution

        return best_neighbour, best_cost