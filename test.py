import sys
import numpy as np
import pandas as pd
import cv2 
import time
from scipy.signal import butter, lfilter, hann
from numpy import fft
from scipy import signal
import matplotlib.pyplot as plt
#%matplotlib inline

def video_data(video):
    cap = cv2.VideoCapture(video)
    #getting the number of frames 
    #no_of_frames = int(cap.get(7))
    length = int(cap.get(3))
    width = int(cap.get(4))
    no_of_frames = int(cap.get(7))
    fps = cap.get(5) #frame rate
    
   
   
    y = np.zeros(no_of_frames)

    #time_list is used for storing occurence time of each frame in the video  
    time_list=[]
    t=0

    #camera frame per second is 30 and so each frame acccurs after 1/30th second
    start = time.time()
    difference = 1/30
    for i in range(no_of_frames):

        #reading the frame
        ret,frame = cap.read()
        #length,width,channels = frame.shape

        #calculating average red value in the frame
        y[i] = np.sum(frame[:,:,2])/(length*width)
        time_list.append(t)
        t = t + difference
    
    end = time.time()
    secs = end - start
    #fps = no_of_frames / secs
    cap.release()
    
    return y, fps

f, fps = video_data('Hart.mp4')
plt.title("Heart Rate Signal")
plt.plot(f, 'r')


