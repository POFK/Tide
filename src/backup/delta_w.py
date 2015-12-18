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
############### delta_g^k #############################
wk=Tide.Get_wk()
N=1024
#Q=0.1681732
L=1.2*10**3
nx=np.fft.fftfreq(N,1./N)
Kx=2*np.pi/L*nx
zero=np.zeros_like(Kx)
K=np.sqrt(Kx[:,None,None]**2+Kx[None,:,None]**2+Kx[None,None,:]**2)
K[0,0,0]=10**(-4)
delta_gk=np.fft.fftn(data)
del data
W=wk(K)
W[0,0,0]=0
##############################delta_g^wx##############################
delta_gk_wx=delta_gk*W*1j*(Kx[:,None,None]+zero[None,:,None]+zero[None,None,:])
del K
dtype=np.dtype([('partialX_delta','f4')])
result=np.array(np.fft.ifftn(delta_gk_wx).real,dtype=dtype)
del delta_gk_wx
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wdensgx.hdf5',mode='w')
f.create_dataset(name='data',data=result)
f.close()
print 'deltagx is ok'
############################## delta_g^wy #############################
delta_gk_wy=delta_gk*W*1j*(Kx[None,:,None]+zero[:,None,None]+zero[None,None,:])
result=np.array(np.fft.ifftn(delta_gk_wy).real,dtype=dtype)
del delta_gk_wy
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wdensgy.hdf5',mode='w')
f.create_dataset(name='data',data=result)
f.close()
print 'deltagy is ok'

