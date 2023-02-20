from operators.direction import Direction
from reinforcement_learning.reinf_engine import ReinfEngine

class ControlReinfLearn():

    def __init__(self, method = 0):

        self.__rmax = 100
        self.__state = None
        self.__action = None
        self.__operators = [dir.value for dir in Direction] # an action is an angle of movement
        self.__learn_engine = ReinfEngine(self.__operators, method)

    # implements a step of learning process
    def execute(self, perception):

        # selects the best action for a state
        sn = perception.position
        an = self.__learn_engine.select_action(sn)

        # the first perception has no previous
        if self.__state != None:
            r = self.__generate_reinforcement(perception)
            self.__learn_engine.learning(self.__state, self.__action, r, sn, an)
            

        self.__state = sn
        self.__action = an

        return self.__action

    # perception is the current position of the agent
    def __generate_reinforcement(self, perception):

        # returns the cost of the last movement
        reinforcement = perception.movement_cost * (-1)
        
        if perception.load:
            reinforcement = self.__rmax

        elif perception.collision:
            reinforcement = (self.__rmax*-1)

        return reinforcement

    def reset_s_a(self):

        self.__state = None
        self.__action = None

    
    @property
    def policy(self):
        return self.__learn_engine.learn_memory.memory