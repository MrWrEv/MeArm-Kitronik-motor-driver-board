# MeArm-Kitronik-motor-driver-board
Code for use with the MeArm kit and the Kitronik Motor Driver board 

picoRobotics.py needs to be copied over to the Raspberry Pi Pico in order to use this code.
moveServo.py is a servo test, which moves each servo in turn, across the full 180° of movement of each servo
servoToCentre.py resets each servo position to 90°, which is theoretically centre.
userMove.py adds a tiny bit of front end to the code and hopefully, will stop the servo from moving past its end point and stalling. 🤞
