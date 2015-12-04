#!/usr/bin/env python
# coding=utf-8
import numpy  as np
from mpi4py import MPI
import time
comm = MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()

x=np.arange(1024)
for i in np.arange(1,1024/2+1):
    x[1024-i]=x[i]

kmin=1
kmax=512
delta=np.log10(kmax)/20.
Ki=rank*delta
count=0
Sk=0
for i in x:
    for j in x:
        for k in x:
            K=np.sqrt(i*i+j*j+k*k)
            if K>10**(Ki) and K<10**(Ki+delta):
                count=count+1
                Sk=K+Sk
Kout=Sk/count
b=np.array([Kout,count])
##########################################################################
if rank!=0:
    comm.send(b,dest=0)
elif rank==0:
    yyy=[]
    yyy.append(b)
    for j in np.arange(1,size):
        time.sleep(0.1)
        b2=comm.recv(source=j)
        yyy.append(b2)
    yyy=np.array(yyy)
    yyy[:,0]=2*np.pi/(1.2*10**3)*yyy[:,0]
    np.savetxt('K_test_withFor',yyy)
