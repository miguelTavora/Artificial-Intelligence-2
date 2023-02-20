Organisation of the reinforcement_learning:
- Go to folder reinforcement_learning, 
- Then go to iasc-obj-2
- Inside doc -> architecture files obtained

- Inside src -> lib is the implementation
                -> test is the files to run

- To execute use the file env.bat
- To test all the algorithms you must go to the file: test_reinforcement.py
- Then uncomment the desired type of algorithm "control" and comment the current one
- To test in another environment, change the variable "agent".
- To change the speed of execution, click on the F key


---------------------------------------------------------


Organization of the state_space_search
- For the state space search - iasc-obj-3
- Inside doc -> architecture files obtained

- Inside src -> lib is the implementation
                -> test is the files to execute
				   
- Within test -> agent is the discrete agent
                 -> locations is a test with locations
				 
- Inside the agent -> test_sss.py file is the A* weighted search
                  -> test_wavefront.py is the front-wave method
				  
- To run it use the file test_sss.bat for A* weighted search
- To run front-wavefront use the file test_wavefront.bat
- To change the weights or environment change in the file test_sss.py for A* weighted search
- To change the environment in the wavefront use test_wavefront.py, 
- argument True in AgentControl is to restart when it reaches all targets
- Click F to change execution speed


--------


- For the optimisation - optimizacao
- Inside doc -> obtained architecture files

- Inside src -> lib is the implementation
                -> test is the files to run
				   
- To execute use the file env_n_queens.bat for the N-queens problem
- To execute the traveling salesman use env_travelling_salesman.bat
- The cost output appears in the cmd console
- To use classic Hill-Climbing is to change the .py file inside the		  