import random
import os

scripts = [
	"/home/pi/SillyTweeter/RandomTweets.py",
	"/home/pi/SillyTweeter/RandomTweets.py",

	"sudo python /home/pi/SillyTweeter/picture.py",
	"sudo python /home/pi/SillyTweeter/picture.py",

	"/home/pi/SillyTweeter/SenseHATHumidity.py",

	"/home/pi/SillyTweeter/SenseHATPressure.py",

	"/home/pi/SillyTweeter/SenseHATTemperature.py",

	"/home/pi/SillyTweeter/Temperature.py",
]

os.system(random.choice(scripts))
