#!/usr/bin/env python
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
from secretcodes import *

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    uptime_string = str(timedelta(seconds = uptime_seconds))[:-7]

sense = SenseHat()
sense.clear()

humidity = sense.get_humidity()
humidity = round(humidity,2)
humidity = str(humidity)

i = datetime.datetime.now().strftime('%d/%m/%Y at %H:%M:%S')
twitter.update_status(status='The humidity of the air around me is '+humidity+'% \nUptime: '+uptime_string+' \nTweeted on %s' %i)



