#!/usr/bin/env python
# coding=utf-8
import struct 
from mpi4py import MPI
import numpy as np
import matplotlib.pyplot as plt
####################################################
N=1024
L=1.2*10**3   #Mpc
H=L/1024.

comm = MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()
####################################################
class Tide():
    @classmethod
    def LoadData(self,filename='/home/mtx/data/tide/0.000den00.bin'):
        f=open(filename,'rb')
        data=f.read()
        f.close()
        data=struct.unpack('1073741824f',data)
        data=np.array(data,dtype=np.float16)
        data=data.reshape((1024,1024,1024),order='F')
        return data
    @classmethod
    def GetX(self):
        x=np.arange(1024)
        for i in np.arange(1,1024/2+1):
            x[1024-i]=x[i]
        return x
######################## Load data and Window func#######################
#if rank==0:
data=Tide.LoadData(filename='/home/mtx/data/tide/0.000den00.bin')
x=Tide.GetX()                 #x: 0,1,2,...,512,511,...,2,1
delta_k=np.abs(np.fft.fftn(data))**2
del data
window_k=np.sinc(np.pi/N*x[:,None,None])*np.sinc(np.pi/N*x[None,:,None])*np.sinc(np.pi/N*x[None,None,:])
Pk=delta_k/(window_k**2)
del window_k
del delta_k
#Pk=np.abs(delta_k)**2.
#############################################################################
#Pk = comm.bcast(Pk if rank == 0 else None, root=0)  
kn=(x[:,None,None]**2.+x[None,:,None]**2.+x[None,None,:]**2.)**(1./2.)
kn_max=512
kn_min=1
x=np.linspace(np.log10(kn_min),np.log10(kn_max),20,endpoint=False)
dx=x[1]-x[0]
P=[]
k=[]
Ln=[]
#############################  MPI  ########################################
MPI_Num=20/size
for i in range(rank*MPI_Num,(rank+1)*MPI_Num):
    bool=((10**x[i])<=kn)*(kn<(10**(x[i]+dx)))
    P.append(Pk[bool].sum()/float(len(Pk[bool])))
    k.append(kn[bool].sum()/float(len(kn[bool])))
    Ln.append(len(kn[bool]))
if rank!=0:
    comm.send((k,P,Ln),dest=0)
elif rank==0:
    for r in np.arange(1,size):
        a1,a2,a3=comm.recv(source=r)
        k=k+a1
        P=P+a2
        Ln=Ln+a3
    P=L**3./(1024.**6)*np.array(P)
    k=np.array(k)*2*np.pi/L
######### save data with no log###############
    np.savetxt('PS_data',np.c_[k,P,Ln])
