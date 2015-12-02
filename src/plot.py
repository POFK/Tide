#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
#data=np.loadtxt('PS_data')
data=np.loadtxt('data_nolog')
plt.plot(np.log10(data[:,0]),np.log10(data[:,1]),'-o')
plt.show()
#plt.savefig('ps.png')
