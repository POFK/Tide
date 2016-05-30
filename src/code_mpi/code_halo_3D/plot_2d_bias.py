#!/usr/bin/env python
# coding=utf-8
from subprocess import call

f1='/project/mtx/output/tides10/halo_0.0048/'
f2='/project/mtx/output/tides11/halo_0.0048/'
f3='/project/mtx/output/tides12/halo_0.0048/'
f4='/project/mtx/output/tides13/halo_0.0048/'
f5='/project/mtx/output/tides14/halo_0.0048/'
f6='/project/mtx/output/tides15/halo_0.0048/'

################################################################################
call('python get_bias_wiener.py %s %s %s %s %s %s '%(f1,f2,f3,f4,f5,f6),shell=True)

