from plan.planner import Planner
from plan.sss.plan_problem import PlanProblem
from copy import deepcopy

class PlanSSS(Planner):

    def __init__(self, search_mec):

        self.__search_mec = search_mec
        self.__plan = []
        self.__route = []

    def plan(self, plan_model, initial_state, objectives):
        
        operators = plan_model.operators()
        plan_prob = PlanProblem(initial_state, objectives[0], operators)
        route = self.__search_mec.resolve(plan_prob)


        # update when is built a new route
        if len(self.__route) > 0:
            if objectives[0] != self.__route[-1].state:
                self.__route = deepcopy(route.solution)

        # set the route
        if len(self.__route) < len(route.solution):
            self.__route = deepcopy(route.solution)
            reversed(self.__route)


        if route is not None:
            self.__plan = [node.operator for node in reversed(route.solution)]
            self.__plan = self.__plan[1:]

    def obtain_action(self, state):
        if self.__plan:
            return self.__plan.pop(0)

    def pending_plan(self):
        return bool(self.__plan)

    def close_plan(self):
        self.__plan = None

    # route used to draw the arrows
    @property
    def route(self):
        return self.__route

    # used to paint the states
    @property
    def route_values(self):
        return None
