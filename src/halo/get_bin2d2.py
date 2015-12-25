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
name=sys.argv[1]
#name='tides00'
#################################################################################
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
########################## Load data ############################################
if rank == 0 :
#################################################################################
    x=np.fft.fftfreq(N,1./N)
    z=np.zeros_like(x)
    KV = ((x**2)[:, None, None] +(x**2)[None, :, None] +(z**2)[None, None, :])**(1. / 2.)
    KP = ((z**2)[:, None, None] +(z**2)[None, :, None] +(x**2)[None, None, :])**(1. / 2.)
    KV=KV.reshape(8*size,-1)
    KP=KP.reshape(8*size,-1)
else :
    KV=[]
    KP=[]
    kappak=[]
################################################################################
bins=10
binlog=np.linspace(0,np.log10(512),bins,endpoint=False)
dbinlog=binlog[2]-binlog[1]
binlog=np.hstack((binlog,binlog[-1]+dbinlog))
bin=10**binlog
bin[0]=0
################################################################################
P_deltak=[]
KV1=[]
KP1=[]
for i in range(8):
    KV1.append(comm.scatter(KV[i::8],root=0))
    KP1.append(comm.scatter(KP[i::8],root=0))
KV1=np.array(KV1)
KP1=np.array(KP1)
################################################################################
if rank==0:
    del KV
    del KP
####################################################################################################
b=np.loadtxt('./result_b')
W=np.loadtxt('./result_W')
################################################################################
if rank==0:
    f=h5py.File('/home/mtx/data/tide/outdata/'+name+'/halo/0.000halo00_wkappa3d_x.hdf5')
    kappa3dx=np.array(f['data'].value,dtype=np.float)
    f.close()
    kappak=np.fft.fftn(kappa3dx)
    kappak=kappak.reshape(8*size,-1)
kappa_k=[]
for i in range(8):
    kappa_k.append(comm.scatter(kappak[i::8],root=0))
kappa_k=np.array(kappa_k)
for i in range(bins):
    for j in range(bins):
        bool1=(bin[j]<=KV1)*(KV1<bin[j+1])
        bool2=(bin[i]<=KP1)*(KP1<bin[i+1])
        bool=bool1*bool2
        if i+j==0:
            if rank==0:
                bool[0,0]=False
        kappa_k[bool]=kappa_k[bool]/b[i,j]*W[i,j]
kappa_k=kappa_k.reshape(-1)
NN=16
ss=len(kappa_k)/NN
combine_data=[]
for i in range(NN):
    x=comm.gather(kappa_k[i*ss:(i+1)*ss],root=0)
    combine_data.append(x)
if rank==0:
    combine_data=np.array(combine_data)
    result=[]
    for i in range(size):
        for j in range(NN):
            result.append(combine_data[j,i])
    result=np.array(result).reshape(1024,1024,1024)
    result=np.fft.ifftn(result).real

    dtype=np.dtype([('kappa','f4')])
    result=np.array(result,dtype=dtype)
    f=h5py.File('/home/mtx/data/tide/outdata/'+name+'/halo/0.000halo00_result_wfkappax.hdf5',mode='w')
    f.create_dataset(name='data',data=result)
    f.close()
