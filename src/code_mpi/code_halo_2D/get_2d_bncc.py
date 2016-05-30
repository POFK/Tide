#!/usr/bin/env python
# coding=utf-8
import sys
import numpy as np
m=7
dir=sys.argv[1:]
n=len(dir)
bias=np.zeros_like(np.loadtxt(dir[0]+'result_b'))
W=np.zeros_like(np.loadtxt(dir[0]+'result_W'))
Pn=np.zeros_like(np.loadtxt(dir[0]+'result_Pn'))
nn=np.loadtxt(dir[0]+'result_n')
CC=np.zeros_like(np.loadtxt(dir[0]+'result_CC'))

for i in dir:
    bias+=np.loadtxt(i+'result_b')
    W+=np.loadtxt(i+'result_W')
    CC+=np.loadtxt(i+'result_CC')
    Pn+=np.loadtxt(i+'result_Pn')


bias/=n
W/=n
Pn/=n
CC/=n
Pn/=nn
np.savetxt('result_b',bias)
np.savetxt('result_W',W)
np.savetxt('result_CC',CC)
np.savetxt('result_Pn',Pn)
