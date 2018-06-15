#!/usr/bin/env python3
from gpiozero import PWMOutputDevice as PWM
from time import sleep
import aiy.audio
from aiy.audio import say
import aiy.cloudspeech
import aiy.voicehat
import RPi.GPIO as GPIO
from time import sleep


def main():
    rec = aiy.cloudspeech.get_recognizer()
    rec.expect_phrase('min')
    rec.expect_phrase('max')
    rec.expect_phrase('mid')
    rec.expect_phrase('off')

    aiy.audio.get_recorder().start()

    but = aiy.voicehat.get_button()

    led = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)

    pwm = PWM(4)

    print("initializing system")

    say("initializing system")
    sleep(1)

    while True:
        say("press button and say min, max or mid to contol the D C Motor")
        print("press button and min, max or mid to contol the D C Motor")
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
                pwm.value = 0.2
            elif 'max' in text:
                say("max")
                print("max")
                pwm.value = 0.8
            elif 'mid' in text:
                say("mid")
                print("mid")
                pwm.value = 0.4
            elif 'off' in text:
                say("off")
                print("off")
                pwm.value = 0.0
            else:
                pwm.value = 0.0
                say("i'm sorry i heard, " + text + " which is not a valid command")
                print("i'm sorry i heard, " + text +  " which is not a valid command")
        GPIO.output(led, GPIO.LOW)

if __name__ == "__main__":
    main()
