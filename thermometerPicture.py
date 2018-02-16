#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
from picamera import PiCamera
from twython import Twython
import sys
import os
import datetime
from sense_hat import SenseHat

#CONSUMER_KEY = 
#CONSUMER_SECRET = 
#ACCESS_KEY = 
#ACCESS_SECRET = in your code put the twitter codes here (without the comments).  I keep them elsewhere for safe keeping though ;)
from secretcodes import *

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#CPU/SENSE TEMPERATURE
with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    #-7 part gets rid of useless last 7 digits of fractions of seconds
    uptime_string = str(datetime.timedelta(seconds = uptime_seconds))[:-7]

sense = SenseHat()
sense.clear()

tempsense = sense.get_temperature()
tempsense = round(tempsense,1)
tempsense = str(tempsense)

cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]
i = datetime.datetime.now().strftime('%d/%m/%Y at %H:%M:%S')

#TAKE PHOTO OF THERMOMETER
with PiCamera() as camera:
	camera.capture('/home/pi/image.jpg')
	photo = open('/home/pi/image.jpg', 'rb')
	response = twitter.upload_media(media=photo)
	message = 'CPU temp is '+temp+'°C, Sense HAT temp is '+tempsense+'°C\nRoom temp in pic\nUptime: '+uptime_string+' \nAt %s' %i
	twitter.update_status(status=message, media_ids=[response['media_id']])
