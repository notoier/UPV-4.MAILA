#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_D, OUTPUT_A

from time import sleep

def main():
    motLeft = LargeMotor(OUTPUT_A)
    motRight = LargeMotor(OUTPUT_D)
    motLeft.on(speed = 50)
    motRight.on(speed = 50)
    sleep(2)
    motLeft.off()
    motRight.off()

if __name__=="__main__":
    main()
    
