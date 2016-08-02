#!/usr/bin/env python
# coding=utf-8
'''
plot 1D Pn
'''
import sys
import numpy as np
import matplotlib.pyplot as plt
bias_cut=9
path=['tides10/CIC_0.0048_3D_NoGau_s1.25_NoWiener/',
    'tides10/CIC_0.0036_3D_NoGau_s1.25_NoWiener/',
    'tides10/CIC_0.0024_3D_NoGau_s1.25_NoWiener/',
    'tides10/CIC_0.0012_3D_NoGau_s1.25_NoWiener/']
num_den=['0.0048','0.0036','0.0024','0.0012']
def f(file_path,label):
    PATH='/project/mtx/output/'+file_path
    print PATH
    Phh=np.loadtxt(PATH+'Pk_HH')
    Pdh=np.loadtxt(PATH+'Pk_DH')
    Pdd=np.loadtxt(PATH+'Pk_DD')
    n=Pdh[:,2]
    bias=Pdh[:,1]/Pdd[:,1]
    b=(bias*n)[:bias_cut].sum()/n[:bias_cut].sum()
    Pn=(Phh[:,1]-b**2*Pdd[:,1])/(b**2*Pdd[:,1])
    print b

    plt.plot(Pdh[:,0],Pn,'.-',label=label)
#   plt.axhline(y=b,linestyle='-.')
#   plt.text(Pdh[8,0],b,'$b=%.6f$'%b)
    return Pdh[:,0]

plt.figure('noise')
plt.title('noise')
plt.subplot(2,1,1)
for i in np.arange(len(path)):
    k=f(path[i],num_den[i])

plt.axhline(y=0,linestyle='-.')
plt.axhline(y=1,linestyle='-.')
plt.xlim([k[0]*0.9,k[-1]*1.1])
plt.xscale('log')
plt.legend(loc='upper left')

plt.subplot(2,1,2)
for i in np.arange(len(path)):
    k=f(path[i],num_den[i])

plt.xlim([k[0]*0.9,k[-1]*1.1])
plt.ylim([-0.05,0.4])
plt.ylabel('$(P_{h}-b^2P_{\delta})/b^2P_{\delta}$')
plt.xlabel('$k$')
plt.xscale('log')
plt.legend(loc='upper left',ncol=2)
plt.grid()

plt.show()
