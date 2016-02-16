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

gamma1=delta_gx*delta_gx-delta_gy*delta_gy
gamma2=2*delta_gx*delta_gy

#####################save data#########################
dtype=np.dtype([('partialX_delta','f4')])
result=np.array(gamma1,dtype=dtype)
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wgamma1.hdf5',mode='w')
f.create_dataset(name='data',data=result)
f.close()

result=np.array(gamma2,dtype=dtype)
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wgamma2.hdf5',mode='w')
f.create_dataset(name='data',data=result)
f.close()

