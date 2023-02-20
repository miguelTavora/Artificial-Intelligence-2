from control.control_reinf_learn import ControlReinfLearn
from control.agent_control import AgentControl
from user_interface.user_interface import UserInterface


#control =  ControlReinfLearn(0) # SARSA
#control =  ControlReinfLearn(1) # Q-Learning
#control =  ControlReinfLearn(2) # QME
control =  ControlReinfLearn(3) # Dyna-Q

#agent = AgentControl(control, "amb1.txt")
agent = AgentControl(control, "amb2.txt")

ui = UserInterface(agent)
ui.loop()

##### Click F -> to slow or speed up the simulation