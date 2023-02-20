class ReifLearning:

	def __init__(self, learn_mem, sel_action, alpha, gama):

		self._learn_mem = learn_mem # instance LearningMemory
		self._sel_action = sel_action #instance from SelectAction
		self._alpha = alpha # double
		self._gama = gama # double


	def learning(self, s, a, r, sn, an):
		raise NotImplementedError("Abstract method")