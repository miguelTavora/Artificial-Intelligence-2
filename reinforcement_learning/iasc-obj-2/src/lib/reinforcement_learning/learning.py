class Learning:


	# return an action
	# @args -> s : state
	def select_action(self, s): 
		raise NotImplementedError("Method from a interface")


	# return void
	# @args -> s : state, a : action, r : double, sn : state, an : action
	def learning(self, s, a, r, sn, an):
		raise NotImplementedError("Method from a interface")