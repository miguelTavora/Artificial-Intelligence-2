import random

class ExperienceMemory():

	def __init__(self, max_dim):

		self.__max_dim = max_dim
		self.__memory = [] 

	# @args e : Experience
	def update(self, e):

		if len(self.__memory) == self.__max_dim:
			self.__memory.pop(0)

		self.__memory.append(e)

	# @args n : int
	def sample(self, n):
		
		n_samples = min(n, len(self.__memory))
		return random.sample(self.__memory, n_samples)