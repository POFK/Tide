#!/usr/bin/env python
# coding=utf-8
#from TIDES import *
import h5py
#from mpi4py import MPI
from parameter import *
import sys

'''get kappa(kv,kp),b,w, and get kappa(x)'''
dir=sys.argv[4]
input=sys.argv[1]
output=sys.argv[2]
inputfile=dir+input
Outputfile=dir+output
#################################################################################
#comm = MPI.COMM_WORLD
#size = comm.Get_size()
#rank = comm.Get_rank()

#N=1024
#L=1.2*10**3
#H=L/N
#Kf=2*np.pi/L
#fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
#fnc=np.arange(N/2+1)
#mpi_fn=np.array_split(fn,size)
#mpi_index=np.array_split(np.arange(N),size)

f=h5py.File(inputfile)#'/home/mtx/data/tide/outdata/old_test/0.000den00_Pk_kappa_delta.hdf5')
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
