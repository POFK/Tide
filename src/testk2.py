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
            K=np.sqrt(i**2+j**2+k**2)
            if K>10**(Ki-delta/2) and K<10**(Ki+delta/2):
                count++
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
    np.savetxt('K_test',np.array(yyy))
