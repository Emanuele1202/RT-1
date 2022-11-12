# PYTHON ROBOTICS SIMULATOR
## Research Track I : Assignment 1
### Professor [Carmine Recchiuto]
### Student: [Emanuele Buzzurro]

##Project Description: 


### Workflow ###

The enviroment used for this project was the portable robot simulator developed by [Student Robotics](https://studentrobotics.org). The arena has a golden and silver tokens, as follows:

![arena](https://github.com/Emanuele1202/Research-Track-I/blob/master/Assignment1/Initial_arena_structure.png) 

The goal for this assignment was about making a robot move continuously around the arena in order to grab one silver token at a time, and when it grabs one, the robot must bring it close to a golden token and then releasing it as follows:

![final](https://github.com/Emanuele1202/Research-Track-I/blob/master/Assignment1/Final_arena_structure.png)

The main part of the work was about managing the fact that the robot should not grab two times the same silver token and also that it should not bring them to the same golden token.
    
    
### reach_silver_token & reach_golden_token ###
 
This functions are used to reach the silver/golden token saw in R.see; in fact they allow the robot to align correctly with the token to reach and subsequently they move the robot forward until the token is situated at a specific distance. 


### find_silver_token & find_golden_token ###
 
This functions return the distance and the rotation used from the reach_token funtion. It also catch the offset of the token in R.see in order to let other functions to add it to the lists: 
	-golden_box_list
	-silver_box_list
 which keeps track of the tokens already "used".
 
##FLOWCHART

![flowchart](https://github.com/Emanuele1202/Research-Track-I/blob/master/Assignment1/flowcharts.png)
 
 
## HOW TO RUN THE CODE:

Open a terminal shell, move to the robot-sim directory and run:
*$python2 run.py exercise1.py* 


## POSSIBLES FURTHER IMPLEMENTATIONS:

	- In order to make our robot more 'intelligent' and 'efficient' we can add a further cycle that evaluate the distance between the grabbed silver box and all the possible golden box to 				 reach, and choose to bring it to the nearest golden box

	- We could also think about adding a function that allow an initial scan of the arena in order to dinamically modify the number of cycle of the main function 

	- Last but not least it can also be interest to add a function that avoid all the tokens in between the path of the robot, while reaching the desired token
