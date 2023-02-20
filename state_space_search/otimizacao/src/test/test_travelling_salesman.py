from travelling_salesman.city_data import CityData
from travelling_salesman.operator_travelling import OperatorTravelling
from travelling_salesman.problem_travelling import ProblemTravelling

from otimization.hill_climbing.hill_climbing import HillClimbing
from otimization.hill_climbing.stochastic_hill_climbing import StochasticHillClimbing
from otimization.hill_climbing.run_hill_climbing import RunHillClimbing

from otimization.simulated_annealing.simulated_annealing import SimulatedAnnealing

from graph.graph_travelling import GraphTravelling


data = CityData()
operator = OperatorTravelling()
problem = ProblemTravelling(data)




algorithm = HillClimbing()
algorithm = StochasticHillClimbing()

run_algorithm = RunHillClimbing(operator, problem, algorithm)   

solution, cost, iter = run_algorithm.calculate()


print("-------------")


algorithm = SimulatedAnnealing(operator, problem, schedule = 25)
path, cost = algorithm.calculate(max_iter = 1_000)



#### DRAW GRAPH
graph = GraphTravelling(data.coordinates, solution)
graph.plot_path()



graph = GraphTravelling(data.coordinates, path)
graph.plot_path()
