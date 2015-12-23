#!/usr/bin/env python
# coding=utf-8
import TIDES as td
import numpy as np
import h5py
data1=td.Tide.LoadData(filename='/home/mtx/data/tide/0.000uwkappa1.25.bin')
#f=h5py.File('/home/mtx/data/tide/outdata/old_test/0.000den00_wkappa3d_x.hdf5')
f=h5py.File('/home/mtx/github/Tide/src/0.000den00_result_kappa.hdf5')

data2=np.array(f['data'].value,dtype=np.float16)
print 'dens\n',data1[500:530,500:530,500:530],'\n\n'
print 'my output:\n',data2[500:530,500:530,500:530],'\n\n'
