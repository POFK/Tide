#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
#data=np.loadtxt('/home/mtx/data/tide/outdata/tides00/PS_DD')
data=np.loadtxt('PS_data')
#data2=np.loadtxt('/home/zhm/btides/powerk/output/0.000pk00.dat')
data2=np.loadtxt('0.000pk00.dat')

#data2=np.loadtxt('PS_Pkappa')

#data=np.loadtxt('data_nolog')
#plt.loglog(data[:,0],data[:,1],'-bo')
#plt.loglog(data2[:,0],data2[:,1],'-ro')
plt.loglog(data2[:,0],data2[:,1],'-or',alpha=0.4)
plt.loglog(data[:,0],data[:,1],'-bo',alpha=0.3)

plt.show()
print data2[:,1]/data[:,1]
#plt.savefig('ps.png')
