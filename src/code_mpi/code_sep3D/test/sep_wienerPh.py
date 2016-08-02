#!/usr/bin/env python
# coding=utf-8
'''To get a wiener filter function'''
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
def WienerF(dirPath,noise,bias_cut=9):
    '''dirPath is dir in parameter.py'''
    Pdd=np.loadtxt(dirPath+'Pk_DD')
    Phh=np.loadtxt(dirPath+'Pk_HH')
    Phh[:,1]-=noise
    Pdh=np.loadtxt(dirPath+'Pk_DH')

    n=Pdh[:,2]
#   bias=Pdh[:,1]/Pdd[:,1]
    bias=((Phh[:,1])/Pdd[:,1])**0.5
    b=(bias*n)[:bias_cut].sum()/n[:bias_cut].sum()
#   print 'bias:',b
    k=Pdd[:,0]
    Pk=Pdd[:,1]*b**2
#   Pk=Phh[:,1]

#   INF=open(dirPath+'data.inf','a')
#   INF.writelines('bias=%f\n'% (b))
#   INF.close()

    window=Pk/(Pk+noise)
    f=interpolate.UnivariateSpline(np.log10(k), window, s=0)  #usage : f(log10(k))
#   f=interpolate.interp1d(np.log10(k), window,kind=3)
#   print np.log10(k).min(),np.log10(k).max()

    plt.semilogx(k,window,'bo',linewidth=3,alpha=0.5,label='wiener points')
    plt.semilogx(k,window,'r-',label='interploate')
    #to test
#   test=np.loadtxt('/project/mtx/output/tides10/test/Wiener.txt')
#   plt.semilogx(test[:,0],test[:,1],'g-',linewidth=2,alpha=0.5)
#   plt.ylim([0,1.])
#   plt.show()
    return (f,b,k[0],k[-1])
#f=WienerF('/project/mtx/output/tides10/test/',noise=208.172029)[0]
