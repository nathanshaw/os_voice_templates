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
from aiy.audio import say
import aiy.cloudspeech
import aiy.voicehat
from random import randint as random


def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase("french")
    recognizer.expect_phrase("spanish")
    recognizer.expect_phrase("german")
    recognizer.expect_phrase("english")
    recognizer.expect_phrase("italian")

    current_lang = "en-US"

    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

    led.set_state(aiy.voicehat.LED.ON)
    print("-------------------------------------------")
    print("please ask me to translate into English, Franch, German, Italian, or Spanish")

    r = random(1,3)
    if r == 1:
        aiy.audio.say("I speak many languages, test me out.")
    elif r == 2:
        aiy.audio.say("Welcome to the translation box, lets learn!.")
    elif r == 3:
        aiy.audio.say("Translation box initializing: English")

    while True:
        print('Press the button and speak')
        led.set_state(aiy.voicehat.LED.BLINK)
        button.wait_for_press()
        print('Listening...')
        led.set_state(aiy.voicehat.LED.ON)
        text = recognizer.recognize()

        if text is not None:
            led.set_state(aiy.voicehat.LED.OFF)
            text = text.lower()
            print(text)
            if "french" in text:
                print("translating to french")
                say("translating to french")
                current_lang = 'fr-FR'
            elif "german" in text:
                print("translating to German")
                say("translating to German")
                current_lang = 'de-DE'
            elif "english" in text:
                print("translating to English")
                say("translating to English")
                current_lang = 'en-US'
            elif "italian" in text:
                print("translating to Italian")
                say("translating to Italian")
                current_lang = 'it-IT'
            elif "spanish" in text:
                print("translating to Spanish")
                say("translating to Spanish")
                current_lang = 'es-ES'
            else:
                aiy.i18n.set_language_code(current_lang)
                print(text)
                say(text)
                aiy.i18n.set_language_code("en-US")
        else:
            print("I am sorry, I did not understand")
            say("I am sorry I did not understand")

if __name__ == '__main__':
    main()
