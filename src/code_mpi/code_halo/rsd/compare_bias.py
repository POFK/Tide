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


f=h5py.File(inputfile)  #input bias
bias=f['data'][mpi_index[rank].tolist()]
f.close()
k=((mpi_fn[rank]**2)[:,None,None]+(fn**2)[None,:,None]+(fnc**2)[None,None,:])**(0.5)
kp=(np.zeros_like(mpi_fn[rank]**2)[:,None,None]+np.zeros_like(fn**2)[None,:,None]+(fnc**2)[None,None,:])**(0.5)
mu=kp/k
k=np.array(k,dtype=np.float64)
bins=20
bin=np.linspace(0,np.log10(512),bins,endpoint=False)
dbin=bin[1]-bin[0]

n=[]
b0=[]
b1=[]
b2=[]
b3=[]
kx=[]
for i in range(bins):
    bool=(10**bin[i]<=k)*(k<(10**(bin[i]+dbin)))
    if i==0:
        if rank==0:
            bool[0,0]=False
            bias[0,0]=0
    n.append(len(k[bool]))
    b0.append((bias[bool]).sum())
    b1.append((bias[bool]*mu[bool]).sum())
    b2.append((bias[bool]*(3*mu[bool]-2+6./4.*(mu[bool]-1)**2)).sum())
    b3.append((bias[bool]*(1+6*(mu[bool]-1)+30*((mu[bool]-1)/2.)**2+20*((mu[bool]-1.)/2.)**3)).sum())
    kx.append(k[bool].sum())

n=np.array(n)
kx=np.array(kx)
b0=np.array(b0)
b1=np.array(b1)
b2=np.array(b2)
b3=np.array(b3)

if rank==0:
    b1=0


n_1=comm.reduce(n,root=0)
kx_1=comm.reduce(kx,root=0)
b0_1=comm.reduce(b0,root=0)
b1_1=comm.reduce(b1,root=0)
b2_1=comm.reduce(b2,root=0)
b3_1=comm.reduce(b3,root=0)
if rank==0:
    n=n_1
    kx=kx_1*Kf/n
    b0=b0_1/n
    b1=b1_1/n
    b2=b2_1/n
    b3=b3_1/n
    np.savetxt(Outputfile,np.c_[kx,b0,b1,b2,b3,n])#'/home/mtx/data/tide/outdata/old_test/PS_Pkkd',np.c_[kx,Pk,n])
