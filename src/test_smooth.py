#!/usr/bin/env python
# coding=utf-8
import TIDES as td
import numpy as np
import h5py
data1=td.Tide.LoadData(filename='/home/mtx/data/tide/0.000dens1.25.bin')
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_smooth.hdf5')
data2=np.array(f['data'].value,dtype=np.float16)
print np.abs((data1-data2).sum())
