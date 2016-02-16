#!/usr/bin/env python
# coding=utf-8
#from TIDES import *
#from mpi4py import MPI
import fftw3 as fftw
from parameter import *

#comm=MPI.COMM_WORLD
#size=comm.Get_size()
#rank=comm.Get_rank()

'''To get uwkappa field'''

##par:
#Input='/home/mtx/data/tide/0.000den00.bin'
#Outfile='/home/mtx/data/tide/outdata/test/'
#N=1024
#L=1.2*10**3
#H=L/N
#Kf=2*np.pi/L
#fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
#fnc=np.arange(N/2+1)
#mpi_fn=np.array_split(fn,size)
#Sigma=1.25
#nthreads=16   #fftw threads number

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#  Load data: #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
if rank==0:
    from Gau import Gau
    import time
    print '='*80
    t0=time.time()
    deltax=Tide.LoadDataOfhdf5(Outfile+'0.000den00_s1.25.hdf5')
##################################Gau....########################################
    deltax=Gau(deltax,Outfile+'Gau.hdf5')
    print 'Gau... end, time: %dm %ds'%((time.time()-t0)/60,(time.time()-t0)%60)
