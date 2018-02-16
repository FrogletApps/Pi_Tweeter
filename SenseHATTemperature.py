#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import datetime
from datetime import timedelta
from sense_hat import SenseHat

from twython import Twython
#CONSUMER_KEY = 
#CONSUMER_SECRET = 
#ACCESS_KEY = 
#ACCESS_SECRET = in your code put the twitter codes here (without the comments).  I keep them elsewhere for safe keeping though ;)
from secretCodes import *

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    uptime_string = str(timedelta(seconds = uptime_seconds))[:-7]

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
temp = round(temp,1)
temp = str(temp)

i = datetime.datetime.now().strftime('%d/%m/%Y at %H:%M:%S')
twitter.update_status(status='A totally accurate temperature reading is '+temp+'°C \nUptime: '+uptime_string+' \nTweeted on %s' %i)



