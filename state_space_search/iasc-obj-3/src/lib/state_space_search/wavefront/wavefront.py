from state_space_search.mechanism.search_mechanism import SearchMechanism
from state_space_search.wavefront.wavefront_memory import WaveFrontMemory
import math

class WaveFront(SearchMechanism):

    def __init__(self, gama = 0.7, max_value = 100):
        super().__init__()
        self.__gama = gama
        self.__max_value = max_value


    # returns -> WaveFrontMemory
    def initialize_memory(self):
        return WaveFrontMemory()
        
    
    def resolve(self, problem, max_depth = 1_999_999):
        
        # returns a list of all objectives
        objectives = problem.objective(None)
        self.search_memory.clear()

        for s in objectives:
            self.search_memory.insert_V(s, self.__max_value)
            self.search_memory.insert_wavefront(s)

        while self.search_memory.wavefront:
            #print("DENTRO LOOP ")
            s = self.search_memory.remove()
            for new_s in self.__obtain_neighbour(problem, s):
                v = self.search_memory.obtain_value(s) * math.pow(self.__gama, self.__dist(s, new_s))

                if (self.search_memory.obtain_value(new_s) is not None) and (v > self.search_memory.obtain_value(new_s)):
                    self.__insert_values(new_s, v)

                elif v > -math.inf and (self.search_memory.obtain_value(new_s) is None):
                   self.__insert_values(new_s, v)

        return self.search_memory.V


    def __obtain_neighbour(self, problem, s):
        
        neighbour_states = []

        for operator in problem.operators:
            state = operator.apply(s)
            if state != None:
                 neighbour_states.append(state)

        return neighbour_states

    def __dist(self, state1, state2):
        current_x, current_y = state1
        final_x, final_y = state2
        vector = (current_x - final_x, current_y - final_y)
        result = math.sqrt((vector[0] ** 2) + (vector[1] ** 2))
        return result

    def __insert_values(self, new_s, v):
        self.search_memory.insert_V(new_s, v)
        self.search_memory.insert_wavefront(new_s)

