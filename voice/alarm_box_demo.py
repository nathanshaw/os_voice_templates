#!/usr/bin/env python3
import aiy.audio
from aiy.audio import say
import aiy.voicehat
from time import sleep
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probally because you need" +\
            "super user privileges. Try running script using sudo")

# this prgram was tested using the HC-SR501 Motion Detector
# That is is white one with a dome
# the code is set up to use the pins for Servo #5 on the hat

class MotionDetector():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)
    def watch(self):
        if GPIO.input(self.pin) > 0:
            print("MOTION DETECTED")
            return True

# this program uses an external proximity sensor to trigger a vocal alarm
def main():
    motion_detector = MotionDetector(24) # servo #5 on hat
    but = aiy.voicehat.get_button()


    print("initializing system")
    say("initializing system")
    sleep(1)

    while True:
        if motion_detector.watch() is True:
            say("STAY AWAY!")

if __name__ == "__main__":
    main()
