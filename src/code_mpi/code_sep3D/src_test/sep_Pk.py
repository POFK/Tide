#!/usr/bin/env python
# coding=utf-8
'''To calulate Pk!'''
import fftw3 as fftw
from parameter import *
from subprocess import call
Path='/project/mtx/output/tides10/'
#data=Tide.LoadDataOfhdf5(Path+DIRNAME+'/haloS1.25.hdf5')
data=Tide.LoadDataOfhdf5(Path+DIRNAME+'/haloS0.00.hdf5')
def pk(deltax1,deltax2,nthreads=4):
    deltak1=Tide.fft3d(deltax1,nthreads)
    deltak2=Tide.fft3d(deltax2,nthreads)
    Pk=((deltak1.conjugate()*deltak2+deltak2.conjugate()*deltak1)/2.).real
    Pk*=(L**3/N**6)
    return Pk
P=pk(deltax1=data,deltax2=data,nthreads=16)
SavePath='/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/tides10/'+DIRNAME+'/Pk_smooth_wiener.hdf5'
Tide.SaveDataHdf5(P,SavePath)
bin1dPath='/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/tides10/'+DIRNAME+'/Pk_smooth_wiener_1d.txt'
call('mpirun -hostfile node_hostfile python sep_get_bin1d.py %s %s %s'%(DirNum,SavePath,bin1dPath),shell=True)
