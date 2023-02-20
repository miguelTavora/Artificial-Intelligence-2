from problem_loc import ProblemLoc
from operator_connection import OperatorConnection
from state_space_search.best_first.uniform_cost_search import UniformCostSearch
from state_loc import StateLoc

class TrajectoryPlanner():

	def __init__(self, initial_loc = 0, final_loc = 6):

		self.__initial_loc = initial_loc
		print("Loc inicial:", self.__initial_loc)
		
		self.__final_loc = final_loc
		print("Loc final:", self.__final_loc)

		
	def run(self):

		prob_loc = ProblemLoc(self.__initial_loc, self.__final_loc, self.define_operators())
		route = UniformCostSearch().resolve(prob_loc)
		self.show_trajectory(route)


	def define_operators(self):

		operators = [OperatorConnection(0, 1, 5), OperatorConnection(0, 2, 25),
				OperatorConnection(1, 3, 12), OperatorConnection(1, 6, 5),
				OperatorConnection(2, 4, 30), OperatorConnection(3, 2, 10),
				OperatorConnection(3, 5, 5), OperatorConnection(4, 3, 2),
				OperatorConnection(5, 6, 8), OperatorConnection(5, 4, 10),
				OperatorConnection(6, 3, 15)]

		return operators


	def show_trajectory(self, route):

		solution = route.solution
		cost = solution[0].cost
		path = []

		for step in solution:
			print("step:", step)
			print("type:", type(step))
			path.append(str(step.state))
			#if isinstance(step, StateLoc()):
				#cost += step.path_cost
				#path.append(step.initial_loc)

		path.reverse()
		print("Path:", path)
		print("Cost:", cost)