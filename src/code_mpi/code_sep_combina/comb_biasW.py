#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import Tide
b1=0.59
b2=0.43
b3=0.39
b4=0.36
path1='/project/mtx/output/tides10/highmass1_0.0012_1.25_NoGau/'
path2='/project/mtx/output/tides10/highmass2_0.0012_1.25_NoGau/'
path3='/project/mtx/output/tides10/highmass3_0.0012_1.25_NoGau/'
path4='/project/mtx/output/tides10/highmass4_0.0012_1.25_NoGau/'
data1=Tide.LoadDataOfhdf5(path1+'kappa3dx.hdf5')
data2=Tide.LoadDataOfhdf5(path2+'kappa3dx.hdf5')
data3=Tide.LoadDataOfhdf5(path3+'kappa3dx.hdf5')
data4=Tide.LoadDataOfhdf5(path4+'kappa3dx.hdf5')
datak1=Tide.fft3d(data1,16)
datak2=Tide.fft3d(data2,16)
datak3=Tide.fft3d(data3,16)
datak4=Tide.fft3d(data4,16)
kappak=(b1**2*datak1+b2**2*datak2+b3**2*datak3+b4**2*datak4)/(b1**2+b2**2+b3**2+b4**2)
kappax=Tide.ifft3d(kappak,16)
kappax/=1024.**3
Tide.SaveDataHdf5(kappax,'/project/mtx/output/tides10/combina_bias_4bin_kspace/halo_kappax_2D.hdf5')
