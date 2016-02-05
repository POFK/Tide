#!/usr/bin/env python
# coding=utf-8
from TIDES import *
#from mpi4py import MPI
import fftw3 as fftw

#comm=MPI.COMM_WORLD
#size=comm.Get_size()
#rank=comm.Get_rank()

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
deltax=np.linspace(0,N,N**3).reshape(N,N,N)
#Tide.SaveDataHdf5(deltax,Outfile+'000del00.hdf5')
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
window_k= np.sinc(1./N*fn[:,None,None])*np.sinc(1./N*fn[None,:,None])*np.sinc(1./N*fnc[None,None,:])
smooth_k=deltak*np.exp(-0.5*Kf*Kf*k*k*Sigma**2)/window_k
print '2'
ifft=fftw.Plan(inarray=smooth_k,outarray=deltax,direction='backward',nthreads=8)
fftw.execute(ifft)
fftw.destroy_plan(ifft)
deltax/=N**3
print '3'
#Tide.SaveDataHdf5(deltax,Outfile+'smooth_1.25.hdf5')


