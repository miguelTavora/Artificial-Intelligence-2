from plan.planner import Planner
from plan.wavefront.plan_problem import PlanProblem
from copy import deepcopy

from state_space_search.mechanism.route import Route
from state_space_search.mechanism.node import Node

class PlanWaveFront(Planner):

    def __init__(self, search_mec):

        self.__search_mec = search_mec
        self.__plan = []
        self.__route = []
        self.__route_values = None

    def plan(self, plan_model, initial_state, objectives):
        
        operators = plan_model.operators()
        plan_prob = PlanProblem(initial_state, operators, objectives)
        route_values = self.__search_mec.resolve(plan_prob)
        self.__route_values = route_values
        
        if len(route_values) is not 0:
            solution = self.generate_solution(initial_state, operators, objectives, route_values)
            self.__plan = [node.operator for node in solution.solution] 

            # update when is built a new route
            if len(self.__route) > 0:
               if objectives[0] != self.__route[0].state:
                    self.__route = deepcopy(solution.solution)

            # set the route
            if len(self.__route) < len(solution.solution):
                self.__route = deepcopy(solution.solution)


    def obtain_action(self, state):
        if self.__plan:
            return self.__plan.pop(0)

    def pending_plan(self):
        return bool(self.__plan)

    def close_plan(self):
        self.__plan = None

    def generate_solution(self, state, operators, objectives, route_values):
        
        route = Route()
        node = Node(state)
        route.add_beginning(node)

        keys = self.__obtain_key_objectives(route_values)


        while len(objectives) != 0 and not state in keys:
            
            info = self.__obtain_new_state(state, operators, route_values)
            node = Node(info[0], info[1], node)
            route.add_beginning(node)
            state = info[0]

        return route

    def __obtain_new_state(self, state, operators, route_values):

        result = []

        for operator in operators:
            new_s = operator.apply(state)

            if new_s is not None:
                value = route_values.get(new_s)

                # the state must be on the wavefront values
                if value is not None:
                    #second_node = Node(second_state, operator, node)
                    result.append([new_s, operator, value])
        
        result.sort(key=self.__get_value, reverse=True)

        # must return only the best value, because the other values don't matter
        return result[0]

    def __get_value(self, element):
        return element[2]

    def __obtain_key_objectives(self, route_values):

        max_value = max(route_values.values())
        keys = [key for key in route_values.keys() if route_values.get(key) == max_value]
        print("keys:", keys)
        return keys

    # route used to draw the arrows
    @property
    def route(self):
        return self.__route

    # used to paint the states
    @property
    def route_values(self):
        return self.__route_values
                

