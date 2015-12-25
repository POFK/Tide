#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import *
import sys
name=sys.argv[1]
Inputfilename='/home/zhm/'+name+'/0.000den00.bin'
Outputfilename='/home/mtx/data/tide/outdata/'+name+'/'
print Inputfilename
print Outputfilename
########################################load data########################################
delta_x=Tide.LoadData(filename=Inputfilename)
deltag=Tide.Smooth(data=delta_x,log=True)
delta_gx,delta_gy=Tide.DeltagW(deltag)
del deltag
gamma1,gamma2=Tide.CalGamma(delta_gx,delta_gy)
del delta_gx
del delta_gy
kappa_3dx=Tide.CalKappa(gamma1,gamma2)
del gamma1
del gamma2
#######################################save data#########################################
Tide.SaveDataHdf5(kappa_3dx,Outputfilename+'0.000den00_kappa3dx.hdf5')
Pk_delta=Tide.AutoPowerSpectrum(data=delta_x)
Pk_kappa=Tide.AutoPowerSpectrum(data=kappa_3dx)
Pk_delta_kappa=Tide.CrossPowerSpectrum(data1=delta_x,data2=kappa_3dx)

Tide.SaveDataHdf5(Pk_kappa,Outputfilename+'0.000den00_Pk_kappa.hdf5')
Tide.SaveDataHdf5(Pk_delta,Outputfilename+'0.000den00_Pk_delta.hdf5')
Tide.SaveDataHdf5(Pk_delta_kappa,Outputfilename+'0.000den00_Pk_delta_kappa.hdf5')

