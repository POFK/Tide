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
smooth_k=None
deltagw1=None
deltagw2=None
deltak=None
deltax1=None
deltax2=None
sum=0.
Pk0=None
Pk1=None
Pk2=None
Pk3=None
k=None
window_k=None
recvdata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
senddata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
SaveHalo=True  #save Pk_halo
#delta_k=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
#wk=Tide.Get_wk()

if rank==0:
    import time
    Pk0=np.empty((N,N,N/2+1),dtype=np.float64)
    deltax=np.linspace(0,N,N**3).reshape(N,N,N)
    change=np.array(Tide.LoadData(Input),dtype=np.float64)
    deltax[:]=change[:]
    deltax=np.array(deltax,dtype=np.float64)
    del change
    sum=deltax.sum()
    deltax*=(N**3/sum)   #for halo, the data is n/nbar.
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
sum=comm.bcast(sum,root=0) #deltak
senddata_k1=recvdata_k1*np.exp(-0.5*Kf*Kf*k*k*Sigma**2)/window_k      #smooth_k
Ph=L**3/N**6*np.abs(senddata_k1)**2
Wiener=Ph/(Ph+(L**3)/sum)   #wiener filter
senddata_k1*=Wiener
Pk_halo=np.abs(recvdata_k1/window_k)**2
Pk_halo*=(L**3/N**6)
Pk_halo=np.array(Pk_halo,dtype=np.float64)
comm.Gather(senddata_k1,smooth_k,root=0)
comm.Gather(Pk_halo,Pk0,root=0)
if rank==0:
    from Gau import Gau
    ifft=fftw.Plan(inarray=smooth_k,outarray=deltax,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    deltax/=N**3              #   smoothed
    if SaveHalo:
        Tide.SaveDataHdf5(Pk0,Outfile+'0.000den00_Pk_halo.hdf5')
    Tide.SaveDataHdf5(deltax,Outfile+'0.000den00_s1.25.hdf5')
    print 'smoothing end, time: %dm %ds'%((time.time()-t0)/60,(time.time()-t0)%60)
