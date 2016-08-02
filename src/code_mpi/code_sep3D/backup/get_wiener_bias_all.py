#!/usr/bin/env python
# coding=utf-8
import sys
import numpy as np
from parameter import *
if not os.path.exists(ResultDir):
    os.mkdir(ResultDir)
m=7
n=6
bias=np.zeros((10,10))
W=np.zeros((10,10),dtype=np.float64)
for i in [10,11,12,13,14,15]:
    bias+=np.loadtxt('/project/mtx/output/tides'+str(i)+'/'+DIRNAME+'/result_b')
    W+=np.loadtxt('/project/mtx/output/tides'+str(i)+'/'+DIRNAME+'/result_W')
bias/=n
W/=n
bias[m:,:]=1.
bias[:,m:]=1.
#print 'bias',bias
#print 'wiener',W
np.savetxt(ResultDir+'result_b',bias)
np.savetxt(ResultDir+'result_W',W)
