class WaveFrontMemory():

    def __init__(self):
        self.clear()

    @property
    def V(self):
        return self.__V

    @property
    def wavefront(self):
        return self.__wavefront

    def clear(self):
        self.__V = {}
        self.__wavefront = []

    def insert_wavefront(self, s):
        self.__wavefront.append(s)

    def remove(self):
        return self.__wavefront.pop(0)

    def obtain_value(self, key):
        return self.__V.get(key)

    def insert_V(self, new_s, v):
        self.__V[new_s] = v


    
