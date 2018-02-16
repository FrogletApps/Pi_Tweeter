#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sense_hat import SenseHat

pressure = SenseHat().get_pressure()

#This runs before the actual pressure tweet, otherwise sometimes you get a reading of 0
