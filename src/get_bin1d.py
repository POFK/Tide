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
########################## Load data ############################################
if rank == 0 :
    f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_Pk_delta.hdf5')
    Pk_d=f['data'].value
    Pk_d=Pk_d.reshape(8*size,-1)
    f.close()
#################################################################################
############################################################
    x=np.fft.fftfreq(N,1./N)
    K = ((x**2)[:, None, None] +(x**2)[None, :, None] +(x**2)[None, None, :])**(1. / 2.)
    K=K.reshape(8*size,-1)
else :
    Pk_d=[]
    K=[]
################################################################################
bins=20
bin=np.linspace(0,np.log10(512),bins,endpoint=False)
dbin=bin[1]-bin[0]
P=[]
kn=[]
for i in range(8):
    P.append(comm.scatter(Pk_d[i::8],root=0))
    kn.append(comm.scatter(K[i::8],root=0))
kn=np.array(kn)
P=np.array(P)
P=np.array(P,dtype=np.float)
################################################################################
if rank==0:
    del Pk_d
    del K
####################################################################################################
kx=[]
Pk=[]
n=[]
for i in range(bins):
    bool=(10**bin[i]<=kn)*(kn<(10**(bin[i]+dbin)))
    if i==0:
        if rank==0:
            bool[0,0]=False
    n.append(len(kn[bool]))
    Pk.append(P[bool].sum())
    kx.append(kn[bool].sum())
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
    np.savetxt('PS_test_mpi_bin1d',np.c_[kx,Pk,n])
