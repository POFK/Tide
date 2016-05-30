#!/usr/bin/env python
# coding=utf-8
from TIDES import *
from mpi4py import MPI
import fftw3 as fftw

comm=MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()

N=1024
L=1.2*10**3
H=L/N
Kf=2*np.pi/L
fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
fnc=np.arange(N/2+1)
mpi_fn=np.array_split(fn,size)
nthreads=16   #fftw threads number

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#  Load data: #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
def pk_cro(Input1='',Input2='',output=''):
    smooth_k=None
    deltagw1=None
    deltagw2=None
    deltak1=None
    deltak2=None
    k=None
    window_k=None
    recvdata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
    recvdata_k2=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
    senddata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)

    if rank==0:
        import time
        deltax1=np.linspace(0,N,N**3).reshape(N,N,N)
        change=np.array(Tide.LoadData(Input1),dtype=np.float64)
        deltax1[:]=change[:]
        deltax2=np.linspace(0,N,N**3).reshape(N,N,N)
        change=np.array(Tide.LoadData(Input2),dtype=np.float64)
        deltax2[:]=change[:]
        deltax2/=(deltax2.sum()/N**3)
        del change
    ###################################fftw#######################################
        deltak1=np.empty((N,N,N/2+1),dtype=np.complex128)
        fft=fftw.Plan(inarray=deltax1,outarray=deltak1,direction='forward',nthreads=nthreads)
        fftw.execute(fft)
        fftw.destroy_plan(fft)
        deltak2=np.empty((N,N,N/2+1),dtype=np.complex128)
        fft=fftw.Plan(inarray=deltax2,outarray=deltak2,direction='forward',nthreads=nthreads)
        fftw.execute(fft)
        fftw.destroy_plan(fft)
        smooth_k=np.empty((N,N,N/2+1),dtype=np.complex128)
    k=(mpi_fn[rank][:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)**(1./2.)
    window_k= np.sinc(1./N*mpi_fn[rank][:,None,None])*np.sinc(1./N*fn[None,:,None])*np.sinc(1./N*fnc[None,None,:])
    comm.Scatter(deltak1,recvdata_k1,root=0) #deltak1
    comm.Scatter(deltak2,recvdata_k2,root=0) #deltak2
    recvdata_k1/=window_k
    recvdata_k2/=window_k
    senddata_k1=(recvdata_k1.conjugate()*recvdata_k2+recvdata_k2.conjugate()*recvdata_k1)/2. #pk
    senddata_k1*=(L**3/N**6)
    
    comm.Gather(senddata_k1,smooth_k,root=0)
    if rank==0:
        pk_cro=np.array(smooth_k.real,dtype=np.float32)
        Tide.SaveDataHdf5(pk_cro,output)
