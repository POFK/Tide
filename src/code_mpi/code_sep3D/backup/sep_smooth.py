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
        INF=open(PathOfINF,'a')
#       INF.writelines('# Information of data\n')
#       INF.writelines('# PATH of data: %s\n'%Input)
#       INF.writelines('# PATH of output: %s\n'%dir)
#       INF.writelines('#===============================================================================\n')

        INF.writelines('NOISE=%f\n'% (L**3/sum))  
#       INF.writelines('NOISE=%f\n'% (4.8*10**-3))  # to test 0709
        INF.writelines('nbar=%f\n'% (sum/L**3))
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
    mpi_senddata_k1/=window_k**2  #cic  
#======== for shot noise  =========
if SmoothHaloNbar:
    sum=comm.bcast(sum,root=0) 
if SmoothWienerOfShotnoise:
# old wiener
#   Ph=L**3/N**6*np.abs(mpi_senddata_k1)**2  
#   Ph=L**3/N**6*np.abs(mpi_senddata_k1)**2/window_k #for test
#   Wiener=(Ph-(L**3)/sum)/Ph  # wiener filter
#   Wiener=Ph/(Ph+(L**3)/sum)  # wiener filter
# new wiener
    from sep_wienerPh import WienerF
    Wienerf,bias,k_min,k_max=WienerF(dir,noise=L**3/sum)
#   Wienerf,bias,k_min,k_max=WienerF(dir,noise=4.8*10**-3)   # to test 0709
    if rank == 0:
        INF=open(PathOfINF,'a')
        INF.writelines('bias=%f\n'% (bias))
        INF.close()
    logk=np.log10(Kf*k)
    logk[(Kf*k)<k_min]=np.log10(k_min)
    shape=logk.shape
    Wiener=Wienerf(logk.reshape(-1))
    Wiener=Wiener.reshape(shape)
    Wiener[(Kf*k)<k_min]=Wienerf(np.log10(k_min))
    Wiener[(Kf*k)>k_max]=Wienerf(np.log10(k_max))
    mpi_senddata_k1*=Wiener
##========================================
## To save halo field which convolved Wiener.
#   if SmoothSaveWienerHalo:
#       DHW=mpi_recvdata_k1*Wiener
#       comm.Gather(DHW,smooth_k,root=0)
#       if rank==0:
#           ifft=fftw.Plan(inarray=smooth_k,outarray=deltax,direction='backward',nthreads=nthreads)
#           fftw.execute(ifft)
#           fftw.destroy_plan(ifft)
#           deltax/=N**3              #   smoothed
#           Tide.SaveDataHdf5(deltax,PathSoutput+'_W.hdf5')
#       del DHW
# a new method to save wiener
    if SmoothSaveWienerHalo:
        WIENER=None
        Wiener=np.array(Wiener,dtype=np.float64)
        if rank==0:
            WIENER=np.empty((N,N,N/2+1),dtype=np.float64)
        comm.Gather(Wiener,WIENER,root=0)
        if rank==0:
#           print WIENER.min(),WIENER.max()
            WIENER=np.array(WIENER,dtype=np.float32)
            Tide.SaveDataHdf5(WIENER,PathSoutput+'_Wiener.hdf5')
#========== save data ===================
comm.Gather(mpi_senddata_k1,smooth_k,root=0)
if rank==0:
#   smooth_k[0,0,0]=0+0j
    ifft=fftw.Plan(inarray=smooth_k,outarray=deltax,direction='backward',nthreads=nthreads)
    fftw.execute(ifft)
    fftw.destroy_plan(ifft)
    deltax/=N**3              #   smoothed
    if SmoothSaveSmoothedData:
        Tide.SaveDataHdf5(deltax,PathSoutput+'.hdf5')

