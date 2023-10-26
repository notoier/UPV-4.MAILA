#!/usr/bin/env python3

from fcntl import F_GETLEASE
from ev3dev2.sensor import Sensor
from time import sleep
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, MoveTank

def printLSA(lsa):
    values = []
    value = 0
    for i in range(0,8):
        value = lsa.value(i)
        values.append(value)    
        print("i=%d value=%d"%(i,value))
        print("--------------------------------")
    
    center = sum(values[3:5]) / 2
    return center, values

def main():
    lsa = Sensor()
    bimot = MoveTank(OUTPUT_C, OUTPUT_B)
    bimot.on(20, 20)
    while True:
        zentro, value = printLSA(lsa)
        if zentro > 15:
            erdi = len(value) // 2
            ezkerra = sum(value[:erdi]) / 5
            eskuina = sum(value[erdi:]) / 4
            
            if eskuina < ezkerra:
                bimot.on(20, 10)            
                sleep(0.1)  
                zentro, value = printLSA(lsa)
                if zentro < 15:
                    bimot.on(20,20)
            else:
                bimot.on(10,20)           
                sleep(0.1)  
                zentro, value = printLSA(lsa)
                if zentro < 15:
                    bimot.on(20,20)    
        sleep(0.1)
            
            
if __name__=="__main__":
    main()