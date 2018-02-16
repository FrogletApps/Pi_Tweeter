#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import datetime

from twython import Twython
#CONSUMER_KEY = 
#CONSUMER_SECRET = 
#ACCESS_KEY = 
#ACCESS_SECRET = in your code put the twitter codes here (without the comments).  I keep them elsewhere for safe keeping though ;)
from secretCodes import *

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    uptime_string = str(datetime.timedelta(seconds = uptime_seconds))[:-7]

cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]
i = datetime.datetime.now().strftime('%d/%m/%Y at %H:%M:%S')
twitter.update_status(status='My current CPU temperature is '+temp+'°C \nUptime: '+uptime_string+' \nTweeted on %s' %i)
