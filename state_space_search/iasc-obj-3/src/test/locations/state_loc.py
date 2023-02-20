from state_space_search.components.state import State

class StateLoc(State):

    # @args -> loc : String
    def __init__(self, loc):
        super().__init__()
        self.__loc = loc

    def __hash__(self):
        return self.__loc

    def __str__(self):
        return "Loc-" + str(self.__loc)