#!/usr/bin/env python
# coding=utf-8
'''To calulate Pk!'''
import fftw3 as fftw
from TIDES import Tide
import numpy as np
#from parameter import *
from subprocess import call
import sys
L=1200
N=1024
Kf=2*np.pi/L
fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
fnc=np.arange(N/2+1)
DIRNAME=sys.argv[1]
#Path='/project/mtx/output/tides10/'
#data=Tide.LoadDataOfhdf5(Path+DIRNAME+'/haloS1.25_Wiener.hdf5')
#delta=Tide.LoadDataOfhdf5('/project/mtx/data/tides10/0.000delta.hdf5')
#========================================
#window_k= (np.sinc(1./N*fn[:,None,None])*np.sinc(1./N*fn[None,:,None])*np.sinc(1./N*fnc[None,None,:]))
def pk(deltax1,deltax2,nthreads=4):
    deltak1=Tide.fft3d(deltax1,nthreads)
    deltak2=Tide.fft3d(deltax2,nthreads)
    Pk=((deltak1.conjugate()*deltak2+deltak2.conjugate()*deltak1)/2.).real
    Pk*=(L**3/N**6)
    return Pk
#========================================
# Pk of wiener wiener
#P=pk(deltax1=data,deltax2=data,nthreads=16)
#SavePath='/project/mtx/output/tides10/'+DIRNAME+'/Pk_wiener.hdf5'
SavePath='/project/mtx/output/tides10/'+DIRNAME+'/haloS1.25_Wiener.hdf5'
#Tide.SaveDataHdf5(P,SavePath)
bin1dPath='/project/mtx/output/tides10/'+DIRNAME+'/wiener_1d.txt'
call('mpirun -hostfile node_hostfile python sep_get_bin1d.py %s %s %s'%('1',SavePath,bin1dPath),shell=True)
# Pk of wiener-delta
#P=pk(deltax1=data,deltax2=delta,nthreads=16)
#P/=window_k**2
#SavePath='/project/mtx/output/tides10/'+DIRNAME+'/Pk_wiener_delta.hdf5'
#Tide.SaveDataHdf5(P,SavePath)
#bin1dPath='/project/mtx/output/tides10/'+DIRNAME+'/Pk_wiener_delta_1d.txt'
#call('mpirun -hostfile node_hostfile python sep_get_bin1d.py %s %s %s'%('1',SavePath,bin1dPath),shell=True)
