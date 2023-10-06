#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_C, OUTPUT_B, MoveSteering 
from time import sleep


def forward(rob, s, v, tsec): 
    rob.on_for_seconds(s, v, tsec)
def turnLeft(rob, s, v, tsec):
    rob.on_for_seconds(s, v, tsec)

def main():
    robot = MoveSteering(OUTPUT_C, OUTPUT_B) 
for i in range(0, 4):
    forward(robot, 0, 50, 2)
    turnLeft(robot, 50, 50, 2) 

if __name__=="__main__": 
    main()