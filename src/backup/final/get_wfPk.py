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
wfkappa_3dx=Tide.LoadDataOfhdf5(Outputfilename+'0.000den00_result_wfkappax.hdf5')
delta_x=Tide.LoadData(filename=Inputfilename1)
#######################################save data#########################################
wfPk_delta=L**3/N**6*Tide.AutoPowerSpectrum(data=delta_x,window=True)
wfPk_delta[0,0,0]=0
wfPk_kappa=L**3/N**6*Tide.AutoPowerSpectrum(data=wfkappa_3dx,window=False)
wfPk_kappa[0,0,0]=0
wfPk_delta_kappa=L**3/N**6*Tide.CrossPowerSpectrum(data1=delta_x,data2=wfkappa_3dx)
wfPk_delta_kappa[0,0,0]=0

Tide.SaveDataHdf5(wfPk_kappa,Outputfilename+'0.000den00_wfPk_kappa.hdf5')
Tide.SaveDataHdf5(wfPk_delta,Outputfilename+'0.000den00_wfPk_delta.hdf5')
Tide.SaveDataHdf5(wfPk_delta_kappa,Outputfilename+'0.000den00_wfPk_delta_kappa.hdf5')
