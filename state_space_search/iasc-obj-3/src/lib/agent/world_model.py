from plan.model_plan import ModelPlan
from operators.direction import Direction
from agent.operator_move import OperatorMove

class WorldModel(ModelPlan):

    def __init__(self):

        self.__changed = False
        self.__state = None
        self.__objectives = None
        self.__operators = [OperatorMove(self, dir.value) for dir in Direction]
        self.__elements = None

    @property
    def changed(self):
        return self.__changed

    def state(self):
        return self.__state

    def operators(self):
        return self.__operators

    def update(self, perception):

        self.__state = perception.position

        # only when the agent reaches one target its needed a new plan
        if perception.targets != self.__objectives:
            self.__objectives = perception.targets
            self.__elements = perception.elements
            self.__changed = True
        else:
            self.__changed = False

    def obtain_elements(self, state):
        return self.__elements.get(state)
