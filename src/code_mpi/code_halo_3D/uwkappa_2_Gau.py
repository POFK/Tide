#!/usr/bin/env python
# coding=utf-8
from subprocess import call
import sys
Outfile=sys.argv[2]
call('python /home/mtx/github/Tide/src/code_mpi/code_halo/gd/gaussian.py %s %s'%(Outfile+'0.000den00_s1.25.hdf5',Outfile+'Gau.hdf5'),shell=True)
