#!/usr/bin/env python
# coding=utf-8
import numpy as np
import h5py
###############load log(delta x)#######################
f = h5py.File('/home/fileF/projects/python/test/ICA/data/21cm_freq100_256.hdf5')
#data = np.array(f['data'].value,dtype=np.float16)
data=f['map'].value
print np.dtype(data)
f.close()
############### partial x #############################
