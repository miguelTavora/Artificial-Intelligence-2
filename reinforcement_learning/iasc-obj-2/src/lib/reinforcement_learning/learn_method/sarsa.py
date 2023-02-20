from reinforcement_learning.learn_method.reinf_learning import ReifLearning


class SARSA(ReifLearning):

	def __init__(self, learn_mem, sel_action, alpha, gama):

		super().__init__(learn_mem, sel_action, alpha, gama)

	def learning(self, s, a, r, sn, an):
		
		qsa = self._learn_mem.Q(s, a)
		qsnan = self._learn_mem.Q(sn, an)
		q = qsa + self._alpha * (r + self._gama * qsnan - qsa)
		self._learn_mem.update(s, a, q)