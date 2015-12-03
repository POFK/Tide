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
kn=((x[:,None,None]**2.+x[None,:,None]**2.+x[None,None,:]**2.)**(1./2.))
kn_max=512.
kn_min=1.
x=np.linspace(np.log10(kn_min),np.log10(kn_max),20,endpoint=False)
dx=x[1]-x[0]
P=[]
k=[]
i=x[rank]#+0.5*dx
#bool=(10**(i-dx/2.)<=kn)*(kn<=10**(i+dx/2.)) # method 1
bool=((10**x[rank])<=kn)*(kn<(10**(x[rank]+dx)))

a1=kn[bool].sum()
a2=len(kn[bool])
a=a1/a2
b=[2*np.pi/1.2/10**3*a,a2]
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
