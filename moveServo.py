import PicoRobotics
import utime


board = PicoRobotics.KitronikPicoRobotics()

while True:
    for servo  in range (1,5,1):
        board.servoWrite(servo,180)
        utime.sleep(2)
        board.servoWrite(servo,0)
        utime.sleep(2)
        board.servoWrite(servo,90)
