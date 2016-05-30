#!/usr/bin/env python
# coding=utf-8
from parameter import *
from subprocess import call
call('mpirun -hostfile node_hostfile python sep_get_bin1d.py %s %s %s'%(DirNum,dir+'Wiener.hdf5',dir+'wiener.txt'),shell=True)
