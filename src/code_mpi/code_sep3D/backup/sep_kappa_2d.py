#!/usr/bin/env python
# coding=utf-8
import fftw3 as fftw
from parameter import *


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#  INIT       #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
deltagw1=None
deltagw2=None
deltagw3=None
gm1_k=None
gm2_k=None
kappa3d_k=None
k=None
window_k=None
mpi_reck1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
mpi_reck2=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
mpi_senddata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
########################  Load data  ###########################################
k_mag=Kf*(mpi_fn[rank][:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)**(1./2.)
k1=Kf*(mpi_fn[rank][:,None,None]+np.zeros_like(fn)[None,:,None]+np.zeros_like(fnc)[None,None,:])
k2=Kf*(np.zeros_like(mpi_fn[rank])[:,None,None]+fn[None,:,None]+np.zeros_like(fnc)[None,None,:])
S=k1**2+k2**2
if rank==0:
    S[0,0,:]=np.ones_like(S[0,0,:])
    print '='*80
    print 'starting cal kappa 2D'
    gm1_x=Tide.LoadDataOfhdf5(PathKappainput+'gm1.hdf5')   # input gamma_1
    gm2_x=Tide.LoadDataOfhdf5(PathKappainput+'gm2.hdf5')   # input gamma_2
    gm1_k=np.empty((N,N,N/2+1),dtype=np.complex128)
    gm2_k=np.empty((N,N,N/2+1),dtype=np.complex128)
    fft1=fftw.Plan(inarray=gm1_x,outarray=gm1_k,direction='forward',nthreads=nthreads)
    fft2=fftw.Plan(inarray=gm2_x,outarray=gm2_k,direction='forward',nthreads=nthreads)
    fftw.execute(fft1)
    fftw.execute(fft2)
    fftw.destroy_plan(fft1)
    fftw.destroy_plan(fft2)
    kappa3d_k=np.empty((N,N,N/2+1),dtype=np.complex128)
comm.Scatter(gm1_k,mpi_reck1,root=0) #gamma1_k
comm.Scatter(gm2_k,mpi_reck2,root=0) #gamma2_k
mpi_senddata_k1=2*k_mag**2/(S**2)*((k1**2-k2**2)*mpi_reck1+2*k1*k2*mpi_reck2)
comm.Gather(mpi_senddata_k1,kappa3d_k,root=0)
if rank==0:
    kappa3d_x=np.empty((N,N,N),dtype=np.float64)
#   print kappa3d_k
    ifft=fftw.Plan(inarray=kappa3d_k,outarray=kappa3d_x,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    kappa3d_x/=N**3
    Tide.SaveDataHdf5(kappa3d_x,PathKappaoutput+'2D.hdf5')


