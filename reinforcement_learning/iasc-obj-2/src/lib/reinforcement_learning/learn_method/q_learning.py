from reinforcement_learning.learn_method.reinf_learning import ReifLearning


class QLearning(ReifLearning):

	def __init__(self, learn_mem, sel_action, alpha, gama):

		super().__init__(learn_mem,sel_action, alpha, gama)
		

	# algorithm of the Q Learning
	def learning(self, s, a, r, sn, an = None):
		
		an = self._sel_action.max_action(sn)
		qsa = self._learn_mem.Q(s, a)
		qsnan = self._learn_mem.Q(sn, an)
		q = qsa + self._alpha * (r + self._gama * qsnan - qsa)
		self._learn_mem.update(s, a, q)