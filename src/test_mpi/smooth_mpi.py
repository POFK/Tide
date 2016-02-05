#!/usr/bin/env python
# coding=utf-8
from TIDES import *
from mpi4py import MPI
import fftw3 as fftw

comm=MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()

#par:
Input='/home/mtx/data/tide/0.000den00.bin'
Outfile='/home/mtx/data/tide/outdata/test/'
N=1024
L=1.2*10**3
H=L/N
Kf=2*np.pi/L
fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
fnc=np.arange(N/2+1)
Sigma=1.25

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#  Load data: #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
senddata=None
smooth_k=None
deltak=None
k=None
window_k=None
recvdata_k1=np.empty((N/(size-1),N,N),dtype=np.complex)
senddata_k1=np.empty((N/(size-1),N,N),dtype=np.complex)
recvdata_x1=np.empty((N/(size-1),N,N),dtype=np.float)
recvdata_x2=np.empty((N/(size-1),N,N),dtype=np.float)
zeros=np.zeros(size)
counts=zeros+N**3/(size-1)
counts[0]=0
dspls=(np.arange(size)-1)*N**3/(size-1)
dspls[0]=0


if rank==0:
    deltax=np.linspace(0,N,N**3).reshape(N,N,N)
    change=np.array(Tide.LoadData(Input),dtype=np.float64)
    deltax[:]=change[:]
    print '0'
    del change
    deltak=np.empty((N,N,N/2+1),dtype=np.complex)
    print deltax.shape
    print deltax.dtype
    fft=fftw.Plan(inarray=deltax,outarray=deltak,direction='forward',nthreads=8)
    fftw.execute(fft)
    fftw.destroy_plan(fft)
    print '1'
    k=(fn[:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)**(1./2.)
#   k[N/2+1:,:,:]=0
    window_k= np.sinc(1./N*fn[:,None,None])*np.sinc(1./N*fn[None,:,None])*np.sinc(1./N*fnc[None,None,:])
    smooth_k=np.empty((N,N,N/2+1),dtype=np.complex)
    print '2'
#comm.Scatterv([deltak,counts,dspls,MPI.DOUBLE_COMPLEX],recvdata_k1,root=0) #deltak
comm.Scatter(deltak,recvdata_k1,root=0) #deltak
print '2.1'
#comm.Scatterv([k,counts,dspls,MPI.DOUBLE],recvdata_x1,root=0)              #k
comm.Scatterv(k,recvdata_x1,root=0)              #k
print '2.2'
#comm.Scatterv([window_k,counts,dspls,MPI.DOUBLE],recvdata_x2,root=0)       #window_k
comm.Scatterv(window_k,recvdata_x2,root=0)       #window_k
print '2.3'
if rank!=0:
    senddata_k1=recvdata_k1*np.exp(-0.5*Kf*Kf*recvdata_x1*recvdata_x1*Sigma**2)/recvdata_x2    #smooth_k
comm.Gather(senddata_k1,smooth_k,root=0)
print '2.4'
if rank==0:
    print '3'
    smooth_k=smooth_k[N/size-1:][:N/2+1]
    print smooth_k.shape
    ifft=fftw.Plan(inarray=smooth_k,outarray=deltax,direction='backward',nthreads=4)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    deltax/=N**3
    print '4'
    Tide.SaveDataHdf5(deltax,Outfile+'smooth_1.25.hdf5')


