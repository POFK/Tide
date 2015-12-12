#!/usr/bin/env python
# coding=utf-8
import numpy as np
import h5py
import TIDES as ti
###############load log(delta x)#######################
f = h5py.File('/home/mtx/data/tide/outdata/0.000den00_smoothg.hdf5')
data =np.array( f['data'].value,dtype=np.float16)
print data.shape
f.close()
############### partial x #############################
alpha,beta=ti.Tide.Get_Alpha_Beta()
N=1024
L=1.2*10**3
nx=np.fft.fftfreq(N,1./N)
Kx=2*np.pi/L*nx
fk=np.fft.fftn(data)
del data
S=np.ones_like(fk)
for i in range(N):
    S[i,:,:]=fk[i,:,:]*Kx[i]*1j

dtype=np.dtype([('partialX_delta','f4')])
result=np.array(np.fft.ifftn(S).real,dtype=dtype)
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wdensgx.hdf5',mode='w')
f.create_dataset(name='data',data=S)
f.close()
