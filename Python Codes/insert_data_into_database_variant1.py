# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 11:35:50 2017

@author: Rajat.Singh
"""

import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
from math import *
import json
import paho.mqtt.publish as publish
import datetime
import time
import paho.mqtt.client as mqtt
import random
import sys

original_arr = np.array([])
wave_initial= np.array([])
for i in np.arange(0,10000):
    val = 23
    r = random.randint(0,90)
    variation = r*0.0005
    wave_initial = np.append(wave_initial,val + variation)
    

sine_fn =np.array([])
outputlabel = np.zeros(shape=(10000,1))
index = 5
while index<9960:
    time_period = random.randint(10,50)
    j=np.arange(0,time_period+1)
    amp = random.randint(1,15)
    sine_fn = amp * np.sin(2.0*np.pi*j/float(2.0*time_period))
    
    for k in np.arange(0,sine_fn.size):
        wave_initial[index] = wave_initial[index] + sine_fn[k]
        index = index + 1
        outputlabel[index] = 1
    back_off_time = random.randint(25,50)
    index = index + back_off_time;
    for i in np.arange(index,10000):
        wave_initial[i] = wave_initial[i] + back_off_time/6
  
print 'Ok'
db = MySQLdb.connect(host = "localhost",user="root",passwd="",db="training")
cur = db.cursor()
time_current = datetime.datetime.now()

print 'Here'
for i in np.arange(0,wave_initial.size):
    
    execution_str = "INSERT into SENSOR_DATA(DATA_RECEIVED,SENSOR_ID) values(%s,'S01')"%wave_initial[i]
    cur.execute(execution_str)
    execution_str = "INSERT into SENSOR_DATA(DATA_RECEIVED,SENSOR_ID) values(%s,'S02')"%wave_initial[i]
    cur.execute(execution_str)
    execution_str = "INSERT into SENSOR_DATA(DATA_RECEIVED,SENSOR_ID) values(%s,'S03')"%wave_initial[i]
    cur.execute(execution_str)
    sys.stdout.flush
    db.commit()
    time.sleep(0.15)
    
