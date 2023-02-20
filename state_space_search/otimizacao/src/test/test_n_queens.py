from n_queens.queens_data import QueensData
from n_queens.operator_queen import OperatorQueen
from n_queens.problem_queen import ProblemQueen
from n_queens.result_queen import ResultQueen

from otimization.hill_climbing.hill_climbing import HillClimbing
from otimization.hill_climbing.stochastic_hill_climbing import StochasticHillClimbing
from otimization.hill_climbing.run_hill_climbing import RunHillClimbing

from otimization.simulated_annealing.simulated_annealing import SimulatedAnnealing

from graph.graph_queens import GraphQueens


data = QueensData()
operator = OperatorQueen()
problem = ProblemQueen(data)
result = ResultQueen()



#algorithm = HillClimbing()
algorithm = StochasticHillClimbing()

run_algorithm = RunHillClimbing(operator, problem, algorithm)

solution, cost, iterations = run_algorithm.calculate()
board = result.show_result(solution)


print("----------------")


algorithm = SimulatedAnnealing(operator, problem, schedule = 30)

solution, cost = algorithm.calculate(max_iter = 1_000)

board2 = result.show_result(solution)



### DRAW BOARD

graph = GraphQueens()
graph.graph(board)


graph = GraphQueens()
graph.graph(board2)