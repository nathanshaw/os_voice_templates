#!/usr/bin/env python3
import aiy.audio
from aiy.audio import say
import aiy.cloudspeech
import aiy.voicehat
import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep


def main():
    rec = aiy.cloudspeech.get_recognizer()
    rec.expect_phrase('min')
    rec.expect_phrase('max')
    rec.expect_phrase('mid')

    aiy.audio.get_recorder().start()

    servo = Servo(26)
    but = aiy.voicehat.get_button()

    led = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)

    print("initializing system")

    say("initializing system")
    sleep(1)

    while True:
        say("press button and say min, max or mid to control servo")
        GPIO.output(led, GPIO.HIGH)
        print("press button to command servo")
        but.wait_for_press()
        print("listening")
        text = rec.recognize()

        if text is None:
            GPIO.output(led, GPIO.LOW)
            say("That is not a valid command!")
        else:
            text = text.lower()
            GPIO.output(led, GPIO.HIGH)
            if 'min' in text:
                say("min")
                print("min")
                servo.min()
            elif 'max' in text:
                say("max")
                print("max")
                servo.max()
            elif 'mid' in text:
                say("mid")
                print("mid")
                servo.mid()
            else:
                say("i'm sorry i heard, " + text + " which is not a valid command")
                print("i'm sorry i heard, " + text +  " which is not a valid command")
        GPIO.output(led, GPIO.LOW)

if __name__ == "__main__":
    main()
