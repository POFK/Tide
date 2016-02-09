#!/usr/bin/env python
# coding=utf-8
from TIDES import *
from mpi4py import MPI
import fftw3 as fftw

comm=MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()

'''cal kappa '''
#par:
Input='/home/mtx/data/tide/0.000den00.bin'
Dir='/home/mtx/data/tide/outdata/test/'
filename1=Dir+'deltax1.25.hdf5'
filename2=Dir+'deltay1.25.hdf5'
N=1024
L=1.2*10**3
H=L/N
Kf=2*np.pi/L
fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
fnc=np.arange(N/2+1)
mpi_fn=np.array_split(fn,size)
mpi_index=np.array_split(np.arange(N),size)
nthreads=16   #fftw threads number

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#  Load data: #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
gamma1_x=None
gamma2_x=None
gamma1_k=None
gamma2_k=None
kappa3d_k=None
k=None
window_k=None
gamma1k=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
gamma2k=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
wk=Tide.Get_wk()
if rank==0:
    gamma1_x=np.empty((N,N,N),dtype=np.float64)
    gamma2_x=np.empty((N,N,N),dtype=np.float64)


#================================================================================
f=h5py.File(filename1,'r')
wdengx=f['data'][mpi_index[rank].tolist()]
f.close()
f=h5py.File(filename2,'r')
wdengy=f['data'][mpi_index[rank].tolist()]
f.close()

gamma1=wdengx*wdengx-wdengy*wdengy
gamma2=2*wdengx*wdengy
print gamma1.dtype
gamma1=np.array(gamma1,dtype=np.float64)
gamma2=np.array(gamma2,dtype=np.float64)

comm.Gather(gamma1,gamma1_x,root=0)
comm.Gather(gamma2,gamma2_x,root=0)

if rank==0:
    gamma1_k=np.empty((N,N,N/2+1),dtype=np.complex128)
    gamma2_k=np.empty((N,N,N/2+1),dtype=np.complex128)
    fft1=fftw.Plan(inarray=gamma1_x,outarray=gamma1_k,direction='forward',nthreads=nthreads)
    fft2=fftw.Plan(inarray=gamma2_x,outarray=gamma2_k,direction='forward',nthreads=nthreads)
    fftw.execute(fft1)
    fftw.execute(fft2)
    fftw.destroy_plan(fft1)
    fftw.destroy_plan(fft2)
comm.Scatter(gamma1_k,gamma1k,root=0)
comm.Scatter(gamma2_k,gamma2k,root=0)
k1=Kf*(mpi_fn[rank][:,None,None]+np.zeros_like(fn)[None,:,None]+np.zeros_like(fnc)[None,None,:])
k2=Kf*(np.zeros_like(mpi_fn[rank])[:,None,None]+fn[None,:,None]+np.zeros_like(fnc)[None,None,:])
S=k1**2+k2**2
if rank==0:
    S[0,0,:]=np.ones_like(S[0,0,:])
    kappa3d_k=np.empty((N,N,N/2+1),dtype=np.complex128)
K_mag2=Kf*Kf*(mpi_fn[rank][:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)
kappa3dk=2*K_mag2/(S**2)*((k1**2-k2**2)*gamma1k+2*k1*k2*gamma2k)

comm.Gather(kappa3dk,kappa3d_k,root=0)
if rank==0:
    kappa3d_x=np.empty((N,N,N),dtype=np.float64)
    ifft=fftw.Plan(inarray=kappa3d_k,outarray=kappa3d_x,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    kappa3d_x/=N**3
    Tide.SaveDataHdf5(kappa3d_x,Dir+'kappa3dx1.25.hdf5')
