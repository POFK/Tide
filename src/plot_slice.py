#!/usr/bin/env python
# coding=utf-8
from TIDES import Tide
import numpy as np
import matplotlib.pyplot as plt
import h5py 
import sys
import os
filename=sys.argv[1]
dir=os.getcwd()
f=h5py.File(dir+'/'+filename,'r')
#data=Tide.LoadData('Gau.bin')
data1=f['data'][0,:60,:60]
plt.pcolor(data1,vmin=data1.min(),vmax=data1.max())
plt.colorbar()
plt.savefig(filename+'slice_y_z.png')
plt.clf()
data2=f['data'][:60,0,:60]
plt.pcolor(data2,vmin=data2.min(),vmax=data2.max())
plt.colorbar()
plt.savefig(filename+'slice_x_z.png')
plt.clf()
data3=f['data'][:60,:60,0]
plt.pcolor(data3,vmin=data3.min(),vmax=data3.max())
plt.colorbar()
plt.savefig(filename+'slice_x_y.png')
plt.clf()
f.close()

