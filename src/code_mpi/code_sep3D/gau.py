#!/usr/bin/env python
# coding=utf-8
from parameter import *
from subprocess import call
import sys
if Gaussian:
    print '='*20+'Gaussian'+'='*20
    input_smooth=PathSoutput+'.hdf5'
    output_gau=PathGwinput
    call('python /home/mtx/github/Tide/src/gd/gaussian.py %s %s'%(input_smooth,output_gau),shell=True)
