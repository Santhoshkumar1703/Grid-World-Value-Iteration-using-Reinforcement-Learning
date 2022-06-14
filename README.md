# R.L_FINAL-PROJECT

# Grid World Value Iteration:
The goal of this project is to create a grid world environment and use value iteration to discover the best policy. The value iteration pseudocode that was programmed and tested is shown below.

![alt text](https://github.com/santhoshkumar170302/R.L_FINAL-PROJECT/blob/1254d827d8dde7243e93e39dbe1b3f20b4193f93/value%20iteration.png)


Value iteration is a technique for determining the best MDP policy and its value.


Value iteration begins at the "end" and goes backward, revising a Q* or V* estimate. It employs an artificial end point since there is no genuine end. Let Vk be the value function and Qk be the Q-function, assuming there are k stages to go. They may be defined in a recursive manner. To acquire the functions for k+1 stages to go from the functions for k stages to go, value iteration begins with an arbitrary function V0 and employs the following equations:


                                                          Qk+1(s,a)	= ∑s' P(s'|s,a) (R(s,a,s')+ γVk(s'))  for k ≥ 0
                                                              Vk(s)	= maxa Qk(s,a)  for k>0.


It can either save the V[S] array or the Q[S,A] array. Saving the V array results in less storage, but it is more difficult to determine an optimal action, and one more iteration is needed to determine which action results in the greatest value.

# Environment of Grid World

The Grid World, we created is a real-time example for a basic algorithm test utilizing value iteration. The student from Ramanujan hostel (source) must arrive at our college's main entrance (destination), by avoiding obstacles such as the academic building and canteen. As indicated in the diagram below.

![GRID WORLD GUI](https://github.com/santhoshkumar170302/R.L_FINAL-PROJECT/blob/72f88485e10ed5f126b4525cbeaa44fe312398d6/Grid%20world.png)

•	The GUI Environment of this project is designed by Tkinter and PIL Image

•	The Agent is Value Iteration

•	Agent: We will Initialize a 2D list of all the actions, the value iteration algorithm generates the all possible actions and the optimal actions from the grid world

•	Environment: The environment is the frontend designed which is integrated with the backend by value iteration agents. We are designed canvas function in order to start the import the images. 

•	In this grid world the rewards of the grid each grid set as zero except destination and obstacles  

•	The rewards for the destination is ‘+1’ and rewards for the obstacles is ‘-1’.

•	By the value iteration it print all possible policy to reach destination

•	As in GUI we need to click on the print policy button first, then click on the move button so the source starts to search the possible paths to reach the destination.

•	 And we can also print the optimal path to reach the destination.

![GRID WORLD GUI](https://github.com/santhoshkumar170302/R.L_FINAL-PROJECT/blob/2bbd14bf7488a065eaa9ef00b213286e10243eed/GRID%20WORLD-2.png)



•	From above figure we can observe that all possible policy has been print in arrow as right, left, up and down.

•	After printing all policy click on move button so source start move in different paths and reach to destination. 

