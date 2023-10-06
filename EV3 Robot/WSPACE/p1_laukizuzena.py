#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, MoveTank, MoveDifferential, SpeedRPM, MoveSteering
from ev3dev2.wheel import EV3EducationSetTire # gurpilaren zirkunferentzia: 176mm

from time import sleep

def main():
    
    bimot = MoveTank(OUTPUT_C, OUTPUT_B)
    b = 120 # gurpil baten erdiko puntutik beste gurpilaren erdi puntura dagoen distantzia mm-tan
    mdiff = MoveDifferential(OUTPUT_B, OUTPUT_C, EV3EducationSetTire, b)
    robot = MoveSteering(OUTPUT_B, OUTPUT_C)
    
if __name__=="__main__":
    main()
    