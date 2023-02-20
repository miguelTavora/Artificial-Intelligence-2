class Operator():

     # shift on the states


     # allow to apply a operator to a state to make a transition on the state
     # @args -> state : State
     # returns State
     def apply(self, state):

          raise NotImplementedError("Interface method")

     
     # allows obtain the cost associated with state transaction
     # @args -> state : State, second_state : State
     # returns float
     def cost(self, state, second_state):

          raise NotImplementedError("Interface method")


     # returns string
     def __str__(self):

          raise NotImplementedError("Interface method")

