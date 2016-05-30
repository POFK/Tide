#!/usr/bin/env python
# coding=utf-8
from TIDES import *
from mpi4py import MPI
import sys

comm=MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()
#================================================================================
Input=  sys.argv[1]    #'/home/mtx/data/tide/haloes/0.000halo_0.0024.bin'  # halo

if len(sys.argv)>3:
    Input2=sys.argv[3]  # dark matter
else :
    Input2='/home/zhm/tides10/0.000delta.bin'  # dark matter

Outfile=sys.argv[2]    #'/home/mtx/data/tide/haloes/outdata/halo_0024/'
N=1024
L=1.2*10**3
#L=0.6*10**3
H=L/N
Sigma=1.25
nthreads=2 #fftw threads number
bins=10
#********************************************************************************
Kf=2*np.pi/L
fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
fnc=np.arange(N/2+1)
mpi_fn=np.array_split(fn,size)
mpi_index=np.array_split(np.arange(N),size)
#================================================================================
