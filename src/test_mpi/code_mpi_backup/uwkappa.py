#!/usr/bin/env python
# coding=utf-8
from TIDES import *
from mpi4py import MPI
import fftw3 as fftw

comm=MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()

'''To get uwkappa field'''

#par:
Input='/home/mtx/data/tide/0.000den00.bin'
Outfile='/home/mtx/data/tide/outdata/test/'
N=1024
L=1.2*10**3
H=L/N
Kf=2*np.pi/L
fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
fnc=np.arange(N/2+1)
mpi_fn=np.array_split(fn,size)
Sigma=1.25
nthreads=16   #fftw threads number

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#  Load data: #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
smooth_k=None
deltagw1=None
deltagw2=None
deltak=None
deltax1=None
deltax2=None
Pk1=None
Pk2=None
Pk3=None
k=None
window_k=None
recvdata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
senddata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
#delta_k=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
wk=Tide.Get_wk()

if rank==0:
    import time
    deltax=np.linspace(0,N,N**3).reshape(N,N,N)
    change=np.array(Tide.LoadData(Input),dtype=np.float64)
    deltax[:]=change[:]
    deltax=np.array(deltax,dtype=np.float64)
    del change
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
delta_k=recvdata_k1/window_k
comm.Gather(senddata_k1,smooth_k,root=0)
if rank==0:
    ifft=fftw.Plan(inarray=smooth_k,outarray=deltax,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    deltax/=N**3              #   smoothed
    print 'smoothing end, time: %dm %ds'%((time.time()-t0)/60,(time.time()-t0)%60)
    t0=time.time()
##################################Wdeltag########################################
    print '='*80
    print 'starting cal wdengx wdengy'
    deltagw1=np.empty_like(smooth_k,dtype=np.complex128)
    deltagw2=np.empty_like(smooth_k,dtype=np.complex128)
    deltax1=np.empty_like(deltax,dtype=np.float64) 
    deltax2=np.empty_like(deltax,dtype=np.float64) 
    del smooth_k
#   Tide.SaveDataHdf5(deltax,Outfile+'smooth_1.25.hdf5')
    deltak=np.empty((N,N,N/2+1),dtype=np.complex128)
    deltax=np.log(deltax)
    fft=fftw.Plan(inarray=deltax,outarray=deltak,direction='forward',nthreads=nthreads)
    fftw.execute(fft)
    fftw.destroy_plan(fft)
#   deltak/=N**3
    k[0,0,0]=10**-4/Kf
comm.Scatter(deltak,recvdata_k1,root=0) #deltak  smoothed log
W=wk(k*Kf)
if rank==0:
    W[0,0,0]=1
deltak1=recvdata_k1*W*1j*Kf*(mpi_fn[rank][:,None,None]+np.zeros_like(fn)[None,:,None]+np.zeros_like(fnc)[None,None,:])
deltak2=recvdata_k1*W*1j*Kf*(np.zeros_like(mpi_fn[rank])[:,None,None]+fn[None,:,None]+np.zeros_like(fnc)[None,None,:])
comm.Gather(deltak1,deltagw1,root=0)
comm.Gather(deltak2,deltagw2,root=0)
if rank==0:
    k[0,0,0]=0
    ifft=fftw.Plan(inarray=deltagw1,outarray=deltax1,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    deltax1/=N**3
    ifft=fftw.Plan(inarray=deltagw2,outarray=deltax2,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    deltax2/=N**3
    print 'wdengx wdengy , time: %dm %ds'%((time.time()-t0)/60,(time.time()-t0)%60)
    t0=time.time()
#   Tide.SaveDataHdf5(deltax1,Outfile+'deltax1.25.hdf5')
#   Tide.SaveDataHdf5(deltax2,Outfile+'deltay1.25.hdf5')





########################gamma1  gamma2##########################################
gamma1_x=None
gamma2_x=None
gamma1_k=None
gamma2_k=None
kappa3d_k=None
wdengx=np.empty((N/size,N,N),dtype=np.float64)
wdengy=np.empty((N/size,N,N),dtype=np.float64)
gamma1k=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
gamma2k=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
if rank==0:
    print '='*80
    print 'Cal kappa'
    gamma1_x=np.empty((N,N,N),dtype=np.float64)
    gamma2_x=np.empty((N,N,N),dtype=np.float64)


#================================================================================
comm.Scatter(deltax1,wdengx,root=0)
comm.Scatter(deltax2,wdengy,root=0)
gamma1=wdengx*wdengx-wdengy*wdengy
gamma2=2*wdengx*wdengy
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
    Pk1=np.empty((N,N,N/2+1),dtype=np.float64)
    Pk2=np.empty((N,N,N/2+1),dtype=np.float64)
    Pk3=np.empty((N,N,N/2+1),dtype=np.float64)
K_mag2=Kf*Kf*(mpi_fn[rank][:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)
kappa3dk=2*K_mag2/(S**2)*((k1**2-k2**2)*gamma1k+2*k1*k2*gamma2k)
kappak_w=kappa3dk/window_k

Pk_dd=np.abs(delta_k)**2
Pk_dd*=(L**3/N**6)
Pk_dd=np.array(Pk_dd,dtype=np.float64)
Pk_kk=np.abs(kappak_w)**2
Pk_kk*=(L**3/N**6)
Pk_kk=np.array(Pk_kk,dtype=np.float64)
Pk_dk=((delta_k.conjugate()*kappak_w+kappak_w.conjugate()*delta_k)/2.).real
Pk_dk*=(L**3/N**6)
Pk_dk=np.array(Pk_dk,dtype=np.float64)

comm.Gather(kappa3dk,kappa3d_k,root=0)
comm.Gather(Pk_dd,Pk1,root=0)
comm.Gather(Pk_dk,Pk2,root=0)
comm.Gather(Pk_kk,Pk3,root=0)
if rank==0:

    kappa3d_x=np.empty((N,N,N),dtype=np.float64)
    ifft=fftw.Plan(inarray=kappa3d_k,outarray=kappa3d_x,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    kappa3d_x/=N**3
    print 'Cal kappa end, time: %dm %ds'%((time.time()-t0)/60,(time.time()-t0)%60)
    t0=time.time()
    Tide.SaveDataHdf5(kappa3d_x,Outfile+'kappa3dx1.25.hdf5')
    Tide.SaveDataHdf5(Pk1,Outfile+'0.000den00_Pk_delta.hdf5')
    Tide.SaveDataHdf5(Pk2,Outfile+'0.000den00_Pk_delta_kappa.hdf5')
    Tide.SaveDataHdf5(Pk3,Outfile+'0.000den00_Pk_kappa.hdf5')
