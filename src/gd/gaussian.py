#!/usr/bin/env python
# coding=utf-8
import numpy as np
import os,sys
from subprocess import call
from TIDES import Tide
import h5py
'''
usage: 
./gaussian.py /project/mtx/output/tides10/halo_0.0048_test_Gau2/0.000den00_s1.25.hdf5 /project/mtx/output/tides10/halo_0.0048_test_Gau2/test_yygau.hdf5
'''

os.chdir(os.path.dirname(sys.argv[0]))
input=sys.argv[1]
output=sys.argv[2]
print 'script dir :',os.path.dirname(sys.argv[0])
print 'Input  file:',input
print 'Output file:',output
input_bin=input[:-4]+'bin'
output_bin=output[:-4]+'bin'
################################################################################
f=h5py.File(input,'r')
data_s=f['data'][...]
f.close()
data_s=data_s.reshape(-1)
data_s.tofile(input_bin,format='f4')
print 'ifort ...'
call('ifort ./gd.f90',shell=True)
print 'gaussian ...'
call('./a.out %s %s'%(input_bin,output_bin),shell=True)
gau=np.fromfile(output_bin,dtype='f4')
gau=gau.reshape(1024,1024,1024)
Tide.SaveDataHdf5(gau,output)
