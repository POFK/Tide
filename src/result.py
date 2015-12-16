#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import *
import h5py
from mpi4py import MPI
'''get kappa(kv,kp),b,w, and get kappa(x)'''
N=1024
L=1.2*10**3
#################################################################################
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
#################################################################################
#f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wkappa3d_x.hdf5')
#kappa3dx=np.array(f['data'].value,dtype=np.float16)
#f.close()
#################################################################################
if rank == 0 :
#    f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wkappa3d_x.hdf5')
#    kappa3dx=np.array(f['data'].value,dtype=np.float16)
#    f.close()

    bins=10
    x=np.fft.fftfreq(N,1./N)
    z=np.zeros_like(x)
    kv = ((x**2)[:, None, None] +(x**2)[None, :, None] +(z**2)[None, None, :])**(1. / 2.)
    kp = ((z**2)[:, None, None] +(z**2)[None, :, None] +(x**2)[None, None, :])**(1. / 2.)
    kv=kv.reshape(-1)
    kp=kp.reshape(-1)
    kn_max = 512
    kn_min = 0

