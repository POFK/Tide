#!/usr/bin/env python
# coding=utf-8
from TIDES import *
import scipy.integrate as integrate
import scipy.interpolate as interpolate
import time
import matplotlib.pyplot as plt
#import sys
##********************************************************************************#
#name='halorhobin1024m3z0.000.dat'
#def Gau(input='',output=''):
#    input=sys.argv[1]
#    output=sys.argv[2]
def Gau(data,output):
    print 'Gau.................................'
    t0=time.time()

    bin=100
#   data=Tide.LoadDataOfhdf5(input)-1
    shape=data.shape
    data=data.reshape(-1)
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
    x=f(a)
    del a
    print 'step 2'
    print 'time: %dm %ds'%((time.time()-t0)/60,(time.time()-t0)%60)
    t0=time.time()

    ################################################################################
    data[sort_data]=x
    ################################################################################
    sum2=(data+1).mean()
    print 'sum1=',sum1
    print 'sum2=',sum2

    result=(data*sum1/sum2+1).reshape(shape)
    Tide.SaveDataHdf5(result,output)
    print 'step 3'
    print 'time: %dm %ds'%((time.time()-t0)/60,(time.time()-t0)%60)
    t0=time.time()

    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
#   plt.subplot(2,1,1)
#   plt.plot(hist[1][:-1],hist[0],'b-',label='1')
#   plt.subplot(2,1,2)
#   hist2=np.histogram(result,bins=bin)
#   plt.plot(hist2[1][:-1],hist2[0],'ro-',label='2')
#   plt.legend()
#   plt.savefig('Gau_test.png')
#   print 'step 4'
#   print 'time: %dm %ds'%((time.time()-t0)/60,(time.time()-t0)%60)
#   t0=time.time()
    return result
