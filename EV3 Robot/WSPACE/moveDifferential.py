#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveDifferential, SpeedRPM, MoveSteering
from ev3dev2.wheel import EV3EducationSetTire # gurpilaren zirkunferentzia: 176mm

def main():
    
    b = 120 # gurpil baten erdiko puntutik beste gurpilaren erdi puntura dagoen distantzia mm-tan
    mdiff = MoveDifferential(OUTPUT_B, OUTPUT_C, EV3EducationSetTire, b)
    robot = MoveSteering(OUTPUT_B, OUTPUT_C)
   
    mdiff.odometry_start(theta_degrees_start=0.0)
    
    mdiff.on_to_coordinates(SpeedRPM(40), 1000, 0)
    mdiff.turn_to_angle(SpeedRPM(40), 90)
    
    mdiff.on_to_coordinates(SpeedRPM(40), 1000, 1000)
    mdiff.turn_to_angle(SpeedRPM(40), 90)
    
    mdiff.on_to_coordinates(SpeedRPM(40), 0, 1000)
    mdiff.turn_to_angle(SpeedRPM(40), 90)
    
    mdiff.on_to_coordinates(SpeedRPM(40), 0, 0)
    mdiff.turn_to_angle(SpeedRPM(40), 90)
    

if __name__=="__main__":
    main()
    print("Square finished")
