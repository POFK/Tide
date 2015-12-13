
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
############################## kappa ##############################
nx=np.fft.fftfreq(N,1./N)
Kx=2*np.pi/L*nx
zero=np.zeros_like(Kx)
k1=Kx[:,None,None]+zero[None,:,None]+zero[None,None,:]
k2=Kx[None,:,None]+zero[:,None,None]+zero[None,None,:]
kappa_2d=1./(np.add(k1**2,k2**2))*(np.subtract(k1**2,k2**2)*gamma1+2*k1*k2*gamma2)
kappa_3d=2*(kx[:,None,None]**2+kx[None,:,None]**2+kx[None,None,:]**2)/(3*(np.add(k1**2,k2**2))**2)*kappa_2d
############################## save data ##############################
dtype=np.dtype([('kappa3d','f4')])
result=np.array(kappa_3d,dtype=dtype)
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wkappa3d.hdf5',mode='w')
f.create_dataset(name='data',data=result)
f.close()


