#!/usr/bin/env python
# coding=utf-8
import numpy as np
import h5py
###############load log(delta x)#######################
f = h5py.File('0.000den00_smoothg.hdf5')
data = np.array(f['data'].value,dtype=np.float16)
print np.dtype(data)
f.close()
############### partial x #############################
