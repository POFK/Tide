#!/usr/bin/env python
# coding=utf-8
############################################################
#To find a optimal smoothing kernel of the reconstruction  #
#with wiener filter.                                       #
############################################################

import numpy as np
import matplotlib.pyplot as plt
import sys
noise=1./(4.8*10**-3)
bias=0.964845
print noise
#PH=np.loadtxt('../result/tides10/0.0048_PK_HH')

PH=np.loadtxt('/project/mtx/output/tides10/CIC_0.0048_3D_NoGau_s1.25_NoWiener/Pk_HH')
PD=np.loadtxt('/project/mtx/output/tides10/CIC_0.0048_3D_NoGau_s1.25_NoWiener/Pk_DD')
PDH=np.loadtxt('/project/mtx/output/tides10/CIC_0.0048_3D_NoGau_s1.25_NoWiener/Pk_DH')
bias_cut=9
n=PH[:,2]
bias1=PDH[:,1]/PD[:,1]
bias2=np.sqrt(PH[:,1]/PD[:,1])
b1=(bias1*n)[:bias_cut].sum()/n[:bias_cut].sum()
b2=(bias2*n)[:bias_cut].sum()/n[:bias_cut].sum()
print b1
print b2
k=np.linspace(PH[:,0].min(),PH[:,0].max(),1000)
def smooth(sigma):
    smooth_K=np.exp(-k**2*sigma**2/2.)**2
    return smooth_K
def wiener(noise):
    W=(PH[:,1]-noise)/PH[:,1]
    return W
def smooth_PH(sigma):
    k=PH[:,0]
    smooth_K=np.exp(-k**2*sigma**2/2.)**2
    return smooth_K
def wiener2(noise):
    W=(bias1**2*PD[:,1])/PH[:,1]
    return W



plt.figure('WS')
plt.semilogx(k,smooth(sigma=1.25),'k-',linewidth=3,label='smooth 1.25')
#plt.semilogx(k,smooth(sigma=2.5),'r-',linewidth=3,label='smooth 2.5')
plt.semilogx(PH[:,0],wiener(noise),'m-',linewidth=3,label='only wiener')
plt.semilogx(PH[:,0],wiener2(noise),'r-',linewidth=3,label='only wiener2')
for i in np.linspace(0.80,2.50,(2.50-0.80)/0.1,endpoint=False):
    print i
    plt.semilogx(PH[:,0],wiener2(noise)*smooth_PH(sigma=i),'-',label='wiener & smooth_%3.2f'%i)
#plt.ylim(10**-3,1)
plt.xlim(0.005,2.5)
plt.legend(loc='lower left')
plt.show()




