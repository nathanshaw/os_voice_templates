#!/usr/bin/python3
from gpiozero import PWMOutputDevice as PWM
from time import sleep

pwm = PWM(4)

while True:
    print("motor on")
    pwm.on()
    sleep(1)
    print("motor off")
    pwm.off()
    sleep(1)
    print("motor 50%")
    pwm.value = 0.5
    sleep(2)
    print("motor 20%")
    pwm.value = 0.2
    sleep(2)
