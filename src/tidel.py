#!/usr/bin/env python
# coding=utf-8
import struct 
import numpy as np
class Tidels():
    @classmethod
    def LoadData(self,filename='/home/mtx/data/tidels/0.000den00.bin'):
        f=open(filename,'rb')
        data=f.read()
        f.close()
        data=struct.unpack('1073741824f',data)
        data=np.reshape(data,(1024,1024,1024),order='F')
        print load data:
        print data.shape
        return data
data=Tidels.LoadData(filename='/home/mtx/data/tidels/0.000den00.bin')
fftd=np.fft.fftn(data)
del data
