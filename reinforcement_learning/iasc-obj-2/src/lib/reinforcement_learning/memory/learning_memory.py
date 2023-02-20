class LearningMemory:

	# @args s : state, a : action, q : double
	def update(self, s, a, q):
		raise NotImplementedError("Method from a interface")

	# @args s : state, a : action
	def Q(self, s, a):
		raise NotImplementedError("Method from a interface")