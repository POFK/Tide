#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
data=np.loadtxt('PS_data')
data2=np.loadtxt('1.000pk00.dat')
#data=np.loadtxt('data_nolog')
plt.loglog(data[:,0],data[:,1],'-bo')
plt.loglog(data2[:,0],data2[:,1],'-ro')
plt.show()
#plt.savefig('ps.png')
