#!/usr/bin/env python
# coding=utf-8
from parameter import *
from subprocess import call
call('mpirun -hostfile node_hostfile python sep_get_bin1d.py %s %s %s'%(DirNum,PathBin1dInput2,PathBin1dOutput2+'noWf.txt'),shell=True)
call('mpirun -hostfile node_hostfile python sep_get_bin1d.py %s %s %s'%(DirNum,PathBin1dInput3,PathBin1dOutput3+'noWf.txt'),shell=True)
call('mpirun -hostfile node_hostfile python sep_get_bin1d.py %s %s %s'%(DirNum,PathBin1dInput5,PathBin1dOutput5+'noWf.txt'),shell=True)
