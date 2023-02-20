import numpy as np
import matplotlib.pyplot as plt

class GraphTravelling():

    def __init__(self, coordinates, solution):

        self.__coordinates = coordinates
        self.__solution = solution

    
    def plot_path(self):
        
        coord = np.array([self.__coordinates[city] for city in self.__solution])
        city = [city for city in self.__solution]

        fig, ax = plt.subplots()
        
        for i, txt in enumerate(coord):
            ax.annotate(city[i], (coord[:, 0][i], coord[:, 1][i]))

        plt.plot(coord[:, 0], coord[:, 1], 'r')
        plt.show()