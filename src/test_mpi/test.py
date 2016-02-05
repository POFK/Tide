#!/usr/bin/env python
# coding=utf-8
from TIDES import *
#from mpi4py import MPI
import fftw3 as fftw
from time import time

#comm=MPI.COMM_WORLD
#size=comm.Get_size()
#rank=comm.Get_rank()

#par:
Input='/home/mtx/data/tide/0.000den00.bin'
Outfile='/home/mtx/data/tide/outdata/test/'
nthreads=8
N=1024
L=1.2*10**3
H=L/N
Kf=2*np.pi/L
fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
fnc=np.arange(N/2+1)
Sigma=1.25

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#  Load data: #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
t0=time()
deltax=np.empty((N,N,N),dtype=np.float)
#Tide.SaveDataHdf5(deltax,Outfile+'000del00.hdf5')
change=np.array(Tide.LoadData(Input),dtype=np.float64)
deltax[:]=change[:]
del change
deltak=np.empty((N,N,N/2+1),dtype=np.complex)
print deltax.shape
print deltax.dtype
fft=fftw.Plan(inarray=deltax,outarray=deltak,direction='forward',nthreads=nthreads)
fftw.execute(fft)
fftw.destroy_plan(fft)
k=(fn[:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)**(1./2.)
window_k= np.sinc(1./N*fn[:,None,None])*np.sinc(1./N*fn[None,:,None])*np.sinc(1./N*fnc[None,None,:])
smooth_k=deltak*np.exp(-0.5*Kf*Kf*k*k*Sigma**2)/window_k
ifft=fftw.Plan(inarray=smooth_k,outarray=deltax,direction='backward',nthreads=nthreads)
fftw.execute(ifft)
fftw.destroy_plan(ifft)
deltax/=N**3
print time()-t0
t0=time()
#deltax[deltax>0]=np.log10(deltax[deltax>0])
################################## deltagW #####################################
wk=Tide.Get_wk()
k[0,0,0]=10**(-4)/Kf
fft=fftw.Plan(inarray=deltax,outarray=deltak,direction='forward',nthreads=nthreads)
fftw.execute(fft)
fftw.destroy_plan(fft)
W=wk(k*Kf)
W[0,0,0]=0
print time()-t0
deltakx=deltak*W*1j*(fn[:,None,None]+0*fn[None,:,None]+0*fnc[None,None,:])
deltaky=deltak*W*1j*(fn[None,:,None]+0*fn[:,None,None]+0*fnc[None,None,:])
deltax1=np.empty_like(deltax)
ifft=fftw.Plan(inarray=deltakx,outarray=deltax1,direction='backward',nthreads=nthreads)
deltax1/=N**3
print time()-t0
t0=time()

Tide.SaveDataHdf5(deltax1,Outfile+'deltax11.25.hdf5')




print time()-t0








#Tide.SaveDataHdf5(deltax,Outfile+'smooth_1.25.hdf5')


