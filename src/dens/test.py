#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import *
import h5py
from mpi4py import MPI
import sys
#import time
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
f=h5py.File('/home/mtx/data/tide/outdata/'+name+'/0.000den00_Pk_delta.hdf5','r')
Pk_d=f['data'][rank*(1024/size):(rank+1)*(1024/size)]
Pk_d=np.array(Pk_d,dtype=np.float)
f.close()

f=h5py.File('/home/mtx/data/tide/outdata/'+name+'/0.000den00_Pk_delta_kappa.hdf5','r')
Pk_kd=f['data'][rank*(1024/size):(rank+1)*(1024/size)]
Pk_kd=np.array(Pk_kd,dtype=np.float)
f.close()

f=h5py.File('/home/mtx/data/tide/outdata/'+name+'/0.000den00_Pk_kappa.hdf5','r')
Pk_k=f['data'][rank*(1024/size):(rank+1)*(1024/size)]
Pk_k=np.array(Pk_k,dtype=np.float)
f.close()
#################################################################################
x=np.fft.fftfreq(N,1./N)
z=np.zeros_like(x)
KV = ((x**2)[rank*(1024/size):(rank+1)*(1024/size)][:, None, None] +(x**2)[None, :, None] +(z**2)[None, None, :])**(1. / 2.)
KP = ((z**2)[rank*(1024/size):(rank+1)*(1024/size)][:, None, None] +(z**2)[None, :, None] +(x**2)[None, None, :])**(1. / 2.)
################################################################################
bins=10
binlog=np.linspace(0,np.log10(512),bins,endpoint=False)
dbinlog=binlog[2]-binlog[1]
binlog=np.hstack((binlog,binlog[-1]+dbinlog))
bin=10**binlog
bin[0]=0
####################################################################################################
pk1=np.zeros([bins,bins])  #Pk_d
pk2=np.zeros([bins,bins])  #Pk_kd
pk3=np.zeros([bins,bins])  #Pk_k
kn=np.zeros([bins,bins])
for i in range(bins):
    for j in range(bins):
        bool1=(bin[j]<=KV)*(KV<bin[j+1])
        bool2=(bin[i]<=KP)*(KP<bin[i+1])
        bool=bool1*bool2
        if i+j==0:
            if rank==0:
                bool[0,0,0]=False
        kn[i,j]=len(Pk_d[bool])
        pk1[i,j]=Pk_d[bool].sum()
        pk2[i,j]=Pk_kd[bool].sum()
        pk3[i,j]=Pk_k[bool].sum()
################################################################################
        kn[i,j]=comm.reduce(kn[i,j],root=0,op=MPI.SUM)
        pk1[i,j]=comm.reduce(pk1[i,j],root=0,op=MPI.SUM)#Pk_d
        pk2[i,j]=comm.reduce(pk2[i,j],root=0,op=MPI.SUM)#Pk_kd
        pk3[i,j]=comm.reduce(pk3[i,j],root=0,op=MPI.SUM)#Pk_k
####################################################################################################
if rank==0:
    b=pk2/pk1
    Pn=(pk3-b**2*pk1)/kn
    W=pk1/(pk1+Pn/(b**2))
    Pka=pk3/kn
    np.savetxt('/home/mtx/data/tide/outdata/'+name+'/result_b',b)
    np.savetxt('/home/mtx/data/tide/outdata/'+name+'/result_Pn',Pn)
    np.savetxt('/home/mtx/data/tide/outdata/'+name+'/result_W',W)
    np.savetxt('/home/mtx/data/tide/outdata/'+name+'/result_n',kn)
    np.savetxt('/home/mtx/data/tide/outdata/'+name+'/result_Pk',Pka)

