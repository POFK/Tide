#!/usr/bin/env python
# coding=utf-8
import numpy as np
from parameter import *

data=None
f=h5py.File('/project/mtx/output/tides10/highmass3_0.0012_1.25_NoGau/'+'halo_wdeng1.hdf5','r')
high1_wg1=f['data'][mpi_index[rank].tolist()]
f.close()
f=h5py.File('/project/mtx/output/tides10/highmass3_0.0012_1.25_NoGau/'+'halo_wdeng2.hdf5','r')
high1_wg2=f['data'][mpi_index[rank].tolist()]
f.close()
f=h5py.File('/project/mtx/output/tides10/highmass4_0.0012_1.25_NoGau/'+'halo_wdeng1.hdf5','r')
high2_wg1=f['data'][mpi_index[rank].tolist()]
f.close()
f=h5py.File('/project/mtx/output/tides10/highmass4_0.0012_1.25_NoGau/'+'halo_wdeng2.hdf5','r')
high2_wg2=f['data'][mpi_index[rank].tolist()]
f.close()
################################################################################
if rank==0:
    data=np.empty((N,N,N),dtype=np.float64)
#=gamma1=============
gm=high1_wg1*high2_wg1-high1_wg2*high2_wg2
comm.Gather(gm,data,root=0)
if rank==0:
    Tide.SaveDataHdf5(data,PathGammaoutput+'gm1.hdf5')
#=gamma2=============
gm=high1_wg1*high2_wg2+high2_wg1*high1_wg2
comm.Gather(gm,data,root=0)
if rank==0:
    Tide.SaveDataHdf5(data,PathGammaoutput+'gm2.hdf5')
##=gamma1=============
#gm=2*wg1*wg3
#comm.Gather(gm,data,root=0)
#if rank==0:
#    Tide.SaveDataHdf5(data,PathGammaoutput+'gmx.hdf5')
##=gamma1=============
#gm=2*wg2*wg3
#comm.Gather(gm,data,root=0)
#if rank==0:
#    Tide.SaveDataHdf5(data,PathGammaoutput+'gmy.hdf5')
##=gamma1=============
#gm=(2*wg3*wg3-wg1*wg1-wg2*wg2)/3
#comm.Gather(gm,data,root=0)
#if rank==0:
#    Tide.SaveDataHdf5(data,PathGammaoutput+'gmz.hdf5')
