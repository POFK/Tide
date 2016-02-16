#!/usr/bin/env python
# coding=utf-8

#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import *
import h5py
from mpi4py import MPI
'''get kappa(kv,kp),b,w, and get kappa(x)'''
N=1024
L=1.2*10**3
################################################################################
f=h5py.File('/home/mtx/data/tide/outdata/0.000den00_Pk_delta.hdf5')
Pk_d=f['data'].value
Pk_d=np.array(Pk_d,dtype=np.float)
f.close()
##########################################################
x=np.fft.fftfreq(N,1./N)
z=np.zeros_like(x)
KV = ((x**2)[:, None, None] +(x**2)[None, :, None] +(z**2)[None, None, :])**(1. / 2.)
KP = ((z**2)[:, None, None] +(z**2)[None, :, None] +(x**2)[None, None, :])**(1. / 2.)
bins=10
binlog=np.linspace(0,np.log10(512),bins,endpoint=False)
dbinlog=binlog[2]-binlog[1]
binlog=np.hstack((binlog,binlog[-1]+dbinlog))
bin=10**binlog
bin[0]=0
n=np.ones((bins,bins))
Pk=np.ones((bins,bins))
for i in range(10): 
    for j in range(10):
        bool1=(bin[j]<=KV)*(KV<bin[j+1])
        bool2=(bin[i]<=KP)*(KP<bin[i+1])
        bool=bool1*bool2
        if i+j==0:
            bool[0,0]=False
        Pk[i,j]=Pk_d[bool].sum()
        n[i,j]=len(Pk_d[bool])
np.savetxt('test_n',n)
np.savetxt('test_Pkd',Pk/n)

