#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import Tide
#from parameter import *

PathDirA='/project/mtx/output/tides10/massbin2_0.0003_m1/'
PathDirB='/project/mtx/output/tides10/massbin2_0.0003_m2/'
PathOut ='/project/mtx/output/tides10/massbin2_0.0003_combine_cross/'
#========= load wdeng ===================
print PathDirA+'wdeng1.hdf5'
wg1a = np.array( Tide.LoadDataOfhdf5(PathDirA + 'halo_wdeng1.hdf5') , dtype = np.float64)
wg1b = np.array( Tide.LoadDataOfhdf5(PathDirB + 'halo_wdeng1.hdf5') , dtype = np.float64)
wg2a = np.array( Tide.LoadDataOfhdf5(PathDirA + 'halo_wdeng2.hdf5') , dtype = np.float64)
wg2b = np.array( Tide.LoadDataOfhdf5(PathDirB + 'halo_wdeng2.hdf5') , dtype = np.float64)
wg3a = np.array( Tide.LoadDataOfhdf5(PathDirA + 'halo_wdeng3.hdf5') , dtype = np.float64)
wg3b = np.array( Tide.LoadDataOfhdf5(PathDirB + 'halo_wdeng3.hdf5') , dtype = np.float64)
#=========  cal gamma  ==================
gm = wg1a * wg1b - wg2a * wg2b
Tide.SaveDataHdf5(gm,PathOut+'gm1.hdf5')
gm = wg1a * wg2b + wg1b * wg2a
Tide.SaveDataHdf5(gm,PathOut+'gm2.hdf5')
gm = wg1a * wg3b + wg1b * wg3a
Tide.SaveDataHdf5(gm,PathOut+'gmx.hdf5')
gm = wg2a * wg3b + wg2b * wg3a
Tide.SaveDataHdf5(gm,PathOut+'gmy.hdf5')
gm = (2. * wg3a * wg3b - wg1a * wg1b - wg2a * wg2b)/3.
Tide.SaveDataHdf5(gm,PathOut+'gmz.hdf5')
