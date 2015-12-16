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
#    f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_Pk_delta.hdf5')
#    deltak=np.array(f['data'].value,dtype=np.float16).reshape(size,-1)
#    f.close()

    bins=10
    x=np.fft.fftfreq(N,1./N)
    z=np.zeros_like(x)
    KV = ((x**2)[:, None, None] +(x**2)[None, :, None] +(z**2)[None, None, :])**(1. / 2.)
    KP = ((z**2)[:, None, None] +(z**2)[None, :, None] +(x**2)[None, None, :])**(1. / 2.)
    kv=kv.reshape(size,-1)
    kp=kp.reshape(size,-1)
bin=np.linspace(0,np.log10(512),10,endpoint=False)
dbin=bin[1]-bin[0]

a=comm.scatter(deltak,root=0)
kv=comm.scatter(KV,root=0)
kp=comm.scatter(KP,root=0)
bool=[]
for v in range(10):
    for p in range(10):
        if v+p==0:
            bool[v,p]=
        bool[i,j]=()
if rank==0:


        
