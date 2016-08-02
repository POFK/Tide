#!/usr/bin/env python
# coding=utf-8
from sep_Pk import *

window_k= (np.sinc(1./N*fn[:,None,None])*np.sinc(1./N*fn[None,:,None])*np.sinc(1./N*fnc[None,None,:]))
for i in np.arange(RunPk0Num):
    print 'Path In :',Path_Pk0_Input[i][0],Path_Pk0_Input[i][2]
    print 'Path out:',Path_Pk0_Output[i]
    IsHalo1=int(Path_Pk0_Input[i][1])
    IsHalo2=int(Path_Pk0_Input[i][3])
    delta1=Tide.LoadDataOfhdf5(Path_Pk0_Input[i][0])
    if IsHalo1:
        sum=delta1.sum()
        delta1*=(N**3/sum)
    delta2=Tide.LoadDataOfhdf5(Path_Pk0_Input[i][2])
    if IsHalo2:
        sum=delta2.sum()
        delta2*=(N**3/sum)
    deltak1=Tide.fft3d(delta1,nthreads)
    deltak2=Tide.fft3d(delta2,nthreads)
    if Path_Pk0_Input[i][4] == 'ngp':
        deltak1/=window_k
    elif Path_Pk0_Input[i][4] == 'cic':
        deltak1/=window_k**2
    if Path_Pk0_Input[i][5] == 'ngp':
        deltak2/=window_k
    elif Path_Pk0_Input[i][5] == 'cic':
        deltak2/=window_k**2
    result_pk=((deltak1.conjugate()*deltak2+deltak2.conjugate()*deltak1)/2.).real
    result_pk*=(L**3/N**6)
    Tide.SaveDataHdf5(result_pk,Path_Pk0_Output[i])
