from operators.agent import Agent

class AgentControl(Agent):

    def __init__(self, control, filename="amb1.txt"):
        # to access the methods and varibles of the extended class
        super().__init__(filename)
        self.__control = control

    def execute(self):

        # updates the varibles 
        self.__update_perception()
        action = self.__process(self.perception)

        # reset the variables of the enviroment
        self.perception.reset()

        # when the target is reached by the agent
        if self.move_action.end_episode:
            self.__control.reset_s_a()
            self.move_action.end_episode = False
        
        self.__act(action)

    def __update_perception(self):
        
        self.perception.detect()

    def __process(self, perception):

        return self.__control.execute(perception)

    def __act(self, action):

        if action is not None:
            self.move_action.act(action)
        
        
    @property
    def policy(self):
        return self.__control.policy


