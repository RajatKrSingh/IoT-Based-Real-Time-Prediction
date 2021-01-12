# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 13:23:23 2017

@author: Rajat.Singh
"""

import matplotlib.pyplot as plt
import numpy as np
from math import *
import json
import paho.mqtt.publish as publish
import datetime
import time
import paho.mqtt.client as mqtt
import random

original_arr = np.array([])
wave_initial= np.array([])
for i in np.arange(0,10000):
    val = 23
    r = random.randint(0,90)
    variation = r*0.0005
    wave_initial = np.append(wave_initial,val + variation)
    

sine_fn =np.array([])
outputlabel = np.zeros(shape=(9999,))
print outputlabel.shape
index = 5
count = 0

plt.plot(wave_initial[0:100])
slope_to_save = np.array([])
for i in np.arange(0,wave_initial.size-1):
    slope_to_save = np.append(slope_to_save,wave_initial[i+1]-wave_initial[i])

plt.show()

to_save = np.vstack((wave_initial,wave_initial,wave_initial,wave_initial))
to_save = np.transpose(to_save)
np.savetxt('fresh_no_noise.txt',to_save)