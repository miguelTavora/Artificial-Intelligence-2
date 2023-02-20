import random

class TRModel():

	def __init__(self):

		self.__T = {}
		self.__R = {}

	# @args e : Experience
	def update(self, s, a, r, sn):

		self.__T[(s, a)] = sn # deterministic model
		self.__R[(s, a)] = r
		

	# @args n : int
	def sample(self):
		s, a = random.choice(list(self.__T.keys()))
		sn = self.__T[(s, a)]
		r = self.__R[(s, a)]
		return s, a, r, sn

