#!/usr/bin/env python
# coding=utf-8
import TIDES as td
import numpy as np
import h5py
import struct
name1='/home/mtx/data/tide/0.000uwkappa1.25.bin'
name2='/home/mtx/data/tide/outdata/old_test/0.000den00_wkappa3d_x.hdf5'
#name1='/home/mtx/data/tide/0.000wgam11.25.bin'
#name2='/home/mtx/data/tide/outdata/old_test/0.000den00_wgamma1.hdf5'

def LoadData( filename='/home/mtx/data/tide/0.000den00.bin'):
    '''read bin data'''
    print 'Loading data.................'
    f = open(filename, 'rb')
    data = f.read(1024*4)
    f.close()
    data = struct.unpack('1024f', data)
    data = np.array(data, dtype=np.float16)
    return data

data1=LoadData(filename=name1)
#f=h5py.File('/home/mtx/data/tide/outdata/old_test/0.000den00_wkappa3d_x.hdf5')
f=h5py.File(name2)
data2=np.array(f['data'][:,0,0],dtype=np.float16)
print data1
print data2
print data1-data2

