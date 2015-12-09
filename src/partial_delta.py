#!/usr/bin/env python
# coding=utf-8
import numpy as np
import h5py
###############load log(delta x)#######################
f = h5py.File('/home/mtx/data/tide/outdata/0.000den00_smoothg.hdf5')
data =np.array( f['data'].value,dtype=np.float16)
print data[0,0,0].dtype
f.close()
############### partial x #############################
