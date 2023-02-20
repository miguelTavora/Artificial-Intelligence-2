from reinforcement_learning.learn_method.q_learning import QLearning
from reinforcement_learning.learn_method.qme.experience_memory import ExperienceMemory


class QME(QLearning):

	# @args learn_mem -> LearningMemory, sel_action -> SelectAction, 
	# alpha -> double, gama -> double, num_sim -> int, dim_max -> int
	def __init__(self, learn_mem, sel_action, alpha, gama, num_sim, max_dim):
		super().__init__(learn_mem, sel_action, alpha, gama)

		self.__num_sim = num_sim
		self.__exp_memory = ExperienceMemory(max_dim)


	# algorithm of the Q Learning with episodic memory
	def learning(self, s, a, r, sn, an = None):
		
		super(QME, self).learning(s, a, r, sn)
		e = (s, a, r, sn)
		self.__exp_memory.update(e)
		self.simulate()

	def simulate(self):

		samples = self.__exp_memory.sample(self.__num_sim)

		for (s, a, r, sn) in samples:

			super(QME, self).learning(s, a, r, sn)