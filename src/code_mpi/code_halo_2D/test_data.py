#!/usr/bin/env python
# coding=utf-8
file1='/project/mtx/output/tides10/halo_0.0048/'
file2='/project/mtx/output/tides11/halo_0.0048/'
file3='/project/mtx/output/tides12/halo_0.0048/'
file4='/project/mtx/output/tides13/halo_0.0048/'
file5='/project/mtx/output/tides14/halo_0.0048/'
file6='/project/mtx/output/tides15/halo_0.0048/'
import numpy as np
import matplotlib.pyplot as plt
def f(file=''):
    dd=np.loadtxt(file+'PS_DD')
    dk=np.loadtxt(file+'PS_DK')
    kk=np.loadtxt(file+'PS_KK')
    r=dk[:,1]/np.sqrt(dd[:,1]*kk[:,1])
    plt.semilogx(dd[:,0],r,label=file[-15:-13])

f(file1)
f(file2)
f(file3)
f(file4)
f(file5)
f(file6)
plt.legend()
plt.show()

