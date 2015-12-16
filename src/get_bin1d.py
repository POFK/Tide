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
    Pk_d=deltak.reshape(8*size,-1)
    f.close()
    f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_Pk_kappa_delta.hdf5')
    Pk_kd=f['data'].value
    Pk_kd=deltak.reshape(8*size,-1)
    f.close()
    f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_Pk_kappa.hdf5')
    Pk_k=f['data'].value
    Pk_k=deltak.reshape(8*size,-1)
    f.close()
#################################################################################
############################################################
    x=np.fft.fftfreq(N,1./N)
    z=np.zeros_like(x)
    KV = ((x**2)[:, None, None] +(x**2)[None, :, None] +(z**2)[None, None, :])**(1. / 2.)
    KP = ((z**2)[:, None, None] +(z**2)[None, :, None] +(x**2)[None, None, :])**(1. / 2.)
    KV=KV.reshape(8*size,-1)
    KP=KP.reshape(8*size,-1)
else :
    Pk_d=[]
    Pk_kd=[]
    Pk_k=[]
    KV=[]
    KP=[]
    kappak=[]
################################################################################
bins=10
bin=np.linspace(0,np.log10(512),bins,endpoint=False)
dbin=bin[1]-bin[0]
P_deltak=[]
k=[]
for i in range(8):
    Pk_d1.append(comm.scatter(Pk_d[i::8],root=0))
    Pk_kd1.append(comm.scatter(Pk_kd[i::8],root=0))
    Pk_k1.append(comm.scatter(Pk_k[i::8],root=0))
    KV1.append(comm.scatter(KV[i::8],root=0))
    KP1.append(comm.scatter(KP[i::8],root=0))
KV1=np.array(KV1)
KP1=np.array(KP1)
Pk_d1=np.array(Pk_d1)
Pk_d1=np.array(Pk_d1,dtype=np.float)
Pk_kd1=np.array(Pk_kd1)
Pk_kd1=np.array(Pk_kd1,dtype=np.float)
Pk_k1=np.array(Pk_k1)
Pk_k1=np.array(Pk_k1,dtype=np.float)
################################################################################
if rank==0:
    del Pk_d
    del Pk_kd
    del Pk_k
    del KV
    del KP
####################################################################################################
pk1=np.zeros([bins,bins])  #Pk_d1
pk2=np.zeros([bins,bins])  #Pk_kd1
pk3=np.zeros([bins,bins])  #Pk_k1
kn=np.zeros([bins,bins])
for i in range(bins):
    for j in range(bins):
        if rank==0:
            if i+j==0:
                bool1=(10**bin[i]<=k)*(k<(10**(bin[i]+dbin)))
                bool2=(10**bin[i]<=k)*(k<(10**(bin[i]+dbin)))
                bool=bool1*bool2
                bool[0,0]=False
                print bool.shape
            else :
                bool1=(10**bin[i]<=k)*(k<(10**(bin[i]+dbin)))
                bool2=(10**bin[i]<=k)*(k<(10**(bin[i]+dbin)))
                bool=bool1*bool2
            kn[i,j]=len(Pk_d1[bool])
            pk1[i,j]=Pk_d1[bool].sum()
            pk2[i,j]=Pk_kd1[bool].sum()
            pk3[i,j]=Pk_k1[bool].sum()

####################################################################################################
kn=comm.reduce(kn,root=0)
pk1=comm.reduce(pk1,root=0)#Pk_d
pk2=comm.reduce(pk2,root=0)#Pk_kd
pk3=comm.reduce(pk3,root=0)#Pk_k

####################################################################################################
if rank==0:
    b=pk2/pk1
    Pn=pk3-b**2*pk1
    W=pk1/(pk1+Pn/(b**2))
    np.savetxt('result_b',b)
    np.savetxt('result_Pn',Pn)
    np.savetxt('result_W',W)
################################################################################
b,W,Pn = comm.bcast([b,W,Pn] if rank == 0 else None, root = 0)
################################################################################
if rank==0:
    f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wkappa3d_x.hdf5')
    kappa3dx=np.array(f['data'].value,dtype=np.float16)
    f.close()
    kappak=np.fft.fft(kappa3dx)
    kappak=kappak(8*size,-1)
    kappa_k=[]
    for i in range(8):
        kappa_k.append(comm.scatter(kappa_k[i::8],root=0))
kappa_k=np.array(kappa_k)
kappa_k=np.array(kappa_k,dtype=np.float)
for i in range(bins):
    for j in range(bins):
        if rank==0:
            if i+j==0:
                bool1=(10**bin[i]<=k)*(k<(10**(bin[i]+dbin)))
                bool2=(10**bin[i]<=k)*(k<(10**(bin[i]+dbin)))
                bool=bool1*bool2
                bool[0,0]=False
            else :
                bool1=(10**bin[i]<=k)*(k<(10**(bin[i]+dbin)))
                bool2=(10**bin[i]<=k)*(k<(10**(bin[i]+dbin)))
                bool=bool1*bool2
            kappa_k=kappa_k[bool]/b[i,j]*W[i,j]

