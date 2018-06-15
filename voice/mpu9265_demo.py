#!/usr/bin/env python3
import aiy.audio
from aiy.audio import say
import aiy.voicehat
from time import sleep
import FaBo9Axis_MPU9250 as DOF

# this prgram was tested using the HC-SR501 Motion Detector
# That is is white one with a dome
# the code is set up to use the pins for Servo #5 on the hat


# this program uses an external proximity sensor to trigger a vocal alarm
def main():
    dof = DOF.MPU9250()

    print("initializing system")
    say("initializing system")
    sleep(1)

    while True:
        a = dof.readAccel()
        g = dof.readGyro()
        m = dof.readMagnet()
        print(a)
        print(g)
        print(m)
        if a['x'] < 0 or a['y'] < 0 or a['z'] < 0:
            print("dont rock the boat!")
            say("Hey dont rock the boat!")
        print("---------------------")
        sleep(0.25)


if __name__ == "__main__":
    main()
