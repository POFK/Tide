#!/usr/bin/env python
# coding=utf-8
#from TIDES import *
import h5py
from parameter import *
import sys

'''get kappa(kv,kp),b,w, and get kappa(x)'''
inputfile=sys.argv[2]
Outputfile=sys.argv[3]

f=h5py.File(inputfile)
Pk_d=f['data'][mpi_index[rank].tolist()]
f.close()
k=((mpi_fn[rank]**2)[:,None,None]+(fn**2)[None,:,None]+(fnc**2)[None,None,:])**(0.5)
k=np.array(k,dtype=np.float64)
bins=20
bin=np.linspace(0,np.log10(512),bins,endpoint=False)
dbin=bin[1]-bin[0]

n=[]
Pk=[]
kx=[]
for i in range(bins):
    bool=(10**bin[i]<=k)*(k<(10**(bin[i]+dbin)))
    if i==0:
        if rank==0:
            bool[0,0]=False
    n.append(len(k[bool]))
    Pk.append(Pk_d[bool].sum())
    kx.append(k[bool].sum())
n=np.array(n)
Pk=np.array(Pk)
kx=np.array(kx)
n_1=comm.reduce(n,root=0)
Pk_1=comm.reduce(Pk,root=0)
kx_1=comm.reduce(kx,root=0)
if rank==0:
    n=n_1
    kx=kx_1*Kf/n
    Pk=Pk_1/n
    np.savetxt(Outputfile,np.c_[kx,Pk,n])#'/home/mtx/data/tide/outdata/old_test/PS_Pkkd',np.c_[kx,Pk,n])
