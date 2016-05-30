#!/usr/bin/env python
# coding=utf-8
import numpy as np
from parameter import *

data=None
f=h5py.File(PathGammainput+'wdeng1.hdf5','r')
wg1=f['data'][mpi_index[rank].tolist()]
f.close()
f=h5py.File(PathGammainput+'wdeng2.hdf5','r')
wg2=f['data'][mpi_index[rank].tolist()]
f.close()
f=h5py.File(PathGammainput+'wdeng3.hdf5','r')
wg3=f['data'][mpi_index[rank].tolist()]
f.close()
wg1=np.array(wg1,dtype=np.float64)
wg2=np.array(wg2,dtype=np.float64)
wg3=np.array(wg3,dtype=np.float64)
################################################################################
if rank==0:
    data=np.empty((N,N,N),dtype=np.float64)
#=gamma1=============
gm=wg1*wg1-wg2*wg2
comm.Gather(gm,data,root=0)
if rank==0:
    Tide.SaveDataHdf5(data,PathGammaoutput+'gm1.hdf5')
#=gamma2=============
gm=2*wg1*wg2
comm.Gather(gm,data,root=0)
if rank==0:
    Tide.SaveDataHdf5(data,PathGammaoutput+'gm2.hdf5')
#=gamma1=============
gm=2*wg1*wg3
comm.Gather(gm,data,root=0)
if rank==0:
    Tide.SaveDataHdf5(data,PathGammaoutput+'gmx.hdf5')
#=gamma1=============
gm=2*wg2*wg3
comm.Gather(gm,data,root=0)
if rank==0:
    Tide.SaveDataHdf5(data,PathGammaoutput+'gmy.hdf5')
#=gamma1=============
gm=(2*wg3*wg3-wg1*wg1-wg2*wg2)/3
comm.Gather(gm,data,root=0)
if rank==0:
    Tide.SaveDataHdf5(data,PathGammaoutput+'gmz.hdf5')
