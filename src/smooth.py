#!/usr/bin/env python
# coding=utf-8
import struct 
#from mpi4py import MPI
import numpy as np
import matplotlib.pyplot as plt
import h5py
####################################################
N=1024
L=1.2*10**3   #Mpc
H=L/1024.
####################################################
class Tide():
    @classmethod
    def LoadData(self,filename='/home/mtx/data/tide/0.000den00.bin'):
        f=open(filename,'rb')
        data=f.read()
        f.close()
        data=struct.unpack('1073741824f',data)
        data=np.array(data,dtype=np.float16)
        data=data.reshape((1024,1024,1024),order='F')
        return data
    @classmethod
    def GetX(self):
        x=np.arange(1024)
        for i in np.arange(1,1024/2+1):
            x[1024-i]=x[i]
        return x
######################## Load data and Window func #######################
#if rank==0:
data=Tide.LoadData()#filename='/home/zhm/tides00/0.000den00.bin')
x=Tide.GetX()                 #x: 0,1,2,...,512,511,...,2,1
delta_k=np.fft.fftn(data)
del data
k=(x[:,None,None]**2.+x[None,:,None]**2.+x[None,None,:]**2.)**(1./2.)
sigma=1.25
smoothed_k=delta_k*np.exp(-k*k*sigma**2)
del delta_k
smoothed_x=np.fft.ifft(smoothed_k)
del smoothed_k
dtype=np.dtype([('smoothed_x','f4')])
smoothed_x=np.array(np.abs(smoothed_x),dtype=dtype)
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_smooth.hdf5',mode='w')
f.create_dataset(name='data',data=smoothed_x)
f.close()
