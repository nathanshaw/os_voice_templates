#!/usr/bin/env python3
from gpiozero import PWMOutputDevice as PWM
from time import sleep
import aiy.audio
from aiy.audio import say
import aiy.cloudspeech
import aiy.voicehat
from time import sleep


def main():
    rec = aiy.cloudspeech.get_recognizer()
    rec.expect_phrase('min')
    rec.expect_phrase('max')
    rec.expect_phrase('mid')
    rec.expect_phrase('percent')
    rec.expect_phrase('%')
    rec.expect_phrase('off')

    aiy.audio.get_recorder().start()

    led = aiy.voicehat.get_led()

    but = aiy.voicehat.get_button()

    pwm = PWM(4)

    led.set_state(aiy.voicehat.LED.ON)
    say("press button to control motor")
    led.set_state(aiy.voicehat.LED.BLINK)
    sleep(1)

    while True:
        print("press button for motor control")
        but.wait_for_press()
        led.set_state(aiy.voicehat.LED.ON)
        pwm.value = 0.0
        print("How fast would you like the Motor to go?")
        say("How fast would you like the Motor to go?")
        led.set_state(aiy.voicehat.LED.BLINK)
        text = rec.recognize()

        if text is None:
            led.set_state(aiy.voicehat.LED.OFF)
            print("That is not a valid command!")
            say("That is not a valid command!")
        else:
            text = text.lower()
            led.set_state(aiy.voicehat.LED.ON)
            if 'min' in text:
                print("min")
                say("min")
                pwm.value = 0.2
                led.set_state(aiy.voicehat.LED.OFF)
            elif 'max' in text:
                print("max")
                say("max")
                pwm.value = 0.8
                led.set_state(aiy.voicehat.LED.OFF)
            elif 'mid' in text:
                print("mid")
                say("mid")
                pwm.value = 0.4
                led.set_state(aiy.voicehat.LED.OFF)
            elif 'off' in text:
                print("off")
                say("off")
                pwm.value = 0.0
                led.set_state(aiy.voicehat.LED.BLINK)
            elif 'percent' in text or '%' in text:
                p_list = list(filter(str.isdigit, text))
                p = ''
                try:
                    for dig in p_list:
                        p += str(dig)
                    p = int(p)
                except ValueError:
                    p  = -1
                    pass
                except AttributeError:
                    p  = -1
                    pass

                if p >= 0 and p <= 100:
                    print("setting motor to : ", p * 0.01)
                    say(str(p) + " percent")
                    pwm.value = p * 0.01
                    led.set_state(aiy.voicehat.LED.OFF)
                else:
                    print("I am sorry I can only accept a percent between 0 and 100")
                    say("I am sorry I can only accept a percent between 0 and 100")
                    led.set_state(aiy.voicehat.LED.BLINK)
            else:
                pwm.value = 0.0
                print("i'm sorry i heard, " + text +  " which is not a valid command")
                say("i'm sorry i heard, " + text + " which is not a valid command")
                print("You can say things like: min, max, off. mid, 45 percent and 91" +
                    " percent.")
                say("You can say things like: min, max, off. mid, 45 percent and 91" +
                    " percent.")
                led.set_state(aiy.voicehat.LED.BLINK)

if __name__ == "__main__":
    main()
