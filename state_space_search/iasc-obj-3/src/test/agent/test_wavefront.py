from state_space_search.wavefront.wavefront import WaveFront

from plan.wavefront.plan_wavefront import PlanWaveFront
from agent.delib_control import DelibControl
from agent.agent_control import AgentControl
from user_interface.user_interface import UserInterface


search = WaveFront()

plan = PlanWaveFront(search)
control = DelibControl(plan)
#agent = AgentControl(control, "amb2.txt")
#agent = AgentControl(control, "amb1.txt", True)
agent = AgentControl(control, "amb3.txt", True)

ui = UserInterface(agent)

ui.loop()
