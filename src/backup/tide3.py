#!/usr/bin/env python
# coding=utf-8
import struct
import numpy as np
import matplotlib.pyplot as plt
from TIDES import *
import h5py
####################################################
N = 1024
L = 1.2 * 10**3  # Mpc
H = L / 1024.
x = np.fft.fftfreq(N,1./N)  # x: 0,1,2,...,512,511,...,2,1
############################################################
#data = Tide.LoadData(filename='/home/zhm/tides00/0.000den00.bin')
#Pk=Tide.AutoPowerSpectrum(data,window=True)
#dtype=np.dtype([('Pk','f4')])
#result=np.array(Pk,dtype=dtype)
#f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_Pk_delta.hdf5',mode='w')
#f.create_dataset(name='data',data=result)
#f.close()
############################################################
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_Pk_delta.hdf5')
Pk=np.array(f['data'].value,dtype=np.float)
############################################################


kn = ((x**2)[:, None, None] +
      (x**2)[None, :, None] +
      (x**2)[None, None, :])**(1. / 2.)
kn_max = 512
kn_min = 1
x = np.linspace(np.log10(kn_min), np.log10(kn_max), 20, endpoint=False)
dx=x[1]-x[0]
x=np.hstack((x,x[-1]+dx))
############################################################
n,bin1=np.histogram(kn,bins=10**x)
k,bin2=np.histogram(kn,bins=10**x,weights=kn)
P,bin3=np.histogram(kn,bins=10**x,weights=Pk)
k=np.pi*2*k/L/n
P=P/n#/L**3
######### save data with no log###############
np.savetxt('PS_data_with_histogram', np.c_[k, P, n])
#############################plot###############################
plt.plot(np.log10(k),np.log10(P),'-o')
plt.savefig('test.png')
