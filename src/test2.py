#!/usr/bin/env python
# coding=utf-8
import TIDES as ti
import numpy as np
L=1.2*10**3
N=1024.
#x=ti.Tide.GetX()
x=np.fft.fftfreq(1024,1./1024.)
k=np.sqrt(x[:,None,None]**2+x[None,:,None]**2+x[0:513][None,None,:]**2)
data=ti.Tide.LoadData()
dataK=np.fft.rfftn(data)
print k.shape
print dataK.shape
del data
out=L**3/(N**6)*np.abs(dataK[k==1])**2
print out
print out.sum()/6
#out=L**3/(N**6)*(PK1**2+PK2**2+PK3**2+PK4**2+PK5**2+PK6**2)/6.
#s=np.array(out,PK1[0],PK2[0],PK3[0],PK4[0],PK5[0],PK6[0])
#s=np.array(out)    #2
np.savetxt('testFirstBin2.txt',out)
