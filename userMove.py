import PicoRobotics
import utime

board = PicoRobotics.KitronikPicoRobotics()

# 1-up/down     || 2-jaws
# 3-left/right  || 4-forward/backward
# 1 = 
for servo in range(1,5,1):
    board.servoWrite(servo,90)

again = "yes"

while again == "yes":
    servo = int(input("servo? "))
    degrees = int(input("0-180"))
    if degrees > 180:
        degrees = 179
    elif degrees < 1:
        degrees = 2
    board.servoWrite(servo,degrees)
