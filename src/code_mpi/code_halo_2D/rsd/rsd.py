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
recvdata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
senddata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
mpi_halo=np.empty((N/(size),N,N),dtype=np.float64)
SaveHalo=True  #save Pk_halo
#delta_k=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
#wk=Tide.Get_wk()
################################################################################
bias=1.1136226513850853
factor=0.308**0.6
beta=factor/bias
################################################################################

if rank==0:
    import time
    print '='*80
    print 'displacement'
    t0=time.time()
    smooth_x=Tide.LoadDataOfhdf5(Outfile+'0.000den00_s1.25.hdf5')
    halo=Tide.LoadData(Input)
    halo=np.array(halo,dtype=np.float64)
    smooth_k=np.empty((N,N,N/2+1),dtype=np.complex128)
    s_k=np.empty((N,N,N/2+1),dtype=np.complex128)
    fft=fftw.Plan(inarray=smooth_x,outarray=smooth_k,direction='forward',nthreads=nthreads)
    fftw.execute(fft)
    fftw.destroy_plan(fft)

comm.Scatter(smooth_k,recvdata_k1,root=0) #deltak
comm.Scatter(halo,mpi_halo,root=0) #deltak
k_mag=(mpi_fn[rank][:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)**(1./2.)
kp=(np.zeros_like(mpi_fn[rank])[:,None,None]**2.+np.zeros_like(fn)[None,:,None]**2.+fnc[None,None,:]**2)**(1./2.)
mu=kp/k_mag
senddata_k1=-1j/bias/k_mag*recvdata_k1/(1+beta*mu**2)
comm.Gather(senddata_k1,s_k,root=0)

if rank==0:
    s_x=np.empty((N,N,N),dtype=np.float64)
    ifft=fftw.Plan(inarray=s_k,outarray=s_x,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    s_x/=N**3
dpm_z=np.empty((N/size,N,N),dtype=np.float64)
comm.Scatter(s_x,dpm_z,root=0) #deltak
dpm_z*=factor*mu#*H                                        #displacement of z
dpm0=(np.arange(N)+0.5)#*H
if rank==0:
    print dpm0
    print dpm_z
    print 'step 1, time: %dm %ds'%((time.time()-t0)/60,(time.time()-t0)%60)
    t0=time.time()

mpi_dpm0=np.array_split(dpm0,size)
X=mpi_dpm0[:,None,None]+np.zeros_like(dpm0)[None,:,None]+np.zeros_like(dpm0)[None,None,:]
Y=np.zeros_like(mpi_dpm0)[:,None,None]+dpm0[None,:,None]+np.zeros_like(dpm0)[None,None,:]
Z=np.zeros_like(mpi_dpm0)[:,None,None]+np.zeros_like(dpm0)[None,:,None]+dpm0[None,None,:]-dpm_z
shape=X0.shape
DPM=np.c_[X.reshape(-1),Y.reshape(-1),Z.reshape(-1)]
edge=np.arange(N+1)#*H
S=np.histogramdd(sample=DPM,bins=(edge,edge,edge),weights=mpi_halo)[0]
comm.Reduce(S, halo, op=MPI.SUM, root=0)
if rank==0:
    if SaveHalo:
        Tide.SaveDataOfhdf5(Outfile+'halo_dealrsd.hdf5')








