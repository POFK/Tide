#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import *
kx=np.fft.fftfreq(1024,1./1024)
z=np.zeros_like(kx)
Pk=Tide.LoadData('/home/mtx/data/tide/outdata/0.000den00_Pk_delta.hdf5')
kv=np.sqrt(kx[:,None,None]**2+kx[None,:,None]**2+z[None,None,:]**2).reshape(-1)
kp=(z[:,None,None]+z[None,:,None]+kx[None,None,:]).reshape(-1)
np.histogram2d()
