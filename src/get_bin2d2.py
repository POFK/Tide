#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import *
import h5py
from mpi4py import MPI
'''get kappa(kv,kp),b,w, and get kappa(x)'''
N=1024
L=1.2*10**3
#name='tides00'
name='old_test'
#################################################################################
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
########################## Load data ############################################
if rank == 0 :
    f=h5py.File('/home/mtx/data/tide/outdata/'+name+'/0.000den00_Pk_delta.hdf5')
    Pk_d=f['data'].value
    Pk_d=Pk_d.reshape(8*size,-1)
    f.close()
    f=h5py.File('/home/mtx/data/tide/outdata/'+name+'/0.000den00_Pk_delta_kappa.hdf5')
    Pk_kd=f['data'].value
    Pk_kd=Pk_kd.reshape(8*size,-1)
    f.close()
    f=h5py.File('/home/mtx/data/tide/outdata/'+name+'/0.000den00_Pk_kappa.hdf5')
    Pk_k=f['data'].value
    Pk_k=Pk_k.reshape(8*size,-1)
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
#bins=10
#bin=np.linspace(0,np.log10(512),bins,endpoint=False)
#dbin=bin[1]-bin[0]
bins=10
binlog=np.linspace(0,np.log10(512),bins,endpoint=False)
dbinlog=binlog[2]-binlog[1]
binlog=np.hstack((binlog,binlog[-1]+dbinlog))
bin=10**binlog
bin[0]=0
################################################################################
P_deltak=[]
Pk_d1=[]
Pk_kd1=[]
Pk_k1=[]
KV1=[]
KP1=[]
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
        bool1=(bin[j]<=KV1)*(KV1<bin[j+1])
        bool2=(bin[i]<=KP1)*(KP1<bin[i+1])
        bool=bool1*bool2
        if i+j==0:
            if rank==0:
                bool[0,0]=False
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
    W=pk1/kn/(pk1/kn+Pn/(b**2))
    Pd=pk1/kn
    np.savetxt('/home/mtx/data/tide/outdata/'+name+'/result_Pd',Pd)
    np.savetxt('/home/mtx/data/tide/outdata/'+name+'/result_b',b)
    np.savetxt('/home/mtx/data/tide/outdata/'+name+'/result_Pn',Pn)
    np.savetxt('/home/mtx/data/tide/outdata/'+name+'/result_W',W)
    np.savetxt('/home/mtx/data/tide/outdata/'+name+'/result_n',kn)
#################################################################################
b,W,Pn = comm.bcast([b,W,Pn] if rank == 0 else None, root = 0)
################################################################################
if rank==0:
    f=h5py.File('/home/mtx/data/tide/outdata/'+name+'/0.000den00_kappa3dx.hdf5')
    kappa3dx=np.array(f['data'].value,dtype=np.float16)
    f.close()
    kappak=np.fft.fft(kappa3dx)
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
kappa_k=L**3*kappa_k.reshape(-1)
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
    f=h5py.File('/home/mtx/data/tide/outdata/'+name+'/0.000den00_result_kappa.hdf5',mode='w')
    f.create_dataset(name='data',data=result)
    f.close()
