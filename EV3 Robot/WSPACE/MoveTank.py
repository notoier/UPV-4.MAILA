#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, MoveTank

from time import sleep

def main():
    
    bimot = MoveTank(OUTPUT_C, OUTPUT_B)
   
    for i in range(4):
        bimot.on_for_seconds(50, 50, 5)
        bimot.on_for_degrees(left_speed=50, right_speed= 75, degree = 90) 
    
    bimot.off(brake = False)
    
if __name__=="__main__":
    main()
    