#!/usr/bin/env python
# coding=utf-8
'''  combine 2 mass bins: kappa3D '''
from parameter import *
path1=Path_ComWkappa[0]
path2=Path_ComWkappa[1]
pathCro=Path_ComWkappa[2]
print 'input:'
print path1,path2,pathCro
print 'output:'
print Path_comWkappa_out
if not os.path.exists(Path_comWkappa_out):
    os.mkdir(Path_comWkappa_out)
#========================================
kappa_a=Tide.LoadDataOfhdf5(path1+'halo_wfkappa_3d.hdf5')
kappa_b=Tide.LoadDataOfhdf5(path2+'halo_wfkappa_3d.hdf5')
kappa_cro=Tide.LoadDataOfhdf5(pathCro+'halo_wfkappa_3d.hdf5')
#========================================
kappa=kappa_a+kappa_b+2*kappa_cro
Tide.SaveDataHdf5(kappa,Path_comWkappa_out+'halo_wfkappa_3d.hdf5')
