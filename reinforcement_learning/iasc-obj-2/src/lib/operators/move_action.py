from copy import deepcopy
from operators.enviroment import Enviroment


class MoveAction():

    def __init__(self, world, perception):
        
        self.__initial_world = deepcopy(world)
        self.__world = world
        self.__perception = perception
        self.end_episode = False

    def act(self, action):

        agent_pos = self.__perception.position
        new_pos = (agent_pos[0]+action[0], agent_pos[1] + action[1])


        # set the cost of the movement of the agent
        cost = self.__perception.cost(agent_pos, new_pos)
        self.__perception.movement_cost = cost

        if not self.__detect_collision(new_pos):
            # detects if the agent will reach the objective, if reached all of them reset
            reset = self.__detect_target(new_pos)

            self.__world[new_pos[1]][new_pos[0]] = Enviroment.CURRENT_POS.value
            self.__world[agent_pos[1]][agent_pos[0]] = Enviroment.EMPTY.value

            if reset:
                print("DEU RESET")
                self.__reset_world()
                self.end_episode = True

        return action


    def __detect_collision(self, new_pos):

        # detect if the new position 
        if self.__world[new_pos[1]][new_pos[0]] == Enviroment.OBSTACLE.value:
            self.__perception.collision = True
            return True

        return False

    def __detect_target(self, new_pos):

        if self.__world[new_pos[1]][new_pos[0]] == Enviroment.TARGET.value:
            self.__perception.load = True

            # when the condition is True, the agent reached all the objectives and must reset the map and agent
            num_targets = len(self.__perception.targets)
            if num_targets == 1:
                return True

        return False
            

    # must set every position on the list, with copy dont work
    def __reset_world(self):

        for line in range(len(self.__world)):
            for column in range(len(self.__world[line])):
                self.__world[line][column] = self.__initial_world[line][column]
