#!/usr/bin/env python
# coding=utf-8
from parameter import *
from subprocess import call
call('mpirun -hostfile node_hostfile python sep_get_bin1d.py %s %s %s'%(DirNum,PathBin1dInput1,PathBin1dOutput1),shell=True)
call('mpirun -hostfile node_hostfile python sep_get_bin1d.py %s %s %s'%(DirNum,PathBin1dInput4,PathBin1dOutput4),shell=True)
call('mpirun -hostfile node_hostfile python sep_get_bin1d.py %s %s %s'%(DirNum,PathBin1dInput6,PathBin1dOutput6),shell=True)
