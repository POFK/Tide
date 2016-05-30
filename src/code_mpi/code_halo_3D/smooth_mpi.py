#!/usr/bin/env python
# coding=utf-8
from TIDES import *
from mpi4py import MPI
import fftw3 as fftw

comm=MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()

#par:
#Input='/project/mtx/output/tides10/halo_0.0048/wfkappa.hdf5'
#Outfile='/project/mtx/data/tides10/kappa_1.25_s8.0.hdf5'
Input='/project/mtx/data/tides10/0.000delta.bin'
Outfile='/project/mtx/data/tides10/0.000delta_s10.0.hdf5'

N=1024
L=1.2*10**3
H=L/N
Kf=2*np.pi/L
fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
fnc=np.arange(N/2+1)
mpi_fn=np.array_split(fn,size)
Sigma=10.0
nthreads=16   #fftw threads number

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#  Load data: #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
smooth_k=None
deltagw1=None
deltagw2=None
deltak=None
k=None
window_k=None
recvdata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
senddata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
#wk=Tide.Get_wk()

if rank==0:
    import time
    deltax=np.linspace(0,N,N**3).reshape(N,N,N)
    change=np.array(Tide.LoadData(Input),dtype=np.float64)
    deltax[:]=change[:]
#   deltax=Tide.LoadDataOfhdf5(Input)
#   deltax=1+np.array(deltax,dtype=np.float64)
    print 'kappa mean',deltax.mean()
#   del change
###################################smooth#######################################
    print '='*80
    print 'smoothing...'
    t0=time.time()
    deltak=np.empty((N,N,N/2+1),dtype=np.complex128)
    fft=fftw.Plan(inarray=deltax,outarray=deltak,direction='forward',nthreads=nthreads)
    fftw.execute(fft)
    fftw.destroy_plan(fft)
    smooth_k=np.empty((N,N,N/2+1),dtype=np.complex128)
k=(mpi_fn[rank][:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)**(1./2.)
window_k= np.sinc(1./N*mpi_fn[rank][:,None,None])*np.sinc(1./N*fn[None,:,None])*np.sinc(1./N*fnc[None,None,:])
comm.Scatter(deltak,recvdata_k1,root=0) #deltak
senddata_k1=recvdata_k1*np.exp(-0.5*Kf*Kf*k*k*Sigma**2)/window_k      #smooth_k
comm.Gather(senddata_k1,smooth_k,root=0)
if rank==0:
    print senddata_k1 
    ifft=fftw.Plan(inarray=smooth_k,outarray=deltax,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    deltax/=N**3              #   smoothed
    print 'smoothed', deltax
    print 'smoothing end, time: %dm %ds'%((time.time()-t0)/60,(time.time()-t0)%60)
    t0=time.time()
##################################Wdeltag########################################
    print 'starting cal wdengx wdengy'
    deltagw1=np.empty_like(smooth_k,dtype=np.complex128)
    deltagw2=np.empty_like(smooth_k,dtype=np.complex128)
    deltax1=np.empty_like(deltax,dtype=np.float64) 
    deltax2=np.empty_like(deltax,dtype=np.float64) 
    del smooth_k
    Tide.SaveDataHdf5(deltax,Outfile)
#    deltak=np.empty((N,N,N/2+1),dtype=np.complex128)
#    deltax=np.log(deltax)
#    fft=fftw.Plan(inarray=deltax,outarray=deltak,direction='forward',nthreads=nthreads)
#    fftw.execute(fft)
#    fftw.destroy_plan(fft)
##   deltak/=N**3
#    k[0,0,0]=10**-4/Kf
#comm.Scatter(deltak,recvdata_k1,root=0) #deltak  smoothed log
#W=wk(k*Kf)
#if rank==0:
#    W[0,0,0]=1
#deltak1=recvdata_k1*W*1j*Kf*(mpi_fn[rank][:,None,None]+np.zeros_like(fn)[None,:,None]+np.zeros_like(fnc)[None,None,:])
#deltak2=recvdata_k1*W*1j*Kf*(np.zeros_like(mpi_fn[rank])[:,None,None]+fn[None,:,None]+np.zeros_like(fnc)[None,None,:])
#comm.Gather(deltak1,deltagw1,root=0)
#comm.Gather(deltak2,deltagw2,root=0)
#if rank==0:
#    k[0,0,0]=0
#    ifft=fftw.Plan(inarray=deltagw1,outarray=deltax1,direction='backward',nthreads=nthreads)
#    fftw.execute(ifft)
#    fftw.destroy_plan(ifft)
#    deltax1/=N**3
#    ifft=fftw.Plan(inarray=deltagw2,outarray=deltax2,direction='backward',nthreads=nthreads)
#    fftw.execute(ifft)
#    fftw.destroy_plan(ifft)
#    deltax2/=N**3
#    print 'wdengx wdengy , time: %dm %ds',%((time.time()-t0)/60,(time.time()-t0)%60)
#    t0=time.time()
#    Tide.SaveDataHdf5(deltax1,Outfile+'deltax1.25.hdf5')
#    Tide.SaveDataHdf5(deltax2,Outfile+'deltay1.25.hdf5')
#########################gamma1  gamma2##########################################
#
