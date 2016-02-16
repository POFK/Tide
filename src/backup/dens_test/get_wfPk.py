#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import *
import sys
name=sys.argv[1]
Inputfilename1='/home/zhm/'+name+'/0.000den00.bin'
Outputfilename='/home/mtx/data/tide/outdata/'+name+'/'
print Outputfilename
L=1.2*10**3
########################################load data########################################
wfkappa_3dx=Tide.LoadDataOfhdf5('0.000den00_result_wfkappax.hdf5')
delta_x=Tide.LoadData(filename=Inputfilename1)
#######################################save data#########################################
wfPk_delta=1./L**3*Tide.AutoPowerSpectrum(data=delta_x,window=True)
wfPk_kappa=1./L**3*Tide.AutoPowerSpectrum(data=wfkappa_3dx,window=False)
wfPk_delta_kappa=1./L**3*Tide.CrossPowerSpectrum(data1=delta_x,data2=wfkappa_3dx)

Tide.SaveDataHdf5(Pk_kappa,Outputfilename+'0.000den00_wfPk_kappa.hdf5')
Tide.SaveDataHdf5(Pk_delta,Outputfilename+'0.000den00_wfPk_delta.hdf5')
Tide.SaveDataHdf5(Pk_delta_kappa,Outputfilename+'0.000den00_wfPk_delta_kappa.hdf5')

