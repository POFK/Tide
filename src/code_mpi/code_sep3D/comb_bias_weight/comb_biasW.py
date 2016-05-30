#!/usr/bin/env python
# coding=utf-8
'''
combine halo field with bias weight
'''
import numpy as np
from TIDES import Tide
b1=0.59
b2=0.43
b3=0.39
b4=0.36
path1='/project/mtx/data/tides10/0.000halo_0.0012.hdf5'
path2='/project/mtx/data/tides10/highmass2_0.0012.hdf5'
path3='/project/mtx/data/tides10/highmass3_0.0012.hdf5'
path4='/project/mtx/data/tides10/highmass4_0.0012.hdf5'
data1=Tide.LoadDataOfhdf5(path1)
data2=Tide.LoadDataOfhdf5(path2)
data3=Tide.LoadDataOfhdf5(path3)
data4=Tide.LoadDataOfhdf5(path4)
#datak1=Tide.fft3d(data1,16)
#datak2=Tide.fft3d(data2,16)
#datak3=Tide.fft3d(data3,16)
#datak4=Tide.fft3d(data4,16)
data=(b1**2*data1+b2**2*data2+b3**2*data3+b4**2*data4)/(b1**2+b2**2+b3**2+b4**2)
Tide.SaveDataHdf5(data,'/project/mtx/data/tides10/halo_combina_bias_4bin.hdf5')
