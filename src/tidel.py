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
        data=np.array(data,dtype=np.float)
        data=data.reshape((1024,1024,1024),order='F')
        return data
N=1024
H=1.2/1024.
kn=np.pi/H
data=Tidels.LoadData(filename='/home/mtx/data/tidels/0.000den00.bin')
delta_k=np.fft.fftn(data)
del data
x=np.arange(1024)
for i in np.arange(1,1024/2+1,dtype=float):
    x[1024-i]=x[i]
window_k=np.sinc(np.pi/N*x[:,None,None])*np.sinc(np.pi/N*x[None,:,None])*np.sinc(np.pi/N*x[None,None,:])
Pk=np.abs(delta_k/window_k)**2
del window_k
#########################################################################
k=(x[:,None,None]**2+x[None,:,None]**2+x[None,None,:]**2)**(1./2.)
kmax=k.max()
kmin=k.min()
x=np.linspace(kmin,kmax,20)
dx=x[1]-x[0]
P=[]
for i in x:
    P.append(Pk[((i-dx/2.)<=k)*(k<(i+dx/2.))].sum()/float(len(Pk[((i-dx/2.)<=k)*(k<(i+dx/2.))])))
P=1.2**3./(1024.**6.)*np.array(P)
plt.plot(x,np.log10(P))
plt.savefig('./ps.png')




