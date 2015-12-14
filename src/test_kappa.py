#!/usr/bin/env python
# coding=utf-8
import TIDES as td
import numpy as np
import h5py
data1=td.Tide.LoadData(filename='/home/mtx/data/tide/0.000wfkappa1.25.bin')
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wkappa3d.hdf5')
#data1=td.Tide.LoadData(filename='/home/mtx/data/tide/0.000wgam11.25.bin')
#f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wgamma1.hdf5')
#data1=td.Tide.LoadData(filename='/home/mtx/data/tide/0.000wdengx1.25.bin')
#f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wdensgx.hdf5')

data2=np.array(f['data'].value,dtype=np.float16)
print 'dens\n',data1[500:530,500:530,500:530],'\n\n'
print 'my output:\n',data2[500:530,500:530,500:530],'\n\n'
