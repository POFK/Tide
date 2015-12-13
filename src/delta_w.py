#!/usr/bin/env python
# coding=utf-8
import numpy as np
import h5py
from TIDES import *
###############load log(delta x)#######################
f = h5py.File('/home/mtx/data/tide/outdata/0.000den00_smoothg.hdf5')
data =np.array( f['data'].value,dtype=np.float16)
print data.shape
f.close()
############### delta_g^x #############################
wk=Tide.Get_wk()
N=1024
L=1.2*10**3
nx=np.fft.fftfreq(N,1./N)
Kx=2*np.pi/L*nx
zero=np.zeros_like(Kx)
K=np.sqrt(Kx[:,None,None]**2+Kx[None,:,None]**2+Kx[None,None,:]**2)
delta_gk=np.fft.fftn(data)
del data
delta_gk_wx=delta_gk*wk(K)*1j*(Kx[:,None,None]+zero[None,:,None]+zero[None,None,:])
del delta_gk
del K
dtype=np.dtype([('partialX_delta','f4')])
result=np.array(np.abs(np.fft.ifftn(delta_gk_wx)),dtype=dtype)
del delta_gk_wx
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wdensgx.hdf5',mode='w')
f.create_dataset(name='data',data=S)
f.close()
g=open('./home/mtx/data/tide/outdata/0.000den00_wdensgx.bin','wb')
g.write(result.reshape(-1))
g.close()
