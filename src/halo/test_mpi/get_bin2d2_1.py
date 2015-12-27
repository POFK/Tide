#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import *
import h5py
from mpi4py import MPI
import sys
#import time
'''get kappa(kv,kp),b,w, and get kappa(x)'''
name=sys.argv[1]
#name='tides00'
#############################creat com.hdf5 of bool############################
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
########################## Load data ############################################
b=np.loadtxt('./result_b')
W=np.loadtxt('./result_W')

g=h5py.File('/home/mtx/data/com.hdf5')
change=g['data'][rank*(1024/size):(rank+1)*(1024/size)]
g.close()
############################################################
x=np.fft.fftfreq(N,1./N)
z=np.zeros_like(x)
KV = ((x**2)[rank*(1024/size):(rank+1)*(1024/size)][:, None, None] +(x**2)[None, :, None] +(z**2)[None, None, :])**(1. / 2.)
KP = ((z**2)[rank*(1024/size):(rank+1)*(1024/size)][:, None, None] +(z**2)[None, :, None] +(x**2)[None, None, :])**(1. / 2.)
################################################################################
bins=10
binlog=np.linspace(0,np.log10(512),bins,endpoint=False)
dbinlog=binlog[2]-binlog[1]
binlog=np.hstack((binlog,binlog[-1]+dbinlog))
bin=10**binlog
bin[0]=0
####################################################################################################
fw=W/b
for i in range(bins):
    for j in range(bins):
        bool1=(bin[j]<=KV)*(KV<bin[j+1])
        bool2=(bin[i]<=KP)*(KP<bin[i+1])
        bool=bool1*bool2
        if i+j==0:
            if rank==0:
                bool[0,0,0]=False
################################################################################
        change[bool]=fw[i,j]
        if rank==0:
            change[0,0,0]=0

g=h5py.File('/home/mtx/data/com.hdf5',mode='w')
g['data'][rank*(1024/size):(rank+1)*(1024/size)]=change
g.close()

####################################################################################################
