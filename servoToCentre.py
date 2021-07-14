import PicoRobotics
import utime


board = PicoRobotics.KitronikPicoRobotics()

board.servoWrite(1,90)
utime.sleep_ms(5)
board.servoWrite(2,90)
utime.sleep_ms(5)
board.servoWrite(3,90)
utime.sleep_ms(5)
board.servoWrite(4,90)
utime.sleep_ms(10)
