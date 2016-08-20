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
print noise
PH=np.loadtxt('../result/tides10/0.0048_PK_HH')
k=np.linspace(PH[:,0].min(),PH[:,0].max(),1000)
def smooth(sigma):
    smooth_K=np.exp(-k**2*sigma**2/2.)**2
    return smooth_K
def wiener(noise):
    W=PH[:,1]/(PH[:,1]+noise)
    return W
def smooth_PH(sigma):
    k=PH[:,0]
    smooth_K=np.exp(-k**2*sigma**2/2.)**2
    return smooth_K

plt.figure('WS')
#plt.semilogx(k,smooth(sigma=1.25),'k-',linewidth=3,label='smooth 1.25')
plt.semilogx(k,smooth(sigma=1.0),'k-',linewidth=3,label='smooth 1.0')
#plt.semilogx(PH[:,0],wiener(noise),'m-',linewidth=3,label='only wiener')
#for i in np.linspace(0.80,1.30,(1.30-0.80)/0.05,endpoint=False):
#    print i
#   plt.semilogx(PH[:,0],wiener(noise)*smooth_PH(sigma=i)/smooth_PH(sigma=1.25),'-',label='wiener & smooth_%3.2f'%i)
#   plt.semilogx(PH[:,0],smooth_PH(sigma=1.25)/(wiener(noise)*smooth_PH(sigma=i)),'-',label='wiener & smooth_%3.2f'%i)
plt.ylim(10**-3,1)
plt.xlim(0.005,2.5)
plt.legend(loc='lower left')
plt.show()




