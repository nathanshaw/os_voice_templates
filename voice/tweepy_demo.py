#!/usr/bin/env python3

import aiy.audio
from aiy.audio import say
import aiy.cloudspeech
import aiy.voicehat
import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep
from tweepy import tweepy

class StreamListener(tweepy.StreamListener):

    def on_status(self, tweet):
        if "google" in tweet.text.lower():
            say("Google")
        elif "yahoo" in tweet.text.lower():
            say("Yahoo")

    def createStream():
        auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
        auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)
        api = tweepy.API(auth)
        stream_listener =  StreamListener()
        stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
        return stream

def main():
    stream = StreamListener.createStream()
    stream.filter("Google Yahoo", async=True)

    # build a recognizer and load it up with terms
    rec = aiy.cloudspeech.get_recognizer()
    rec.expect_phrase('min')
    rec.expect_phrase('max')
    rec.expect_phrase('mid')

    # start listening
    aiy.audio.get_recorder().start()

    # setup servo 0
    servo = Servo(26)
    # setup the button
    but = aiy.voicehat.get_button()

    # the led for the button
    led = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)

    # one time init message printed to console and said through speaker
    print("initializing system")
    say("initializing system")
    sleep(1) # wait for one second

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
