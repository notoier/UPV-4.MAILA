#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B

from time import sleep

def main():
    motLeft = LargeMotor(OUTPUT_B)
    motRight = LargeMotor(OUTPUT_C)
    motLeft.on(speed = 20)
    motRight.on(speed = 20)
    sleep(10)
    motLeft.off()
    motRight.off()

if __name__=="__main__":
    main()
    
