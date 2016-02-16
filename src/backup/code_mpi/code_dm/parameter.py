#!/usr/bin/env python
# coding=utf-8
from TIDES import *
from mpi4py import MPI

comm=MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()



#================================================================================
Input='/home/mtx/data/tide/0.000den00.bin'
Outfile='/home/mtx/data/tide/outdata/test/'
N=1024
L=1.2*10**3
H=L/N
Sigma=1.25
nthreads=16   #fftw threads number
bins=10

#********************************************************************************


Kf=2*np.pi/L
fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
fnc=np.arange(N/2+1)
mpi_fn=np.array_split(fn,size)
mpi_index=np.array_split(np.arange(N),size)


#================================================================================
