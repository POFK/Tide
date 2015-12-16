#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
data=np.loadtxt('PS_data_with_histogram')
#data2=np.loadtxt('PS_data_with_histogram')
#data2=np.loadtxt('1.000pk00.dat')
data2=np.loadtxt('PS_data_with_histogram')

#data=np.loadtxt('data_nolog')
#plt.loglog(data[:,0],data[:,1],'-bo')
#plt.loglog(data2[:,0],data2[:,1],'-ro')
plt.plot(np.log10(data2[:,0]),np.log10(data2[:,1]),'-or',alpha=0.4)
plt.plot(np.log10(data[:,0]),np.log10(data[:,1]),'-bo',alpha=0.3)

plt.show()
#plt.savefig('ps.png')
