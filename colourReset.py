#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sense_hat import SenseHat
import time
import random

#CONSUMER_KEY = 
#CONSUMER_SECRET = 
#ACCESS_KEY = 
#ACCESS_SECRET = in your code put the twitter codes here (without the comments).  I keep them elsewhere for safe keeping though ;)
from secretCodes import *

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

sense = SenseHat()

N = [0,0,0]

reset = [
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N
]

sense.set_pixels(reset)
