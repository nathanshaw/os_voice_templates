#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
from random import randint as random


def main():
    recognizer = aiy.cloudspeech.get_recognizer()

    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

    r = random(1,3)
    if r == 1:
        aiy.audio.say("Hello, lets talk, i am a good listener. Press my button and lets chat.")
    elif r == 2:
        aiy.audio.say("I am a good listener. Press my button and i will listen.")
    elif r == 3:
        aiy.audio.say("you can tell me anything, just press my button")

    while True:
        print('Press the button and speak')
        led.set_state(aiy.voicehat.LED.BLINK)
        button.wait_for_press()
        print('Listening...')
        led.set_state(aiy.voicehat.LED.ON)
        text = recognizer.recognize()

        if text is not None:
            led.set_state(aiy.voicehat.LED.OFF)
            t = "tell me more about, " + text
            print(t)
            aiy.audio.say(t)
        else:
            r = random(1, 10)
            if r < 3:
                aiy.audio.say("Oh wow. I'm listening")
            elif r < 6:
                aiy.audio.say("No way! Go on...")
            else:
                aiy.audio.say("Wow, you do not say, go on")

if __name__ == '__main__':
    main()
