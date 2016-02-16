#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import *
import h5py
import sys
'''get kappa(kv,kp),b,w, and get kappa(x)'''
name=sys.argv[1]
#name='tides00'
#################################################################################
f=h5py.File('/home/mtx/data/tide/outdata/'+name+'/halo/0.000halo00_wkappa3d_x.hdf5')
kappa3dx=f['data'].value
f.close()
kappak=np.fft.fftn(kappa3dx)
g=h5py.File('/home/mtx/data/com.hdf5')
wf=g['data'].value
g.close()
wfkappak=wf*kappak
result=np.fft.ifftn(wfkappak).real
f=h5py.File('/home/mtx/data/tide/outdata/'+name+'/halo/0.000halo00_result_wfkappax.hdf5.test',mode='w')
f.create_dataset(name='data',dtype='f4',data=result)
f.close()
################################################################################
