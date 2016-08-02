#!/usr/bin/env python
# coding=utf-8
#from TIDES import *
import h5py
from parameter import *
import fftw3 as fftw

'''get kappa(kv,kp),b,w, and get kappa(x)'''
#################################################################################
deltak=None
delta_k=np.empty((N/size,N,N/2+1),dtype=np.complex128)
########################## Load data ############################################
if rank==0:
    print '='*80
    print 'Cal wkkappa'
    deltax=Tide.LoadDataOfhdf5(PathWkkappaInput1)  #load kappax
    deltax=np.array(deltax,dtype=np.float64)
    deltak=np.empty((N,N,N/2+1),dtype=np.complex128)
    fft=fftw.Plan(inarray=deltax,outarray=deltak,direction='forward',nthreads=nthreads)
    fftw.execute(fft)
    fftw.destroy_plan(fft)
    
comm.Scatter(deltak,delta_k,root=0) #
binlog=np.linspace(0,np.log10(512),bins,endpoint=False)
dbinlog=binlog[2]-binlog[1]
binlog=np.hstack((binlog,binlog[-1]+dbinlog))
bin=10**binlog
bin[0]=0

b=np.loadtxt(PathWkkappaBias)
W=np.loadtxt(PathWkkappaWiener)

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
        delta_k[bool]=delta_k[bool]/b[i,j]*W[i,j]


comm.Gather(delta_k,deltak,root=0)
if rank==0:
    ifft=fftw.Plan(inarray=deltak,outarray=deltax,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    deltax/=N**3
    Tide.SaveDataHdf5(deltax,PathWkkappaOutput)
