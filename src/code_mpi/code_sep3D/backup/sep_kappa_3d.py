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
gmx_k=None
gmy_k=None
gmz_k=None
kappa3d_k=None
k=None
window_k=None
mpi_reck1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
mpi_reck2=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
mpi_reckx=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
mpi_recky=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
mpi_reckz=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
mpi_senddata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
########################  Load data  ###########################################
k_mag=Kf*(mpi_fn[rank][:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)**(1./2.)
k1=Kf*(mpi_fn[rank][:,None,None]+np.zeros_like(fn)[None,:,None]+np.zeros_like(fnc)[None,None,:])
k2=Kf*(np.zeros_like(mpi_fn[rank])[:,None,None]+fn[None,:,None]+np.zeros_like(fnc)[None,None,:])
k3=Kf*(np.zeros_like(mpi_fn[rank])[:,None,None]+np.zeros_like(fn)[None,:,None]+fnc[None,None,:])
if rank==0:
    print '='*80
    print 'starting cal kappa 3D'
    gm1_x=Tide.LoadDataOfhdf5(PathKappainput+'gm1.hdf5')   # input gamma_1
    gm2_x=Tide.LoadDataOfhdf5(PathKappainput+'gm2.hdf5')   # input gamma_2
    gmx_x=Tide.LoadDataOfhdf5(PathKappainput+'gmx.hdf5')   # input gamma_x
    gmy_x=Tide.LoadDataOfhdf5(PathKappainput+'gmy.hdf5')   # input gamma_y
    gmz_x=Tide.LoadDataOfhdf5(PathKappainput+'gmz.hdf5')   # input gamma_z
    gm1_k=np.empty((N,N,N/2+1),dtype=np.complex128)
    gm2_k=np.empty((N,N,N/2+1),dtype=np.complex128)
    gmx_k=np.empty((N,N,N/2+1),dtype=np.complex128)
    gmy_k=np.empty((N,N,N/2+1),dtype=np.complex128)
    gmz_k=np.empty((N,N,N/2+1),dtype=np.complex128)
    fft1=fftw.Plan(inarray=gm1_x,outarray=gm1_k,direction='forward',nthreads=nthreads)
    fft2=fftw.Plan(inarray=gm2_x,outarray=gm2_k,direction='forward',nthreads=nthreads)
    fft3=fftw.Plan(inarray=gmx_x,outarray=gmx_k,direction='forward',nthreads=nthreads)
    fft4=fftw.Plan(inarray=gmy_x,outarray=gmy_k,direction='forward',nthreads=nthreads)
    fft5=fftw.Plan(inarray=gmz_x,outarray=gmz_k,direction='forward',nthreads=nthreads)
    fftw.execute(fft1)
    fftw.execute(fft2)
    fftw.execute(fft3)
    fftw.execute(fft4)
    fftw.execute(fft5)
    fftw.destroy_plan(fft1)
    fftw.destroy_plan(fft2)
    fftw.destroy_plan(fft3)
    fftw.destroy_plan(fft4)
    fftw.destroy_plan(fft5)
    k_mag[0,0,0]=np.inf
    kappa3d_k=np.empty((N,N,N/2+1),dtype=np.complex128)
comm.Scatter(gm1_k,mpi_reck1,root=0) #gamma1_k
comm.Scatter(gm2_k,mpi_reck2,root=0) #gamma2_k
comm.Scatter(gmx_k,mpi_reckx,root=0) #gammax_k
comm.Scatter(gmy_k,mpi_recky,root=0) #gammay_k
comm.Scatter(gmz_k,mpi_reckz,root=0) #gammaz_k
mpi_senddata_k1 = 1./k_mag**2*((k1**2-k2**2)*mpi_reck1+2*k1*k2*mpi_reck2+2*k1*k3*mpi_reckx+2*k2*k3*mpi_recky+(2*k3**2-k1**2-k2**2)*mpi_reckz)
comm.Gather(mpi_senddata_k1,kappa3d_k,root=0)
if rank==0:
    kappa3d_x=np.empty((N,N,N),dtype=np.float64)
    ifft=fftw.Plan(inarray=kappa3d_k,outarray=kappa3d_x,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    kappa3d_x/=N**3
    Tide.SaveDataHdf5(kappa3d_x,PathKappaoutput+'3D.hdf5')


