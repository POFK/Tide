#!/usr/bin/env python
# coding=utf-8
import struct 
import numpy as np
import matplotlib.pyplot as plt
class Tidels():
    @classmethod
    def LoadData(self,filename='/home/mtx/data/tidels/0.000den00.bin'):
        f=open(filename,'rb')
        data=f.read()
        f.close()
        data=struct.unpack('1073741824f',data)
        data=np.array(data,dtype=np.float16)
        data=data.reshape((1024,1024,1024),order='F')
        return data
N=1024
L=1.2*10**3   #Mpc
H=L/1024.
kf=2*np.pi/L
data=Tidels.LoadData(filename='/home/mtx/data/tidels/0.000den00.bin')
#########################################################################
delta_k=np.fft.fftn(data)
del data
x=np.arange(1024)
for i in np.arange(1,1024/2+1):
    x[1024-i]=x[i]
window_k=np.sinc(np.pi/N*x[:,None,None])*np.sinc(np.pi/N*x[None,:,None])*np.sinc(np.pi/N*x[None,None,:])
Pk=(np.abs(delta_k/window_k)**2)
del window_k
#########################################################################
k=((x[:,None,None]**2+x[None,:,None]**2+x[None,None,:]**2)**(1./2.))
kmax=k.max()
kmin=1
x=np.linspace(np.log10(kmin),np.log10(kmax),20,endpoint=True)
dx=x[1]-x[0]
P=[]
for i in x:
    P.append(Pk[(10**(i-dx/2.)<=k)*(k<10**(i+dx/2.))].sum()/float(len(Pk[(10**(i-dx/2.)<=k)*(k<10**(i+dx/2.))])))
P=L**3./(1024.**6.)*np.array(P)
x=10**x*2*np.pi/L
######### save with no log###############
np.savetxt('PS_data',np.c_[x,P])




