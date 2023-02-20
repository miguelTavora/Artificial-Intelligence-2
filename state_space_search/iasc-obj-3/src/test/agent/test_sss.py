from state_space_search.best_first.weighted_a_star import WeightedAStar
from state_space_search.best_first.greedy_search import GreedySearch
from state_space_search.best_first.uniform_cost_search import UniformCostSearch
from state_space_search.best_first.aa_search import AASearch
from plan.sss.plan_sss import PlanSSS
from agent.delib_control import DelibControl
from agent.agent_control import AgentControl
from user_interface.user_interface import UserInterface


# 0 -> equal to AASearch, more than 0 goes more greedy
#search = WeightedAStar(weight = 0)
search = WeightedAStar(weight = 5)
#search = UniformCostSearch()
#search = GreedySearch()
#search = AASearch()


plan = PlanSSS(search)
control = DelibControl(plan)
#agent = AgentControl(control, "amb2.txt")
#agent = AgentControl(control, "amb1.txt", True)
agent = AgentControl(control, "amb3.txt")

ui = UserInterface(agent)

ui.loop()
