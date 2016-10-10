#!/usr/bin/env python
# coding=utf-8
'''  combine 2 mass bins '''
from parameter import *
from subprocess import call
if Combine_wden:
    PathOut=Path_comWden_out
    if not os.path.exists(PathOut):
        os.mkdir(PathOut)
    path=[]
    for i in np.arange(NUM_massbin):
        path.append(Path_ComWden[i])
    #========= load wdeng ===================
    wg1a = np.array( Tide.LoadDataOfhdf5(path[0] + 'halo_wdeng1.hdf5') , dtype = np.float64)
    wg1b = np.array( Tide.LoadDataOfhdf5(path[1] + 'halo_wdeng1.hdf5') , dtype = np.float64)
    wg2a = np.array( Tide.LoadDataOfhdf5(path[0] + 'halo_wdeng2.hdf5') , dtype = np.float64)
    wg2b = np.array( Tide.LoadDataOfhdf5(path[1] + 'halo_wdeng2.hdf5') , dtype = np.float64)
    wg3a = np.array( Tide.LoadDataOfhdf5(path[0] + 'halo_wdeng3.hdf5') , dtype = np.float64)
    wg3b = np.array( Tide.LoadDataOfhdf5(path[1] + 'halo_wdeng3.hdf5') , dtype = np.float64)
    #=========  cal gamma  ==================
    gm = wg1a * wg1b - wg2a * wg2b
    Tide.SaveDataHdf5(gm,PathOut+'halo_gm1.hdf5')
    gm = wg1a * wg2b + wg1b * wg2a
    Tide.SaveDataHdf5(gm,PathOut+'halo_gm2.hdf5')
    gm = wg1a * wg3b + wg1b * wg3a
    Tide.SaveDataHdf5(gm,PathOut+'halo_gmx.hdf5')
    gm = wg2a * wg3b + wg2b * wg3a
    Tide.SaveDataHdf5(gm,PathOut+'halo_gmy.hdf5')
    gm = (2. * wg3a * wg3b - wg1a * wg1b - wg2a * wg2b)/3.
    Tide.SaveDataHdf5(gm,PathOut+'halo_gmz.hdf5')
    

