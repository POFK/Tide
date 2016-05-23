#!/usr/bin/env python
# coding=utf-8
from parameter import *
if not os.path.exists(ResultDir):
    os.mkdir(ResultDir)
bias=np.loadtxt(dir+'result_b')
wiener=np.loadtxt(dir+'result_W')
#bias[7:,:]=1.
#bias[:,7:]=1.
np.savetxt(ResultDir+'result_b',bias)
np.savetxt(ResultDir+'result_W',wiener)
