#!/usr/bin/env python3
from gpiozero import Servo
from time import sleep
from random import random

# servo 0 - 26
servo0 = Servo(26)
# servo 1 - 6
servo1 = Servo(6)
# servo 2 - 13
servo2 = Servo(13)
# servo 3 - 5
servo3 = Servo(5)
# servo 4 - 12
servo4 = Servo(12)
# servo 5 - 24
servo5 = Servo(24)

while True:
    print("min")
    servo0.min()
    servo3.min()
    sleep(random())
    print("mid")
    servo0.mid()
    servo3.mid()
    sleep(random())
    print("max")
    servo0.max()
    servo3.max()
    sleep(random())

if __name__ == '__main__':
    main()

