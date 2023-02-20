from reinforcement_learning.memory.learning_memory import LearningMemory


class SpreadMemory(LearningMemory):

	def __init__(self, default_value = 0.0):

		self.__default_value = default_value
		self.__memory = {} # associative memory

	# @args s : state, a : action, q : double
	def update(self, s, a, q):
		self.__memory[(s, a)] = q

	# @args s : state, a : action
	def Q(self, s, a):
		return self.__memory.get((s, a), self.__default_value)


	@property
	def memory(self):
		return self.__memory