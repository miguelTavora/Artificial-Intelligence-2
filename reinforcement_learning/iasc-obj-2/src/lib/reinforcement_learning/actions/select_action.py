class SelectAction:
	
	# @args s : state
	# return action
	def select_action(self, s):
		raise NotImplementedError("Method from a interface")


	# @args s : state
	# return action
	def max_action(self, s):
		raise NotImplementedError("Method from a interface")