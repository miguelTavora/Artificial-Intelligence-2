from agent.world_model import WorldModel


class DelibControl():

    def __init__(self, plan):
        self.__plan = plan
        self.__world_model = WorldModel()
        self.__objectives = None

    def execute(self, perception):

        self.__assimilate(perception)
        if self.__reconsider():
            self.__deliberate(perception)
            self.__planning()

        return self.__execute_action()

    def __assimilate(self, perception):
        self.__world_model.update(perception)


    def __reconsider(self):
        return self.__world_model.changed or not self.__plan.pending_plan() or self.__objectives is None

    def __deliberate(self, perception):
        self.__objectives = perception.targets

    def __planning(self):
        if self.__objectives:
            self.__plan.plan(self.__world_model, self.__world_model.state(), self.__objectives)

        else:
            self.__plan.close_plan()

    def __execute_action(self):
        operator = self.__plan.obtain_action(self.__world_model.state())
        if operator:
            return operator.move_dist

    @property
    def route(self):
        return self.__plan.route

    @property
    def route_values(self):
        return self.__plan.route_values