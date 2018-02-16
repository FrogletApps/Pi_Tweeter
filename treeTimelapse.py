#!/usr/bin/env python
# -*- coding: utf-8 -*-
from picamera import PiCamera
from twython import Twython
import sys
import os
import datetime

#CONSUMER_KEY = 
#CONSUMER_SECRET = 
#ACCESS_KEY = 
#ACCESS_SECRET = in your code put the twitter codes here (without the comments).  I keep them elsewhere for safe keeping though ;)
from secretcodes import *

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#WORK OUT TODAY'S DATE
i = datetime.datetime.now().strftime('Tweeted on %d/%m/%Y at %H:%M:%S')

#WORK OUT THE UPTIME OF THE RASPBERRY PI
with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    #-7 part gets rid of useless last 7 digits of fractions of seconds
    uptime_string = str(datetime.timedelta(seconds = uptime_seconds))[:-7]    

#Generate timestamp and storage location for photo
timestamp = datetime.datetime.now().isoformat()
photo_path = '/var/www/html/hosting/treetimelapse/Timelapse_Photo_Store/%s.jpg' %timestamp

#TAKE PHOTO OF TREE
with PiCamera() as camera:
	camera.resolution = (2592, 1944)
	camera.framerate = 15
	camera.capture(photo_path)
	photo = open(photo_path, 'rb')
	response = twitter.upload_media(media=photo)
	message = 'Tree Timelapse Picture\n%s' %i +'\nUptime: %s' %uptime_string
	twitter.update_status(status=message, media_ids=[response['media_id']])
