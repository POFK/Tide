#!/usr/bin/env python
# coding=utf-8
import h5py
import numpy as np
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wdensgx.hdf5')
g=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wdensgy.hdf5')
delta_gx=np.array(f['data'].value,dtype=np.float16)
delta_gy=np.array(g['data'].value,dtype=np.float16)
f.close()
g.close()
############################## gamma ##############################
gamma1=delta_gx*delta_gx-delta_gy*delta_gy
gamma2=2*delta_gx*delta_gy
gamma1_k=np.fft.fftn(gamma1)
gamma2_k=np.fft.fftn(gamma2)
############################## kappa ##############################
N=1024
L=1.2*10**3
nx=np.fft.fftfreq(N,1./N)
Kx=2*np.pi/L*nx
zero=np.zeros_like(Kx)
k1=Kx[:,None,None]+zero[None,:,None]+zero[None,None,:]
k2=Kx[None,:,None]+zero[:,None,None]+zero[None,None,:]
S=k1**2+k2**2

S[0,0,:]=np.ones_like(S[0,0,:])
kappa_3dk=2*(Kx[:,None,None]**2+Kx[None,:,None]**2+Kx[None,None,:]**2)/(S**2)*((k1**2-k2**2)*gamma1_k+2*k1*k2*gamma2_k)
del S
############################## save data ##############################
kappa_3dx=np.fft.ifftn(kappa_3dk).real
dtype=np.dtype([('kappa3dx','f4')])
result=np.array(kappa_3dx,dtype=dtype)
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wkappa3d_x.hdf5',mode='w')
f.create_dataset(name='data',data=result)
f.close()


