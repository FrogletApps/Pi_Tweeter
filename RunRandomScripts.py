#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import os

scripts = [
	"/home/pi/TweetScripts/randomTweets.py",
	"/home/pi/TweetScripts/randomTweets.py",

	"sudo python /home/pi/TweetScripts/selfie.py",
	"sudo python /home/pi/TweetScripts/selfie.py",

	"/home/pi/TweetScripts/senseHATHumidity.py",

	"/home/pi/TweetScripts/senseHATPressure.py",

	"/home/pi/TweetScripts/senseHATTemperature.py",

	"/home/pi/TweetScripts/temperature.py",
]

os.system(random.choice(scripts))
