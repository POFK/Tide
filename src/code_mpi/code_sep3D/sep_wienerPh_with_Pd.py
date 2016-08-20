#!/usr/bin/env python
# coding=utf-8
'''To get a wiener filter function:
    Here, W=b^2*Pd/(Ph+shotnoise)'''
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
def WienerF(dirPath,noise,bias_cut=6,mode=None):
    '''dirPath is dir in parameter.py'''
    Pdd=np.loadtxt(dirPath+'Pk_DD')
    Phh=np.loadtxt(dirPath+'Pk_HH')
    Pdh=np.loadtxt(dirPath+'Pk_DH')
    Phh[:,1]-=noise

    n=Pdh[:,2]
    bias=Pdh[:,1]/Pdd[:,1]
    b=(bias*n)[:bias_cut].sum()/n[:bias_cut].sum()
    k=Pdd[:,0]
    Pk=Phh[:,1]
    if mode==None:
        print 'please choose wiener model'
    if mode==1:
        print 'wiener with Ph'
        window=Pk/(Pk+noise)                    # Wiener with Ph
    if mode==2:
        print 'wiener with Pd, where bias is k-independent, here we set bias=1'
        window=Pdd[:,1]/(Pk+noise)         # wiener with Pd, where bias is k-independent    
    if mode==3:
        print 'wiener with Pd, where bias is k-dependent'
        window=bias**2*Pdd[:,1]/(Pk+noise)      # wiener with Pd, where bias is k-dependent
#  set the final point of window
    k[-1]=5
#   window[-1]=0.

    f=interpolate.UnivariateSpline(np.log10(k), window, s=0)  #usage : f(log10(k))
    return (f,b,k[0],k[-1])
#f=WienerF('/project/mtx/output/tides10/test/',noise=208.172029)[0]
