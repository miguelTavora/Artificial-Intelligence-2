class Planner:

	def plan(self, plan_model, initial_state, objectives):
		raise NotImplementedError("Interface method")

	def obtain_action(self, state):
		raise NotImplementedError("Interface method")

	def pending_plan(self):
		raise NotImplementedError("Interface method")

	def close_plan(self):
		raise NotImplementedError("Interface method")