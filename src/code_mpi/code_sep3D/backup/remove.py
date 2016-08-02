#!/usr/bin/env python
# coding=utf-8
from parameter import *
from subprocess import call
call('ls %shalo_gm*.hdf5'%dir,shell=True)
call('rm %shalo_gm*.hdf5'%dir,shell=True)
call('ls %shalo_wdeng*.hdf5'%dir,shell=True)
call('rm %shalo_wdeng*.hdf5'%dir,shell=True)
#call('ls %s.hdf5'%PathSoutput,shell=True)
#call('rm %s.hdf5'%PathSoutput,shell=True)
call('rm %shaloGau.bin'%dir,shell=True)
call('rm %s.bin'%PathSoutput,shell=True)
