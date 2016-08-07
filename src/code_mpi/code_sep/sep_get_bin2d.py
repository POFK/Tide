#!/usr/bin/env python
# coding=utf-8
#from TIDES import *
import h5py
from parameter import *


'''get kappa(kv,kp),b,w, and get kappa(x)'''
input1=PathBin2dInput1
input2=PathBin2dInput2
input3=PathBin2dInput3
Outfile=PathBin2dOutput
################################################################################
f=h5py.File(input1)
Pk_dd=f['data'][mpi_index[rank].tolist()]
f.close()
f=h5py.File(input2)
Pk_dk=f['data'][mpi_index[rank].tolist()]
f.close()
f=h5py.File(input3)
Pk_kk=f['data'][mpi_index[rank].tolist()]
f.close()

binlog=np.linspace(0,np.log10(512),bins,endpoint=False)
dbinlog=binlog[2]-binlog[1]
binlog=np.hstack((binlog,binlog[-1]+dbinlog))
bin=10**binlog
bin[0]=0


KV=((mpi_fn[rank]**2)[:,None,None]+(fn**2)[None,:,None]+np.zeros_like(fnc**2)[None,None,:])**(0.5)
KV=np.array(KV,dtype=np.float64)
KP=(np.zeros_like(mpi_fn[rank]**2)[:,None,None]+np.zeros_like(fn**2)[None,:,None]+(fnc**2)[None,None,:])**(0.5)
KP=np.array(KP,dtype=np.float64)
pk1=np.zeros([bins,bins])  #Pk_dd
pk2=np.zeros([bins,bins])  #Pk_dk
pk3=np.zeros([bins,bins])  #Pk_kk
kn=np.zeros([bins,bins])
for i in range(bins):
    for j in range(bins):
        bool1=(bin[j]<=KV)*(KV<bin[j+1])
        bool2=(bin[i]<=KP)*(KP<bin[i+1])
        bool=bool1*bool2
        if i+j==0:
            if rank==0:
                bool[0,0]=False
        kn[i,j]=len(Pk_dd[bool])
        pk1[i,j]=Pk_dd[bool].sum()
        pk2[i,j]=Pk_dk[bool].sum()
        pk3[i,j]=Pk_kk[bool].sum()

####################################################################################################
kn=comm.reduce(kn,root=0)
pk1=comm.reduce(pk1,op=MPI.SUM,root=0)#Pk_d
pk2=comm.reduce(pk2,op=MPI.SUM,root=0)#Pk_kd
pk3=comm.reduce(pk3,op=MPI.SUM,root=0)#Pk_k
if rank==0:
    b=pk2/pk1
    Pn=pk3-b**2*pk1
    W=pk1/(pk1+Pn/(b**2))
    Pn=(Pn/kn)/(pk1/kn+ShotNoise)/b**2
    Pd=pk1/kn
    Pk=pk3/kn
    Pdk=pk2/kn
    CC=pk2/np.sqrt(pk1*pk3)
    np.savetxt(Outfile+'result_Pd',Pd)
    np.savetxt(Outfile+'result_Pk',Pk)
    np.savetxt(Outfile+'result_Pdk',Pdk)
    np.savetxt(Outfile+'result_CC',CC)
    np.savetxt(Outfile+'k_bin',bin)
    np.savetxt(Outfile+'result_b',b)
    np.savetxt(Outfile+'result_Pn',Pn)
    np.savetxt(Outfile+'result_W',W)
    np.savetxt(Outfile+'result_n',kn)