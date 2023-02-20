class Problem:

    def cost_solution(self, solution):

        raise NotImplementedError("Interface method")

    def generate_random_solution(self):

        raise NotImplementedError("Interface method")

    def random_neighbour(self, neighbours):

        raise NotImplementedError("Interface method")