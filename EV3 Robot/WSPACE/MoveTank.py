#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_C, OUTPUT_B, MoveTank

from time import sleep

def main():
    
    bimot = MoveTank(OUTPUT_C, OUTPUT_B)
   
    for i in range(4):
        bimot.on(50, 50)
        sleep(5)
        bimot.on_for_degrees()

    bimot.off(brake = False)
    
if __name__=="__main__":
    main()
    