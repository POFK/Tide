#!/usr/bin/env python
# coding=utf-8
#from TIDES import *
import h5py
from parameter import *
#from mpi4py import MPI
import fftw3 as fftw

'''get kappa(kv,kp),b,w, and get kappa(x)'''
dir=Outfile
#Input2='/home/mtx/data/tide/0.000den00.bin'
input1=dir+'0.000den00_Pk_delta.hdf5'
input2=dir+'0.000den00_Pk_delta_kappa.hdf5'
input3=dir+'0.000den00_Pk_kappa.hdf5'
#Outfile='/home/mtx/data/tide/outdata/test/'
#################################################################################
#comm = MPI.COMM_WORLD
#size = comm.Get_size()
#rank = comm.Get_rank()

#N=1024
#L=1.2*10**3
#H=L/N
#Kf=2*np.pi/L
#fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
#fnc=np.arange(N/2+1)
#mpi_fn=np.array_split(fn,size)
#mpi_index=np.array_split(np.arange(N),size)
#nthreads=16
#bins=10
################################################################################
kappak=None
deltak=None
delta_k=np.empty((N/size,N,N/2+1),dtype=np.complex128)
kappa_k=np.empty((N/size,N,N/2+1),dtype=np.complex128)
window_k= np.sinc(1./N*mpi_fn[rank][:,None,None])*np.sinc(1./N*fn[None,:,None])*np.sinc(1./N*fnc[None,None,:])
########################## Load data ############################################
if rank==0:
    print '='*80
    print 'Cal wkkappa'
    deltax=np.linspace(0,N,N**3).reshape(N,N,N)
    change=np.array(Tide.LoadData(Input2),dtype=np.float64)
    deltax[:]=change[:]
    deltax=np.array(deltax,dtype=np.float64)
    del change
    deltak=np.empty((N,N,N/2+1),dtype=np.complex128)
    fft=fftw.Plan(inarray=deltax,outarray=deltak,direction='forward',nthreads=nthreads)
    fftw.execute(fft)
    fftw.destroy_plan(fft)
    kappax=Tide.LoadDataOfhdf5(dir+'kappa3dx.hdf5')
    kappak=np.empty((N,N,N/2+1),dtype=np.complex128)
    fft=fftw.Plan(inarray=kappax,outarray=kappak,direction='forward',nthreads=nthreads)
    fftw.execute(fft)
    fftw.destroy_plan(fft)

comm.Scatter(deltak,delta_k,root=0) #deltak
comm.Scatter(kappak,kappa_k,root=0) #deltak
#delta_k/=window_k
binlog=np.linspace(0,np.log10(512),bins,endpoint=False)
dbinlog=binlog[2]-binlog[1]
binlog=np.hstack((binlog,binlog[-1]+dbinlog))
bin=10**binlog
bin[0]=0

b=np.loadtxt('./result_b')
W=np.loadtxt('./result_W')

KV=((mpi_fn[rank]**2)[:,None,None]+(fn**2)[None,:,None]+np.zeros_like(fnc**2)[None,None,:])**(0.5)
KV=np.array(KV,dtype=np.float64)
KP=(np.zeros_like(mpi_fn[rank]**2)[:,None,None]+np.zeros_like(fn**2)[None,:,None]+(fnc**2)[None,None,:])**(0.5)
KP=np.array(KP,dtype=np.float64)
for i in range(bins):
    for j in range(bins):
        bool1=(bin[j]<=KV)*(KV<bin[j+1])
        bool2=(bin[i]<=KP)*(KP<bin[i+1])
        bool=bool1*bool2
        if i+j==0:
            if rank==0:
                bool[0,0]=False
        kappa_k[bool]=kappa_k[bool]/b[i,j]*W[i,j]

#Pk_dd=np.abs(delta_k)**2
#Pk_dd*=(L**3/N**6)
#Pk_dd=np.array(Pk_dd,dtype=np.float64)
Pk_kk=np.abs(kappa_k)**2
Pk_kk*=(L**3/N**6)
Pk_kk=np.array(Pk_kk,dtype=np.float64)
Pk_dk=((delta_k.conjugate()*kappa_k+kappa_k.conjugate()*delta_k)/2.).real
Pk_dk*=(L**3/N**6)
Pk_dk=np.array(Pk_dk,dtype=np.float64)

g=h5py.File(input3)
g['data'][mpi_index[rank].tolist()]=Pk_kk
f=h5py.File(input2)
f['data'][mpi_index[rank].tolist()]=Pk_dk

comm.Gather(kappa_k,kappak,root=0)
if rank==0:
    ifft=fftw.Plan(inarray=kappak,outarray=kappax,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    kappax/=N**3
    Tide.SaveDataHdf5(kappax,dir+'wfkappa.hdf5')
f.close()
g.close()
