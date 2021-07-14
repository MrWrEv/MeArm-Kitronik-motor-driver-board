#servoMove.py
# test code that ramps each servo individually from 0-180-0 
import PicoRobotics
import utime


board = PicoRobotics.KitronikPicoRobotics()
while True:
        
    for servo in range (1,5,1):
        for degrees in range (180):
            board.servoWrite(servo, degrees)
            utime.sleep_ms(10)
        for degrees in range(180):
            board.servoWrite(servo, 180-degrees)
            utime.sleep_ms(10)
        board.servoWrite(servo, 90)
        utime.sleep_ms(50)
