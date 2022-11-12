from __future__ import print_function
from ast import operator
from lib2to3.pgen2 import token
from re import T
#from operator import length_hint

import time
from sr.robot import *

R = Robot()

a_th = 2.0
d_th = 0.4
global silver_box_list #global list that contains silver token already taken
silver_box_list = []
global golden_box_list #global list that contains golden token already taken
golden_box_list = []
global g_variable #store the offset of the golden token 
global s_variable #store the offset of the silver token


def drive(speed, seconds):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0


def turn(speed, seconds):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_silver_token():
    dist = 100
    global s_variable
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER and token.info.offset not in silver_box_list:
            dist = token.dist
            rot_y = token.rot_y
            s_variable= token.info.offset
    if dist == 100:
        return -1, -1
    else:
        return dist, rot_y


def find_golden_token():
    dist = 100
    global g_variable
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and token.info.offset not in golden_box_list:
            dist = token.dist
            rot_y = token.rot_y
            g_variable = token.info.offset
    if dist == 100:
        return -1, -1
    else:
        return dist, rot_y

def reach_silver_token(): #function used to reach the silver token in R.see
    silver= True 
    while silver==True:
        #print(silver_box_list) #uncomment to debug
        dist, rot_y = find_silver_token()
        if dist == -1:  # if no token is detected, we make the robot turn
            print("I don't see any silver token!!")
            turn(+10, 1)
        elif dist < d_th:  # if we are close to the token, we try grab it.
            print("Found the silver one!")
            if silver==True:
                R.grab()  # if we grab the token, we move the robot forward and on the right, we release the token, and we go back to the initial position
                print("Gotcha!")
                #print("Silver postgrab ma preappend: ",silver_box_list) #uncomment to debug
                silver_box_list.append(s_variable) #add the offset of the token to the list
                #print("Silver post append",silver_box_list) #uncomment to debug
                turn(25, 2)
                silver = False
            else:
                print("Aww, I'm not close enough.") 
        elif -a_th <= rot_y <= a_th:  # if the robot is well aligned with the token, we go forward
            print("Ah, that'll do.")
            drive(25, 0.5)
        elif rot_y < -a_th:  # if the robot is not well aligned with the token, we move it on the left or on the right
            print("Left a bit...")
            turn(-2, 0.5)
        elif rot_y > a_th:
            print("Right a bit...")
            turn(+2, 0.5)

def reach_golden_token(): #function used to reach the golden token in R.see
    silver=False
    while silver==False:
        #print(golden_box_list) #uncomment to debug
        dist, rot_y = find_golden_token()
        if dist == -1:  # if no token is detected, we make the robot turn
            print("I don't see any golden token!!")
            turn(+10, 1)
        elif dist < 1.3*d_th:  # if we are close to the token, we try grab it.
            print("Releasing it!")
            if silver==False:
                R.release()
                silver = True 
                #print("Golden pre append: ", golden_box_list) #uncomment to debug
                golden_box_list.append(g_variable) #add the offset of the token to the list
                #print("Golden post append: ", golden_box_list) #uncomment to debug
                return silver
        elif -a_th <= rot_y <= a_th:  # if the robot is well aligned with the token, we go forward
            print("Ah, that'll do.")
            drive(20, 0.5)
        elif rot_y < -a_th:  # if the robot is not well aligned with the token, we move it on the left or on the right
            print("Left a bit...")
            turn(-2, 0.5)
        elif rot_y > a_th:
            print("Right a bit...")
            turn(+2, 0.5)

while len(silver_box_list)<6:
    reach_silver_token()
    reach_golden_token()
    drive(-10, 2)
    turn(15, 2)
print("My job is done here!!")
