class Problem():

    # @args -> initial_state : State, operators : Operator[]
    def __init__(self, initial_state, operators):

        self.__initial_state = initial_state
        self.__operators = operators

    @property
    def initial_state(self):
        return self.__initial_state

    @property
    def operators(self):
        return self.__operators


    # @args -> state : State
    # returns boolean
    def objective(self, state):
         
        raise NotImplementedError("Abstract method")

