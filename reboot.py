#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, datetime, time
from datetime import timedelta
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

i = datetime.datetime.now().strftime('%d/%m/%Y at %H:%M:%S')
twitter.update_status(status=' Rebooting...  Back in a second! \nUptime: '+uptime_string+' \nTweeted on %s' %i)
