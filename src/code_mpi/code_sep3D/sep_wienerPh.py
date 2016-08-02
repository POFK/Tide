#!/usr/bin/env python
# coding=utf-8
'''To get a wiener filter function:
    Here, W=Ph/(Ph+shotnoise)'''
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
def WienerF(dirPath,noise,bias_cut=9):
    '''dirPath is dir in parameter.py'''
    Pdd=np.loadtxt(dirPath+'Pk_DD')
    Phh=np.loadtxt(dirPath+'Pk_HH')
    Pdh=np.loadtxt(dirPath+'Pk_DH')
    Phh[:,1]-=noise

    n=Pdh[:,2]
    bias=Pdh[:,1]/Pdd[:,1]
#   bias=((Phh[:,1])/Pdd[:,1])**0.5
    b=(bias*n)[:bias_cut].sum()/n[:bias_cut].sum()
    k=Pdd[:,0]
    Pk=Phh[:,1]
    window=Pk/(Pk+noise)
#  set the final point of window
    k[-1]=5
#   window[-1]=0.

    f=interpolate.UnivariateSpline(np.log10(k), window, s=0)  #usage : f(log10(k))
#   f=interpolate.interp1d(np.log10(k), window,kind=3)

#   plt.semilogx(k,window,'bo',linewidth=3,alpha=0.5)
#   plt.semilogx(k,window,'r-')
#   #to test
#   test=np.loadtxt('/project/mtx/output/tides10/test/Wiener.txt')
#   plt.semilogx(2*np.pi/1200.*np.linspace(1,512.*3.**0.5,1000),f(np.log10(2*np.pi/1200.*np.linspace(1,512.*3**0.5,1000))),'y-',linewidth=2,alpha=0.5)
#   plt.semilogx(test[:,0],test[:,1],'g-',linewidth=2,alpha=0.5)
#   plt.ylim([0,1.])
#   plt.show()
    return (f,b,k[0],k[-1])
#f=WienerF('/project/mtx/output/tides10/test/',noise=208.172029)[0]
