#!/usr/bin/env python
# coding=utf-8

#!/usr/bin/env python
# coding=utf-8
import struct 
import numpy as np
import matplotlib.pyplot as plt
####################################################
N=1024
L=1.2*10**3   #Mpc
H=L/1024.
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
#########################################################################
data=Tide.LoadData(filename='/home/mtx/data/tide/0.000den00.bin')
delta_k=np.fft.fftn(data)
data2=np.fft.ifftn(delta_k).real
print np.abs(data2-data).sum()
