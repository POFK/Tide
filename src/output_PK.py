#!/usr/bin/env python
# coding=utf-8
import numpy as np
import h5py
from TIDES import *
N=1024.
L=1.2*10**3
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wkappa3d_x.hdf5')
kappa3dx=np.array(f['data'].value,dtype=np.float16)
f.close()
deltax=Tide.LoadData(filename='/home/mtx/data/tide/0.000den00.bin')
kappa3dk=np.fft.fftn(kappa3dx)
deltak=np.fft.fftn(deltax)
Pk_delta=1./L**3*Tide.AutoPowerSpectrum(deltax,window=True)
###################save data#####################
dtype=np.dtype([('Pk','f4')])

result=np.array(Pk_delta,dtype=dtype)
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_Pk_delta.hdf5',mode='w')
f.create_dataset(name='data',data=result)
f.close()

Pk_kappa=1./L**3*np.abs(kappa3dk)**2
Pk_kappa_delta=1./L**3*(kappa3dk*deltak.conjugate()+kappa3dk.conjugate()*deltak)/2
del kappa3dx
del deltax

result=np.array(Pk_kappa,dtype=dtype)
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_Pk_kappa.hdf5',mode='w')
f.create_dataset(name='data',data=result)
f.close()

result=np.array(Pk_kappa_delta.real,dtype=dtype)
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_Pk_kappa_delta.hdf5',mode='w')
f.create_dataset(name='data',data=result)
f.close()
