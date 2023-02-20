class Node():

     # Each node is refering a state, and comes from a predecessor
	# and a operator except the root node

     # @args -> state : State, operator : Operator, precedessor : Node
     def __init__(self, state, operator = None, predecessor = None):

          self.__state = state
          self.__operator = operator
          self.__predecessor = predecessor

          # only when a node has a precessor has a cost and depth
          # accumulated cost since this node until the last node
          self.__cost = self.__predecessor.cost + self.__operator.cost(predecessor, state) if predecessor is not None else 0
          # depth since the last node until the present
          self.__depth = predecessor.depth + 1 if predecessor is not None else 0


     @property
     def depth(self):
          return self.__depth


     @property
     def cost(self):
          return self.__cost

     @property
     def state(self):
          return self.__state

     @property
     def operator(self):
          return self.__operator

     @property
     def predecessor(self):
          return self.__predecessor

     def __str__(self):
          return "state: "+ str(self.__state) + ", operator: "+str(self.__operator) + ", cost:"+str(self.__cost)

     # need this method to compare between instances of node with heappush
     def __lt__(self, node_compare):
          return self.__cost < node_compare.cost


     

