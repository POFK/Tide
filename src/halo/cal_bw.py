#!/usr/bin/env python
# coding=utf-8
import numpy as np
b0=np.loadtxt('/home/mtx/data/tide/outdata/tides00/halo/result_b')
b1=np.loadtxt('/home/mtx/data/tide/outdata/tides01/halo/result_b')
b2=np.loadtxt('/home/mtx/data/tide/outdata/tides02/halo/result_b')
b3=np.loadtxt('/home/mtx/data/tide/outdata/tides03/halo/result_b')
b4=np.loadtxt('/home/mtx/data/tide/outdata/tides04/halo/result_b')
b5=np.loadtxt('/home/mtx/data/tide/outdata/tides05/halo/result_b')
w0=np.loadtxt('/home/mtx/data/tide/outdata/tides00/halo/result_W')
w1=np.loadtxt('/home/mtx/data/tide/outdata/tides01/halo/result_W')
w2=np.loadtxt('/home/mtx/data/tide/outdata/tides02/halo/result_W')
w3=np.loadtxt('/home/mtx/data/tide/outdata/tides03/halo/result_W')
w4=np.loadtxt('/home/mtx/data/tide/outdata/tides04/halo/result_W')
w5=np.loadtxt('/home/mtx/data/tide/outdata/tides05/halo/result_W')
b=(b0+b1+b2+b3+b4+b5)/6
for i in range(10):
    for j in range(10):
        if i>6:
            b[i,j]=1
        if j>6:
            b[i,j]=1
w=(w0+w1+w2+w3+w4+w5)/6
np.savetxt('result_b',b)
np.savetxt('result_W',w)
