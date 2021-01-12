# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 14:42:40 2017

@author: Rajat.Singh
"""
#from sklearn import svm
import json
import numpy as np
import MySQLdb
from hmmlearn import hmm
import time
import datetime
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

def probcal1(z_hmm,len1,len2):
    c_arr = np.zeros(shape=(27,1))
    z_input =np.array([])

    for i in np.arange(0,len1-1):
        if((z_hmm[i][0] == 1) and (z_hmm[i][1] == 5) and (z_hmm[i][2] == 0)):
            c_arr[0] = c_arr[0] + 1
            z_input = np.append(z_input,0)
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 5) and (z_hmm[i][2] == 25)):
            c_arr[1] = c_arr[1] + 1
            z_input = np.append(z_input,1)
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 5) and (z_hmm[i][2] == 50)):
            c_arr[2] = c_arr[2] + 1
            z_input = np.append(z_input,2)
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 0)):
            c_arr[3] = c_arr[3] + 1
            z_input = np.append(z_input,3)
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 25)):
            c_arr[4] = c_arr[4] + 1
            z_input = np.append(z_input,4)
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 50)):
            c_arr[5] = c_arr[5] + 1
            z_input = np.append(z_input,5)
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 0)):
            c_arr[6] = c_arr[6] + 1
            z_input = np.append(z_input,6)
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 25)):
            c_arr[7] = c_arr[7] + 1
            z_input = np.append(z_input,7)
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 50)):
            c_arr[8] = c_arr[8] + 1
            z_input = np.append(z_input,8)
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 5) and (z_hmm[i][2] == 0)):
            c_arr[9] = c_arr[9] + 1
            z_input = np.append(z_input,9)
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 5) and (z_hmm[i][2] == 25)):
            c_arr[10] = c_arr[10] + 1
            z_input = np.append(z_input,10)
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 5) and (z_hmm[i][2] == 50)):
            c_arr[11] = c_arr[11] + 1
            z_input = np.append(z_input,11)
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 0)):
            c_arr[12] = c_arr[12] + 1
            z_input = np.append(z_input,12)
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 25)):
            c_arr[13] = c_arr[13] + 1
            z_input = np.append(z_input,13)
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 50)):
            c_arr[14] = c_arr[14] + 1
            z_input = np.append(z_input,14)
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 0)):
            c_arr[15] = c_arr[15] + 1
            z_input = np.append(z_input,15)
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 25)):
            c_arr[16] = c_arr[16] + 1
            z_input = np.append(z_input,16)
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 50)):
            c_arr[17] = c_arr[17] + 1
            z_input = np.append(z_input,17)
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 5) and (z_hmm[i][2] == 0)):
            c_arr[18] = c_arr[18] + 1
            z_input = np.append(z_input,18)
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 5)  and (z_hmm[i][2] == 25)):
            c_arr[19] = c_arr[19] + 1
            z_input = np.append(z_input,19)
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 5)  and (z_hmm[i][2] == 50)):
            c_arr[20] = c_arr[20] + 1
            z_input = np.append(z_input,20)
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 0)):
            c_arr[21] = c_arr[21] + 1
            z_input = np.append(z_input,21)
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 25)):
            c_arr[22] = c_arr[22] + 1
            z_input = np.append(z_input,22)
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 50)):
            c_arr[23] = c_arr[23] + 1
            z_input = np.append(z_input,23)
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 0)):
            c_arr[24] = c_arr[24] + 1
            z_input = np.append(z_input,24)
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 25)):
            c_arr[25] = c_arr[25] + 1
            z_input = np.append(z_input,25)
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 50)):
            c_arr[26] = c_arr[26] + 1
            z_input = np.append(z_input,26)
    return c_arr,z_input


def probcal(z_hmm,len1,len2):
    z_input = np.array([])
    c_arr = np.zeros(shape=(27,1))
    check_noise = np.loadtxt('noise_check.txt')
    d_arr =np.zeros(shape = (27,1))
    for i in np.arange(len1,len1+len2-2):
        if((z_hmm[i][0] == 1) and (z_hmm[i][1] == 5) and (z_hmm[i][2] == 0)):
            if check_noise[i-len1]== 1:
                d_arr[0] = d_arr[0] + 1
                z_input = np.append(z_input,0)
            else:
                c_arr[0] = c_arr[0] + 1
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 5) and (z_hmm[i][2] == 25)):
            if check_noise[i-len1] == 1:
                d_arr[1] = d_arr[1] + 1
                z_input = np.append(z_input,1)
            else:
                c_arr[1] = c_arr[1] + 1
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 5) and (z_hmm[i][2] == 50)):
            if check_noise[i-len1] == 1:
                d_arr[2] = d_arr[2] + 1
                z_input = np.append(z_input,2)
            else:
                c_arr[2] = c_arr[2] + 1
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 0)):
            if check_noise[i-len1] == 1:
                d_arr[3] = d_arr[3] + 1
                z_input = np.append(z_input,3)
            else:
                c_arr[3] = c_arr[3] + 1
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 25)):
            if check_noise[i-len1] == 1:
                d_arr[4] = d_arr[4] + 1
                z_input = np.append(z_input,4)
            else:
                c_arr[4] = c_arr[4] + 1
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 50)):
            if check_noise[i-len1] == 1:
                d_arr[5] = d_arr[5] + 1
                z_input = np.append(z_input,5)
            else:
                c_arr[5] = c_arr[5] + 1
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 0)):
            if check_noise[i-len1] == 1:
                d_arr[6] = d_arr[6] + 1
                z_input = np.append(z_input,6)
            else:
                c_arr[6] = c_arr[6] + 1
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 25)):
            if check_noise[i-len1] == 1:
                d_arr[7] = d_arr[7] + 1
                z_input = np.append(z_input,7)
            else:
                c_arr[7] = c_arr[7] + 1
        elif((z_hmm[i][0] == 1) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 50)):
            if check_noise[i-len1] == 1:
                d_arr[8] = d_arr[8] + 1
                z_input = np.append(z_input,8)
            else:
                c_arr[8] = c_arr[8] + 1
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 5) and (z_hmm[i][2] == 0)):
            if check_noise[i-len1] == 1:
                d_arr[9] = d_arr[9] + 1
                z_input = np.append(z_input,9)
            else:
                c_arr[9] = c_arr[9] + 1
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 5) and (z_hmm[i][2] == 25)):
            if check_noise[i-len1] == 1:
                d_arr[10] = d_arr[10] + 1
                z_input = np.append(z_input,10)
            else:
                c_arr[10] = c_arr[10] + 1
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 5) and (z_hmm[i][2] == 50)):
            if check_noise[i-len1] == 1:
                d_arr[11] = d_arr[11] + 1
                z_input = np.append(z_input,11)
            else:
                c_arr[11] = c_arr[11] + 1
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 0)):
            if check_noise[i-len1] == 1:
                d_arr[12] = d_arr[12] + 1
                z_input = np.append(z_input,12)
            else:
                c_arr[12] = c_arr[12] + 1
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 25)):
            if check_noise[i-len1] == 1:
                d_arr[13] = d_arr[13] + 1
                z_input = np.append(z_input,13)
            else:
                c_arr[9] = c_arr[9] + 1
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 50)):
            if check_noise[i-len1] == 1:
                d_arr[14] = d_arr[14] + 1
                z_input = np.append(z_input,14)
            else:
                c_arr[14] = c_arr[14] + 1
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 0)):
            if check_noise[i-len1] == 1:
                d_arr[15] = d_arr[15] + 1
                z_input = np.append(z_input,15)
            else:
                c_arr[15] = c_arr[15] + 1
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 25)):
            if check_noise[i-len1] == 1:
                d_arr[16] = d_arr[16] + 1
                z_input = np.append(z_input,16)
            else:
                c_arr[16] = c_arr[16] + 1
        elif((z_hmm[i][0] == 0) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 50)):
            if check_noise[i-len1] == 1:
                d_arr[17] = d_arr[17] + 1
                z_input = np.append(z_input,17)
            else:
                c_arr[17] = c_arr[17] + 1
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 5) and (z_hmm[i][2] == 0)):
            if check_noise[i-len1] == 1:
                d_arr[18] = d_arr[18] + 1
                z_input = np.append(z_input,18)
            else:
                c_arr[18] = c_arr[18] + 1
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 5)  and (z_hmm[i][2] == 25)):
            if check_noise[i-len1] == 1:
                d_arr[19] = d_arr[19] + 1
                z_input = np.append(z_input,19)
            else:
                c_arr[19] = c_arr[19] + 1
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 5)  and (z_hmm[i][2] == 50)):
            if check_noise[i-len1] == 1:
                d_arr[20] = d_arr[20] + 1
                z_input = np.append(z_input,20)
            else:
                c_arr[20] = c_arr[20] + 1
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 0)):
            if check_noise[i-len1] == 1:
                d_arr[21] = d_arr[21] + 1
                z_input = np.append(z_input,21)
            else:
                c_arr[21] = c_arr[21] + 1
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 25)):
            if check_noise[i-len1] == 1:
                d_arr[22] = d_arr[22] + 1
                z_input = np.append(z_input,22)
            else:
                c_arr[22] = c_arr[22] + 1
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 10) and (z_hmm[i][2] == 50)):
            if check_noise[i-len1] == 1:
                d_arr[23] = d_arr[23] + 1
                z_input = np.append(z_input,23)
            else:
                c_arr[23] = c_arr[23] + 1
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 0)):
            if check_noise[i-len1] == 1:
                d_arr[24] = d_arr[24] + 1
                z_input = np.append(z_input,24)
            else:
                c_arr[24] = c_arr[24] + 1
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 25)):
            if check_noise[i-len1] == 1:
                d_arr[25] = d_arr[25] + 1
                z_input = np.append(z_input,25)
            else:
                c_arr[25] = c_arr[25] + 1
        elif((z_hmm[i][0] == -1) and (z_hmm[i][1] == 20) and (z_hmm[i][2] == 50)):
            if check_noise[i-len1] == 1:
                d_arr[26] = d_arr[26] + 1
                z_input = np.append(z_input,26)
            else:
                c_arr[26] = c_arr[26] + 1
    return c_arr,d_arr,z_input

def supervised_learning():
    print 'Start Algorithm'
    input_data = np.loadtxt('no_noise.txt')
    input_data = input_data.astype(int)
    np.savetxt('no_noise.txt',input_data,fmt='%d')
    output_label = np.array([])
    k1,k2 =  input_data.shape
    print k1,k2
    for i in np.arange(0,k1):
        output_label = np.append(output_label,0)
    tempp = np.loadtxt('noise.txt')
    tempp = tempp.astype(int)
    k1,k2 = tempp.shape
    for i in np.arange(0,k1):
        output_label = np.append(output_label,1)
    len_pass1,g = input_data.shape
    len_pass2,g = tempp.shape
    input_data = np.vstack((input_data,tempp))
    print input_data.shape
    #print input_data[1][2]
    len1,len2 = input_data.shape;
    slope_x = np.array([])
    slope_y = np.array([])
    slope_z = np.array([])
    slope_xyz = np.array([0,0,0])
    looper = np.arange(0,len1-1)
    for i in looper:
        slope_x = np.append(slope_x,input_data[i+1][0]-input_data[i][0])
        slope_y = np.append(slope_y,input_data[i+1][1]-input_data[i][1])
        slope_z = np.append(slope_z,input_data[i+1][2]-input_data[i][2])
    #print slope_x.shape,slope_y.shape,slope_z.shape
    #print slope_x,slope_y,slope_z
    slope_temp = np.vstack((slope_x,slope_y))
    slope_temp = np.vstack((slope_temp,slope_z))
    slope_temp = np.transpose(slope_temp)
    #print slope_temp.shape,slope_xyz.shape
    #print slope_temp
    slope_xyz = np.vstack((slope_xyz,slope_temp))
    slope_xyz = slope_xyz[1:,]
    #print slope_xyz
    #print output_label[1:].shape
    #print slope_xyz.shape
    #print output_label
    
    return input_data,slope_xyz,output_label,len_pass1,len_pass2

#--------------------------------------------------------------------------------------------------------------
def makeFile_func():
    db = MySQLdb.connect(host = "localhost",user="root",passwd="",db="training")

    cur = db.cursor()
    time_current = datetime.datetime.now()
    time_current = time_current - datetime.timedelta(seconds=5)
    #print time_current.strftime("%Y-%m-%d %H:%M:%S")
    execution_str = "SELECT sensor_id,receive_time,data_received FROM SENSOR_DATA order by receive_time desc limit 80"    
    cur.execute(execution_str)
    data_s1 = np.array([])
    data_s2 = np.array([])
    data_s3 = np.array([])
    timex = np.array([])
    timey = np.array([])
    timez = np.array([])
    for row in cur.fetchall():
        if (row[0] == 'S01'):
            data_s1 = np.append(data_s1,row[2])
            timex = np.append(timex,str(row[1]))
        elif (row[0] == 'S02'):
            data_s2 = np.append(data_s2,row[2])
            timey = np.append(timey,str(row[1]))
        elif (row[0] == 'S03'):
            data_s3 = np.append(data_s3,row[2])
            timez = np.append(timez,str(row[1]))
    #print timex
    timex =np.flip(timex,0)
    timey =np.flip(timey,0)
    timez =np.flip(timez,0)
    np.savetxt('timex.txt',timex,fmt="%s")
    np.savetxt('timey.txt',timey,fmt="%s")
    np.savetxt('timez.txt',timez,fmt="%s")
    np.savetxt('datax.txt',data_s1)
    
    common_number = np.min([data_s1.size,data_s2.size,data_s3.size])

    data_s1 = data_s1[0:common_number,]
    data_s2 = data_s2[0:common_number,]
    data_s3 = data_s3[0:common_number,]
    data_s1 =np.flip(data_s1,0)
    data_s2 =np.flip(data_s2,0)
    data_s3 =np.flip(data_s3,0)
    
    # Calculate slopes
        
    slope_x = np.array([])
    slope_y = np.array([])
    slope_z = np.array([])
    slope_x = data_s1
    slope_y = data_s2
    slope_z = data_s3    
    
    # Calculate count
    count_array_x = np.array([])
    count_array_y = np.array([])
    count_array_z = np.array([])    
    
    slope_xyz = np.vstack([slope_x,slope_y,slope_z])
    slope_xyz = np.transpose(slope_xyz)   
    
    # X count 
    count_array_x,flag_array = count_flag(slope_xyz,0,0,slope_x.size)
    final_flag_array_x =  flag_array
    
    # Y count 
    count_array_y,flag_array = count_flag(slope_xyz,1,0,slope_x.size)
    final_flag_array_y =  flag_array
    
    # Z count 
    count_array_z,flag_array = count_flag(slope_xyz,2,0,slope_x.size)
    final_flag_array_z =  flag_array
    
    #Normalize count array
    for i in np.arange(0,count_array_x.size):
        if count_array_x[i] >2:
            count_array_x[i] = 20
        elif count_array_x[i] >=1:
            count_array_x[i] = 10
        elif count_array_x[i]>=0:
            count_array_x[i] = 5

        if count_array_y[i] >2:
            count_array_y[i] = 20
        elif count_array_y[i] >=1:
            count_array_y[i] = 10
        elif count_array_y[i]>=0:
            count_array_y[i] = 5
            
        if count_array_z[i] >2:
            count_array_z[i] = 20
        elif count_array_z[i] >=1:
            count_array_z[i] = 10
        elif count_array_z[i]>=0:
            count_array_z[i] = 5
    
    
#-------------------------------------------------------------------------------------------------------------
# FEATURE 3
#-------------------------------------------------------------------------------------------------------------    
    
    feature3_x =np.array([])
    feature3_y =np.array([])
    feature3_z =np.array([])
    print count_array_x.size
    for i in np.arange(0,count_array_x.size):
        feature3_x = np.append(feature3_x,flag_changes(final_flag_array_x,i))
    for i in np.arange(0,count_array_x.size):
        feature3_y = np.append(feature3_y,flag_changes(final_flag_array_y,i))
    for i in np.arange(0,count_array_x.size):
        feature3_z = np.append(feature3_z,flag_changes(final_flag_array_z,i))

    print feature3_x.size,feature3_y.size,feature3_z.size
#-------------------------------------------------------------------------------------------------------------
   
    x_hmm = final_flag_array_x
    y_hmm = final_flag_array_y
    z_hmm = final_flag_array_z
    
    x_hmm = np.vstack((x_hmm,count_array_x,feature3_x))
    y_hmm = np.vstack((y_hmm,count_array_y,feature3_y))
    z_hmm = np.vstack((z_hmm,count_array_z,feature3_z))
    x_hmm = np.transpose(x_hmm)
    y_hmm = np.transpose(y_hmm)
    z_hmm = np.transpose(z_hmm)    
    
    np.savetxt('z_hmmp.txt',z_hmm)   
    arr = np.hstack([x_hmm,y_hmm,z_hmm])

    k1,k2 = arr.shape
    
    
# -------------------------------------------------------------------------------------------------------------
# Extractx  labels from input as the observed states
#------------------------------------------------------------------------------------------------------------
    
    carr,x_input = probcal1(x_hmm,k1+1,k1)
    print x_input.shape
# -------------------------------------------------------------------------------------------------------------
# Extractx  labels from input as the observed states
#------------------------------------------------------------------------------------------------------------
  
    carr,y_input = probcal1(y_hmm,k1+1,k1)

# -------------------------------------------------------------------------------------------------------------
# Extractx  labels from input as the observed states
#------------------------------------------------------------------------------------------------------------
    
    carr,z_input = probcal1(z_hmm,k1+1,k1)

   
    to_save = np.vstack([x_input,y_input,z_input])
    to_save = np.transpose(to_save)
    np.savetxt('prediction_data.txt',to_save)
    db.close   



#--------------------------------------------------------------------------------------------------------------

def prv_flag(flag_array):
    p_value = 0
    for i in np.arange(flag_array.size):
        if(flag_array[flag_array.size-1-i] == 1):
            p_value = 1
            break
        elif(flag_array[flag_array.size-1-i] == -1):
            p_value = -1
            break
    return p_value


#--------------------------------------------------------------------------------------------------------------
def flag_changes(flag_array,pos):
    retval = 0
    init_val = 1
    if pos > 3:
        init_val = pos-3
    for j in np.arange(init_val,pos+1):
        if flag_array[j]<> flag_array[j-1]:
            retval = retval + 1
    if retval>2:
        return 50
    elif retval>0:
        return 25
    return 0
        
def changes(count_array,top):
    start =0
    retval = 0    
    if(top>4):
        start = top - 4
    i = top -1
    while i >= start:
        if count_array[top] == count_array[i]:
            retval = retval + 1
            i = i-1
        else:
            break;
    return retval
  

def count_flag(observed,index,start,len1):
    flag_inc_dec = 0 #positive
    flag_array = np.array([])
    count_array_x =np.array([])
    # X AXIS   
    count_top = -1
    for i in np.arange(start,len1-1):
        count_changes = changes(flag_array,count_top)
        flag_array = np.append(flag_array,flag_inc_dec)
        if((observed[i+1][index] - observed[i][index] > 0) and ((flag_inc_dec == 1) or ((flag_inc_dec == 0 ) and (prv_flag(flag_array) <> -1)))):
            count_changes = count_changes + 1
            flag_inc_dec = 1
        elif((observed[i+1][index] - observed[i][index] < 0) and ((flag_inc_dec ==-1) or ((flag_inc_dec == 0 )and (prv_flag(flag_array) <> 1)))):
            count_changes = count_changes + 1
            flag_inc_dec = -1
        elif observed[i+1][index] - observed[i][index] > 0:
            flag_inc_dec = 1
            count_changes = 0
        elif observed[i+1][index] - observed[i][index] < 0:
            flag_inc_dec = -1
            count_changes = 0
        else:
            flag_inc_dec = 0
        count_array_x = np.append(count_array_x,count_changes)
        count_top = count_top + 1
    return count_array_x,flag_array
      
#--------------------------------------------------------------------------------------------------------------
def tryHmm(observed,input_data,hidden,len1,len2):
    l1,l2 = observed.shape  # The slopes 0--->len1-1 an len1--->len2+len1   
    arr = np.arange(0,l1-1)
    count_changes = 0
    count_array_x = np.array([])
    count_array_y = np.array([])
    count_array_z = np.array([])
    final_flag_array_x = np.array([])
    final_flag_array_y = np.array([])
    final_flag_array_z = np.array([])
    
    # X AXIs
    
    count_array_x,flag_array = count_flag(observed,0,0,len1)
    x,y = count_flag(observed,0,len1,len1+len2)
    count_array_x = np.append(count_array_x,x)
    flag_array = np.append(flag_array,y)
    final_flag_array_x =  np.append(final_flag_array_x,flag_array)
    
    # Y AXIS
    
    count_array_y,flag_array = count_flag(observed,1,0,len1)
    x,y = count_flag(observed,1,len1,len1+len2)
    count_array_y = np.append(count_array_y,x)
    flag_array = np.append(flag_array,y)
    final_flag_array_y =  np.append(final_flag_array_y,flag_array)
        
    # Z AXIS
        
    count_array_z,flag_array = count_flag(observed,2,0,len1)
    x,y = count_flag(observed,2,len1,len1+len2)
    count_array_z = np.append(count_array_z,x)
    flag_array = np.append(flag_array,y)
    final_flag_array_z =  np.append(final_flag_array_z,flag_array)
    
    #np.savetxt('count.txt',count_array_x)
    for i in np.arange(0,count_array_x.size):
        if count_array_x[i] >2:
            count_array_x[i] = 20
        elif count_array_x[i] >=1:
            count_array_x[i] = 10
        elif count_array_x[i]>=0:
            count_array_x[i] = 5

        if count_array_y[i] >2:
            count_array_y[i] = 20
        elif count_array_y[i] >=1:
            count_array_y[i] = 10
        elif count_array_y[i]>=0:
            count_array_y[i] = 5
            
        if count_array_z[i] >2:
            count_array_z[i] = 20
        elif count_array_z[i] >=1:
            count_array_z[i] = 10
        elif count_array_z[i]>=0:
            count_array_z[i] = 5 
    
#-------------------------------------------------------------------------------------------------------------
# FEATURE 3
#-------------------------------------------------------------------------------------------------------------    
    feature3_x =np.array([])
    feature3_y =np.array([])
    feature3_z =np.array([])
    
    for i in np.arange(0,len1-1):
        feature3_x = np.append(feature3_x,flag_changes(final_flag_array_x,i))
    for i in np.arange(0,len1-1):
        feature3_y = np.append(feature3_y,flag_changes(final_flag_array_y,i))
    for i in np.arange(0,len1-1):
        feature3_z = np.append(feature3_z,flag_changes(final_flag_array_z,i))
    #print final_flag_array_x.shape   
    
    for i in np.arange(0,len2-2):
        feature3_x = np.append(feature3_x,flag_changes(final_flag_array_x[len1:,],i))
    for i in np.arange(0,len2-2):
        feature3_y = np.append(feature3_y,flag_changes(final_flag_array_y[len1:,],i))
    for i in np.arange(0,len2-2):
        feature3_z = np.append(feature3_z,flag_changes(final_flag_array_z[len1:,],i))

#-------------------------------------------------------------------------------------------------------------

    tmp = np.vstack((count_array_x,count_array_y))
    tmp = np.vstack((tmp,count_array_z))
    tmp = np.transpose(tmp)
    tmp = tmp[:-1]

    observed = observed[:-1]
    #x_hmm = observed[:,0]
    #y_hmm = observed[:,1]
    #z_hmm = observed[:,2]
    
    x_hmm = final_flag_array_x[:-1]
    y_hmm = final_flag_array_y[:-1]
    z_hmm = final_flag_array_z[:-1]

    x_hmm = np.vstack((x_hmm,(tmp[:,0]),feature3_x))
    y_hmm = np.vstack((y_hmm,(tmp[:,1]),feature3_y))
    z_hmm = np.vstack((z_hmm,(tmp[:,2]),feature3_z))
    x_hmm = np.transpose(x_hmm)
    y_hmm = np.transpose(y_hmm)
    z_hmm = np.transpose(z_hmm)
       
    np.savetxt('z_hmm.txt',z_hmm)        
    
    len2 = len2 -1
    # Calculate Training Parameters for X
    
    states = ["No_Noise","Noise"]
    n_states = len(states)  
    observations = ["1,5","1,10","1,20","0,5","0,10","0,20","-1,5","-1,10","-1,20"]
    n_observations = len(observations)  
    start_probability = [0.9,0.1]
    transition_probability = np.array([[0.8,0.2],[0.2,0.8]])
    
    c_arr,x_input = probcal1(x_hmm,len1,len2)
    c_arr1,d_arr,x_input = probcal(x_hmm,len1,len2)
    c_arr = c_arr+c_arr1
    c_arr = c_arr/(len1+len2 - np.sum(d_arr))
    d_arr = d_arr/np.sum(d_arr)
    # Check Here if not working
    
    emission_probability = np.hstack((c_arr,d_arr))
    emission_probability = np.transpose(emission_probability)
    
#------------------------------------------------------------------------------------------------------------    
# Calculate Training Parameters for Y
#------------------------------------------------------------------------------------------------------------
    
    transition_probability = np.array([[0.8,0.2],[0.2,0.8]])
    c_arr,y_input = probcal1(y_hmm,len1,len2)
    c_arr1,d_arr,y_input = probcal(y_hmm,len1,len2)
    c_arr = c_arr+c_arr1
    c_arr = c_arr/(len1+len2 - np.sum(d_arr))
    d_arr = d_arr/np.sum(d_arr)
    
    emission_probability_y = np.hstack((c_arr,d_arr))
    emission_probability_y = np.transpose(emission_probability_y)
    
#-------------------------------------------------------------------------------------------------------------    
# Calculate Training Parameters for Z
#-------------------------------------------------------------------------------------------------------------
    
    transition_probability = np.array([[0.8,0.2],[0.2,0.8]])
    c_arr,z_input = probcal1(z_hmm,len1,len2)

    c_arr1,d_arr,z_input1 = probcal(z_hmm,len1,len2)
    c_arr = c_arr+c_arr1
    print z_input1
    c_arr = c_arr/(len1+len2 - np.sum(d_arr))
    d_arr = d_arr/np.sum(d_arr)

    emission_probability_z = np.hstack((c_arr,d_arr))
    emission_probability_z = np.transpose(emission_probability_z)
#---------------------------------------------------------------------------------------------------------------    
# HMM MODELS ACCROSS VARIOUS AXIS
  #--------------------------------------------------------------------------------------------------------------
    
    #X Axis model    
    hmm_X = hmm.MultinomialHMM(n_components=2)
    hmm_X.startprob_ = start_probability
    hmm_X.transmat_ = transition_probability
    hmm_X.emissionprob_ = emission_probability


    x_input = x_input.astype(int)
    x_input = np.array([x_input]).T
    
    logprob,output = hmm_X.decode(x_input,algorithm = "viterbi")
    #print "Output is",",".join(map(lambda x: states[x],output)) 

    #Y axis model

    hmm_Y = hmm.MultinomialHMM(n_components=2)
    hmm_Y.startprob_ = start_probability
    hmm_Y.transmat_ = transition_probability
    hmm_Y.emissionprob_ = emission_probability_y    
    
    y_input = y_input.astype(int)
    y_input = np.array([y_input]).T
    
    logprob,output = hmm_Y.decode(y_input,algorithm = "viterbi")
    #print "Output is",",".join(map(lambda x: states[x],output)) 

    # Z axis model
    
    hmm_Z = hmm.MultinomialHMM(n_components=2)
    hmm_Z.startprob_ = start_probability
    hmm_Z.transmat_ = transition_probability
    hmm_Z.emissionprob_ = emission_probability_z    
    
    z_input = z_input.astype(int)
    z_input = np.array([z_input]).T
    
    logprob,output = hmm_Z.decode(z_input,algorithm = "viterbi")
    #print "Output is",",".join(map(lambda x: states[x],output)) 
    #print output.size
    plt.ion()
    while 1<2:
        makeFile_func()
        time.sleep(5)
        #time.sleep(5)
        prediction_file = np.loadtxt('prediction_data.txt')
        prediction_file = prediction_file.astype(int)
        timex = np.loadtxt('timex.txt',dtype='str')
        timey = np.loadtxt('timey.txt',dtype='str')
        timez = np.loadtxt('timey.txt',dtype='str')
        
        np.savetxt('timex_output.txt',np.array([]))
        np.savetxt('timey_output.txt',np.array([]))
        np.savetxt('timez_output.txt',np.array([]))
        
        x_input_predict = prediction_file[:,0]
        x_input_predict = x_input_predict.ravel()
        x_input_predict = np.array([x_input_predict]).T
        
        y_input_predict = prediction_file[:,1]
        y_input_predict = y_input_predict.ravel()
        y_input_predict = np.array([y_input_predict]).T
        
        z_input_predict = prediction_file[:,2]
        z_input_predict = z_input_predict.ravel()
        z_input_predict = np.array([z_input_predict]).T
        
        #print x_input_predict.shape,x_input_predict.shape
        loga,x_predict = hmm_X.decode((x_input_predict).astype(int),algorithm = "viterbi")
        loga,y_predict = hmm_Y.decode((y_input_predict).astype(int),algorithm = "viterbi")
        loga,z_predict = hmm_Z.decode((z_input_predict).astype(int),algorithm = "viterbi")

        for i in np.arange(0,x_predict.size):
            if(x_predict[i] == 1):
                tval = np.loadtxt('timex_output.txt',dtype='str')
                tval = np.append(tval,str(timex[i-2][1]))
                np.savetxt('timex_output.txt',tval,fmt="%s")
            if(y_predict[i] == 1):
                tval = np.loadtxt('timey_output.txt',dtype='str')
                tval = np.append(tval,str(timey[i-2][1]))
                np.savetxt('timey_output.txt',tval,fmt="%s")
            if(z_predict[i] == 1 ):
                tval = np.loadtxt('timez_output.txt',dtype='str')
                tval = np.append(tval,str(timez[i-2][1]))
                np.savetxt('timez_output.txt',tval,fmt="%s")
        #plt.plot(np.arange(0,x_input_predict.size),x_predict)
        #plt.show()
# Model clf is SVM model
# Train model
# Predict in main itself
#np.savetxt('sample1.txt',np.array([[1,2,3],[10,13,20],[40,50,60],[70,80,90],[55,55,55],[102,14,57],[5,2,3]]))
#np.savetxt('sample1_out.txt',np.array([1,2,2,3,2,3,1]))
input_data,slope_xyz,output_label,len_pass1,len_pass2 = supervised_learning()
#np.savetxt('slope_txt.txt',slope_xyz[len_pass1:len_pass1+len_pass2-1])
#SVM MODEL
#print input_data.shape,slope_xyz.shape,output_label.shape
#prediction_data = np.loadtxt('predict.txt')

#clf = svm.SVC()
#clf.fit(slope_xyz,output_label[:-1])
#l1,l2 = prediction_data.shape 

#for i in np.arange(0,l1):
sum_k = 0.0
#print len1
slope_x = np.array([])
slope_y = np.array([])
slope_z = np.array([])
slope_xyz1 = np.array([0,0,0])
#looper = np.arange(0,len1-1)
#for i in looper:
#    slope_x = np.append(slope_x,prediction[i+1][0]-prediction[i][0])
#    slope_y = np.append(slope_y,prediction[i+1][1]-prediction[i][1])
#    slope_z = np.append(slope_z,prediction[i+1][2]-prediction[i][2])
#slope_temp = np.array([])
#slope_temp = np.vstack((slope_x,slope_y))
#slope_temp = np.vstack((slope_temp,slope_z))
#slope_temp = np.transpose(slope_temp)
#print slope_temp.shape
    #print slope_temp.shape,slope_xyz.shape
    #print slope_temp
#slope_xyz1 = np.vstack((slope_xyz1,slope_temp))
#slope_xyz1 = slope_xyz1[1:,]
#print slope_xyz1.shape

#par = clf.predict(slope_xyz1)
#for i in np.arange(0,par.size):
#    sum_k = sum_k + par[i]
#sum_k = sum_k/par.size
#print sum_k

#HMM Model
print slope_xyz.shape,len_pass1,len_pass2
tryHmm(input_data,slope_xyz,output_label,len_pass1,len_pass2)
                     