from reinforcement_learning.learn_method.q_learning import QLearning
from reinforcement_learning.learn_method.dynam_q.tr_model import TRModel


class DynamQ(QLearning):

	def __init__(self, learn_mem, sel_action, alpha, gama, num_sim):

		super().__init__(learn_mem, sel_action, alpha, gama)
		self.__num_sim = num_sim
		self.__model = TRModel()


	def learning(self, s, a, r, sn, an = None):
		
		super(DynamQ, self).learning(s, a, r, sn)
		self.__model.update(s, a, r, sn)
		self.simulate()

	def simulate(self):

		for i in range(self.__num_sim):

			s, a, r, sn = self.__model.sample()
			super(DynamQ, self).learning(s, a, r, sn)