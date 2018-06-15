#!/usr/bin/env python3
# This program is for interfacing with mpi9265 or other
# MPU9250 style 9-DOF sensors

import aiy.audio
from aiy.audio import say
import aiy.voicehat
from time import sleep
import FaBo9Axis_MPU9250 as DOF

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
        print("---------------------")
        sleep(0.25)

if __name__ == "__main__":
    main()
