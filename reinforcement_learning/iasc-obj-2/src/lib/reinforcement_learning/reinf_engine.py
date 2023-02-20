from reinforcement_learning.learning import Learning
from reinforcement_learning.memory.spread_memory import SpreadMemory
from reinforcement_learning.actions.e_greedy import EGreedy

from reinforcement_learning.learn_method.sarsa import SARSA
from reinforcement_learning.learn_method.q_learning import QLearning
from reinforcement_learning.learn_method.qme.qme import QME
from reinforcement_learning.learn_method.dynam_q.dynam_q import DynamQ


class ReinfEngine(Learning):

	def __init__(self, actions, method):

		# can receive a double value, default is 0.0
		self.__learn_memory =  SpreadMemory(0.01)

		# epsilon is the prob of explore the map 0.9 is 90%
		epsilon = 0.01
		self.__select_action = EGreedy(self.__learn_memory, actions, epsilon)


		self.__learn_method = self.__select_learning_method(self.__learn_memory, self.__select_action, method)


	def learning(self, s, a, r, sn, an = None):

		self.__learn_method.learning(s, a, r, sn, an)

	def select_action(self, s):

		return self.__select_action.select_action(s)


	def __select_learning_method(self, learn_memory, select_action, method):

		learn_method = None

		alpha    = 0.5
		gama     = 0.9
		num_sim  = 5
		max_dim  = 1000

		if method == 0:
			learn_method = SARSA(learn_memory, select_action, alpha, gama)

		elif method == 1:
			learn_method = QLearning(learn_memory, select_action, alpha, gama)

		elif method == 2:
			learn_method = QME(learn_memory, select_action, alpha, gama, num_sim, max_dim)

		elif method == 3:
			learn_method = DynamQ(learn_memory, select_action, alpha, gama, num_sim)

		return learn_method


	@property
	def learn_memory(self):
		return self.__learn_memory

