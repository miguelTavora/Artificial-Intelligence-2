import random
from reinforcement_learning.actions.select_action import SelectAction

class EGreedy(SelectAction):

	def __init__(self, learn_mem, actions, epsilon):

		self.__learn_mem = learn_mem
		self.__actions = actions #List <Action>
		self.__epsilon = epsilon # double varies between 0 - 1


	def select_action(self, s):
		# generate a number between 0 and 1
		random_number = random.random() 

		# epsilon is the prob of the value being random
		if random_number <= self.__epsilon:
			return self.explore_action()

		# if not random action returns greedy action
		return self.greedy_action(s)

	# returns the action that the highest reward known
	def greedy_action(self, s):

		return self.max_action(s)

	# returns a random action from the ones that can be done
	def explore_action(self):
		return random.choice(self.__actions)


	def max_action(self, s):
		# must shuffle to guarantee that is not choosed always the same action
		random.shuffle(self.__actions)

		# the max functions as argmax
		return max(self.__actions, key=lambda a: self.__learn_mem.Q(s, a))