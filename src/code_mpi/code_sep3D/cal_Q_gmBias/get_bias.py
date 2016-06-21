#!/usr/bin/env python
# coding=utf-8
import sys
import numpy as np
import matplotlib.pyplot as plt
bias_cut=9
NUM=sys.argv[1]
DIR=sys.argv[2]
PATH='/project/mtx/output/'+NUM+'/'+DIR+'/'
print PATH
Pdh=np.loadtxt(PATH+'Pk_DH')
Pdd=np.loadtxt(PATH+'Pk_DD')
n=Pdh[:,2]
bias=Pdh[:,1]/Pdd[:,1]
b=(bias*n)[:bias_cut].sum()/n[:bias_cut].sum()
print b
plt.semilogx(Pdh[:,0],bias,'.-')
plt.axhline(y=b,linestyle='-.')
plt.text(Pdh[8,0],b,'$b=%.6f$'%b)
plt.show()
