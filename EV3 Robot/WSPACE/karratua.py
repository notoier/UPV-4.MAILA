#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B

from time import sleep

def main():
    motLeft = LargeMotor(OUTPUT_B)
    motRight = LargeMotor(OUTPUT_C)
    for i in range(4):
        motLeft.on(speed = 50)
        motRight.on(speed = 50)
        sleep(5)
        motRight.off()
        sleep(0.62)
    sleep(0.14)
    
    
    motLeft.off()
    motRight.off()

if __name__=="__main__":
    main()
    
