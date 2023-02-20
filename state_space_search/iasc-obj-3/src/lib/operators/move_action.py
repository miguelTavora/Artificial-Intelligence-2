from copy import deepcopy
from operators.enviroment import Enviroment


class MoveAction():

    def __init__(self, perception):
        
        self.__initial_world = deepcopy(perception.world)
        self.__world = perception.world
        self.__perception = perception

    def act(self, action):

        agent_pos = self.__perception.position
        new_pos = (agent_pos[0]+action[0], agent_pos[1] + action[1])

        if not self.__detect_collision(new_pos):
            self.__world[new_pos[1]][new_pos[0]] = Enviroment.CURRENT_POS.value
            self.__world[agent_pos[1]][agent_pos[0]] = Enviroment.EMPTY.value

        return action


    # must set every position on the list, with copy dont work
    def reset_world(self):

        for line in range(len(self.__world)):
            for column in range(len(self.__world[line])):
                self.__world[line][column] = self.__initial_world[line][column]


    def __detect_collision(self, new_pos):

        # detect if the new position 
        if self.__world[new_pos[1]][new_pos[0]] == Enviroment.OBSTACLE.value:
            self.__perception.collision = True
            return True

        return False

    
