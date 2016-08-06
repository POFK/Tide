#!/usr/bin/env python
# coding=utf-8

import numpy as np
import fftw3 as fftw
from parameter import *
from read_par import readPar
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#  INIT       #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
deltagw1=None
deltagw2=None
deltagw3=None
deltak=None
k=None
window_k=None
mpi_recvdata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
mpi_senddata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
########################  Load data  ###########################################
#INF=readPar(PathOfINF)
#bias=np.float(INF['bias'])
k=(mpi_fn[rank][:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)**(1./2.)
wk=Tide.Get_wk()
#wk=Tide.Get_wk(bias=bias,shotnoise=Shotnoise)
if rank==0:
    deltax=Tide.LoadDataOfhdf5(PathGwinput)   # input smoothed halo field
    deltak=np.empty((N,N,N/2+1),dtype=np.complex128)
##################################Wdeltag########################################
    print '='*80
    print 'starting cal wdengx wdengy wdengz'
    deltagw1=np.empty((N,N,N/2+1),dtype=np.complex128)
    deltagw2=np.empty((N,N,N/2+1),dtype=np.complex128)
    deltagw3=np.empty((N,N,N/2+1),dtype=np.complex128)
    deltax1=np.empty_like(deltax,dtype=np.float64) 
    deltax2=np.empty_like(deltax,dtype=np.float64) 
    deltax3=np.empty_like(deltax,dtype=np.float64) 
    fft=fftw.Plan(inarray=deltax,outarray=deltak,direction='forward',nthreads=nthreads)
    fftw.execute(fft)
    fftw.destroy_plan(fft)
    k[0,0,0]=10**-4/Kf
comm.Scatter(deltak,mpi_recvdata_k1,root=0) #deltak  smoothed 
W=wk(k*Kf)
if rank==0:
    W[0,0,0]=0
deltak1=mpi_recvdata_k1*W*1j*Kf*(mpi_fn[rank][:,None,None]+np.zeros_like(fn)[None,:,None]+np.zeros_like(fnc)[None,None,:])
deltak2=mpi_recvdata_k1*W*1j*Kf*(np.zeros_like(mpi_fn[rank])[:,None,None]+fn[None,:,None]+np.zeros_like(fnc)[None,None,:])
deltak3=mpi_recvdata_k1*W*1j*Kf*(np.zeros_like(mpi_fn[rank])[:,None,None]+np.zeros_like(fn)[None,:,None]+fnc[None,None,:])
comm.Gather(deltak1,deltagw1,root=0)
comm.Gather(deltak2,deltagw2,root=0)
comm.Gather(deltak3,deltagw3,root=0)
if rank==0:
    k[0,0,0]=0
    ifft=fftw.Plan(inarray=deltagw1,outarray=deltax1,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    deltax1/=N**3
    ifft=fftw.Plan(inarray=deltagw2,outarray=deltax2,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    deltax2/=N**3
    ifft=fftw.Plan(inarray=deltagw3,outarray=deltax3,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    deltax3/=N**3
    if GwSaveGwData:
        Tide.SaveDataHdf5(deltax1,PathGwoutput+'wdeng1.hdf5')
        Tide.SaveDataHdf5(deltax2,PathGwoutput+'wdeng2.hdf5')
        Tide.SaveDataHdf5(deltax3,PathGwoutput+'wdeng3.hdf5')
