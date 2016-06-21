#!/usr/bin/env python
# coding=utf-8
import numpy as np
import fftw3 as fftw
from parameter import *


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#  INIT       #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
smooth_k=None
deltagw1=None
deltagw2=None
deltak=None
k=None
window_k=None
mpi_recvdata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)
mpi_senddata_k1=np.empty((N/(size),N,N/2+1),dtype=np.complex128)


if rank==0:
    deltax=Tide.LoadDataOfhdf5(PathSinput)   # input halo field
    if SmoothHaloNbar:
        sum=deltax.sum()
        deltax*=(N**3/sum)   #for halo, the data is n/nbar.
        print 'n bar:', sum/L**3
        print 'shot noise',L**3/sum
#========save information of data=========
        INF=open(PathOfINF,'w')
        INF.writelines('# Information of data\n')
        INF.writelines('# PATH of data: %s\n'%Input)
        INF.writelines('# PATH of output: %s\n'%dir)
        INF.writelines('#===============================================================================\n')
        INF.writelines('NOISE=%f\n'% (L**3/sum))
        INF.writelines('nbar=%f\n'% (sum/L**3))
        INF.writelines('Sigma=%f\n'% (Sigma))
        INF.writelines('CutOff=%s\n'% str(CutOff))
        INF.writelines('Gaussian=%s\n'% str(Gaussian))
        INF.writelines('SmoothWienerOfShotnoise=%s\n'% str(SmoothWienerOfShotnoise))
        INF.close()
###################################smooth#######################################
    print '='*80
    print 'smoothing...'
    deltak=np.empty((N,N,N/2+1),dtype=np.complex128)
    fft=fftw.Plan(inarray=deltax,outarray=deltak,direction='forward',nthreads=nthreads)
    fftw.execute(fft)
    fftw.destroy_plan(fft)
    smooth_k=np.empty((N,N,N/2+1),dtype=np.complex128)
k=(mpi_fn[rank][:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)**(1./2.)
window_k= (np.sinc(1./N*mpi_fn[rank][:,None,None])*np.sinc(1./N*fn[None,:,None])*np.sinc(1./N*fnc[None,None,:]))
comm.Scatter(deltak,mpi_recvdata_k1,root=0) #deltak
mpi_senddata_k1=mpi_recvdata_k1*np.exp(-0.5*Kf*Kf*k*k*Sigma**2)     #smooth_k
#mpi_senddata_k1=mpi_recvdata_k1     #for test
#========window of top hat=========
if SmoothWindowOfTophat:
    mpi_senddata_k1/=window_k 
#======== for shot noise  =========
if SmoothHaloNbar:
    sum=comm.bcast(sum,root=0) 
if SmoothWienerOfShotnoise:
    Ph=L**3/N**6*np.abs(mpi_senddata_k1)**2  
#   Ph=L**3/N**6*np.abs(mpi_senddata_k1)**2/window_k #for test
    Wiener=(Ph-(L**3)/sum)/Ph  # wiener filter
#   Wiener=Ph/(Ph+(L**3)/sum)  # wiener filter
    if rank==0:
        print Wiener
    mpi_senddata_k1*=Wiener
##========================================
## To save halo field which convolved Wiener.
    if SmoothSaveWienerHalo:
        DHW=mpi_recvdata_k1*Wiener
        comm.Gather(DHW,smooth_k,root=0)
        if rank==0:
            ifft=fftw.Plan(inarray=smooth_k,outarray=deltax,direction='backward',nthreads=nthreads)
            fftw.execute(ifft)
            fftw.destroy_plan(ifft)
            deltax/=N**3              #   smoothed
            Tide.SaveDataHdf5(deltax,PathSoutput+'_W.hdf5')
        del DHW
##========== save data ===================
comm.Gather(mpi_senddata_k1,smooth_k,root=0)
if rank==0:
#   smooth_k[0,0,0]=0+0j
    ifft=fftw.Plan(inarray=smooth_k,outarray=deltax,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    deltax/=N**3              #   smoothed
    if SmoothSaveSmoothedData:
        Tide.SaveDataHdf5(deltax,PathSoutput+'.hdf5')

