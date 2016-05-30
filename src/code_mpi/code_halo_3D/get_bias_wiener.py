#!/usr/bin/env python
# coding=utf-8
import sys
import numpy as np
m=7
dir=sys.argv[1:]
n=len(dir)
bias=np.loadtxt(dir[0]+'result_b')
W=np.loadtxt(dir[0]+'result_W')

for i in dir:
    bias+=np.loadtxt(i+'result_b')
    W+=np.loadtxt(i+'result_W')
bias/=n
W/=n
bias[m:,:]=1.
bias[:,m:]=1.
#W[m:,:]=1.
#W[:,m:]=1.
print 'bias',bias
print 'wiener',W
np.savetxt('result_b',bias)
np.savetxt('result_W',W)
