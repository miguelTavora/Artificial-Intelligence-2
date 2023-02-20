class State():

	def __eq__(self, other):
	   
		return hash(self) == hash(other)

	def __hash__(self):

		raise NotImplementedError("Abstract method")
		

	def __str__(self):
		return str(hash(self))

