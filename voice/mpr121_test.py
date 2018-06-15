#!/usr/bin/env python3
# This program is for interfacing with mpi9265 or other
# MPU9250 style 9-DOF sensors

import aiy.audio
from aiy.audio import say
import aiy.voicehat
from time import sleep
from piripherals import MPR121

def main():

    cap = MPR121()

    print("initializing system")
    say("initializing system")
    sleep(1)

    while True:
        for i in range(12):
            mpr.on_touch(i, lambda *x: print(x))

if __name__ == "__main__":
    main()
