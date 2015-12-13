#!/usr/bin/env python
# coding=utf-8
import h5py
import numpy as np
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wdensgx.hdf5')
g=h5py.File('/home/mtx/data/tide/outdata/0.000den00_wdensgy.hdf5')
delta_gx=f['data'].value
delta_gy=g['data'].value
f.close()
g.close()
gamma1=delta_gx*delta_gx-delta_gy*delta_gy
gamma2=2*delta_gx*delta_gy
