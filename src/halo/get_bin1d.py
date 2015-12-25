#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import *
import h5py
from mpi4py import MPI
import sys
'''get kappa(kv,kp),b,w, and get kappa(x)'''
N=1024
L=1.2*10**3
filename1=sys.argv[1]
filename2=sys.argv[2]
#################################################################################
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
########################## Load data ############################################
f=h5py.File(filename1,'r')#'/home/mtx/data/tide/outdata/old_test/0.000den00_Pk_kappa_delta.hdf5')
Pk_d=f['data'][rank*(1024/size):(rank+1)*(1024/size)]
Pk_d=np.array(Pk_d,dtype=np.float)
f.close()
#############################################################################
x=np.fft.fftfreq(N,1./N)
K = ((x**2)[rank*(1024/size):(rank+1)*(1024/size)][:, None, None] +(x**2)[None, :, None] +(x**2)[None, None, :])**(1. / 2.)
################################################################################
bins=20
bin=np.linspace(0,np.log10(512),bins,endpoint=False)
dbin=bin[1]-bin[0]
################################################################################
kx=[]
Pk=[]
n=[]
for i in range(bins):
    bool=(10**bin[i]<=K)*(K<(10**(bin[i]+dbin)))
    n.append(len(K[bool]))
    Pk.append(Pk_d[bool].sum())
    kx.append(K[bool].sum())
n=np.array(n)
Pk=np.array(Pk)
kx=np.array(kx)

################################################################################################
n_1=comm.reduce(n,root=0)
Pk_1=comm.reduce(Pk,root=0)#Pk_d
kx_1=comm.reduce(kx,root=0)#Pk_kd
if rank==0:
    n=n_1
    kx=kx_1*np.pi*2/L/n
    Pk=Pk_1/n
    np.savetxt(filename2,np.c_[kx,Pk,n])#'/home/mtx/data/tide/outdata/old_test/PS_Pkkd',np.c_[kx,Pk,n])
