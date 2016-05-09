#!/usr/bin/env python
# coding=utf-8
#from TIDES import *
import scipy.integrate as integrate
import scipy.interpolate as interpolate
import numpy as np
import time
#import matplotlib.pyplot as plt
import sys
##********************************************************************************#
#usage :
#python Gau2.py input.bin output.bin
input=sys.argv[1]   #smoothed data path
output=sys.argv[2]
def Gau(data,output=''):
    print 'Gau.................................'
    t0=time.time()

    bin=100
#   data=Tide.LoadDataOfhdf5(input)-1
#   shape=data.shape
#   data=data.reshape(-1)
    data=np.array(data,dtype=np.float64)
    sum1=data.mean()
    sort_data=data.argsort()
    #data=data[sort_data]
#   hist=np.histogram(data,bins=bin)
    print 'step 1'
    print 'time: %dm %ds'%((time.time()-t0)/60,(time.time()-t0)%60)
    t0=time.time()


    ###############################gauss...#########################################
    n=1024**3
    x=np.linspace(-3,3,1000)
    def gau(x):
        gau=np.exp(-0.5*x**2)
        return gau
    y=[integrate.quad(gau,0,i)[0] for i in x]
    f=interpolate.interp1d(y,x)
    a=np.linspace(y[0],y[-1],n)
    x=np.array(f(a),dtype=np.float64)
    del a
    print 'step 2'
    print 'time: %dm %ds'%((time.time()-t0)/60,(time.time()-t0)%60)
    t0=time.time()

    ################################################################################
    data[sort_data]=x[:]
    ################################################################################
    sum2=(data+1).mean()
    print 'mean1=',sum1
    print 'mean2=',sum2

    result=((data+1)*sum1/sum2)#.reshape(shape)
    print 'result',result.mean()
#   Tide.SaveDataHdf5(result,output)
    result=np.array(result,dtype=np.float32)
    result.tofile(output,format='f4')
    print 'step 3'
    print 'time: %dm %ds'%((time.time()-t0)/60,(time.time()-t0)%60)
    t0=time.time()

    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
    return result
data=np.fromfile(input,dtype='f4',count=1024**3)
Gau(data=data,output=output)
