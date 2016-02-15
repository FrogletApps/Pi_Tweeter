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

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    uptime_string = str(timedelta(seconds = uptime_seconds))[:-7]

sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
pressure = round(pressure,2)
pressure = str(pressure)

i = datetime.datetime.now().strftime('%d/%m/%Y at %H:%M:%S')
api.update_status(status='The pressure of the air around me is '+pressure+' millibars \nUptime: '+uptime_string+' \nTweeted on %s' %i)



