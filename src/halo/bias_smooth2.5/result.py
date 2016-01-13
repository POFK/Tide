#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import *
import sys
name=sys.argv[1]
name2=sys.argv[2]
sigma=2.5
Inputfilename='/home/zhm/'+name+'/halorhobin1024m1z0.000.dat'
Outputfilename='/home/mtx/data/tide/outdata/'+name+'/halo/'+name2+'/'
print Inputfilename
print Outputfilename
########################################load data########################################
halo_x=Tide.LoadData(filename=Inputfilename)
#####################add later of wiener filter and smooth######################
Kf=2*np.pi/(1.2*10**3)
x = np.fft.fftfreq(N,1./N)  # x: 0,1,2,...,512,-511,...,-2,-1
sum=halo_x.sum()
halo_x=(1024**3)/sum*halo_x
halo_k=np.fft.fftn(halo_x)
#********************************************************************************
k=(x[:,None,None]**2.+x[None,:,None]**2.+x[None,None,:]**2.)**(1./2.)
window_k = np.sinc( 1./N* x[:,None,None]) * np.sinc( 1./N * x[None,:,None]) * np.sinc( 1./N * x[None,None,:])

halo_k2=halo_k*(np.exp(-0.5*(Kf*Kf)*k*k*sigma**2))/window_k
Ph=L**3/N**6*np.abs(halo_k2)**2
W=Ph/(Ph+(1024.**3)/sum)  #wiener filter
del halo_k2
#********************************************************************************
#Ph=L**3/N**6*np.abs(halo_k)**2
#W=Ph/(Ph+3.3*10**3)  #wiener filter
del halo_x
bias=np.sqrt(2.6)
halo_k=halo_k*W
########################## smooth and window function###########################
#k=(x[:,None,None]**2.+x[None,:,None]**2.+x[None,None,:]**2.)**(1./2.)
#window_k = np.sinc( 1./N* x[:,None,None]) * np.sinc( 1./N * x[None,:,None]) * np.sinc( 1./N * x[None,None,:])
halo_k=halo_k*(np.exp(-0.5*(Kf*Kf)*k*k*sigma**2))/window_k
del k
Pk_h=L**3/N**6*np.abs(halo_k)**2
deltag=np.fft.ifftn(halo_k).real
del halo_k

################################################################################
Tide.SaveDataHdf5(Pk_h,Outputfilename+'0.000halo00_Pk_halo.hdf5')
################################################################################
deltag=(deltag-1)/bias+1
deltag[deltag>0]=np.log(deltag[deltag>0])
delta_gx,delta_gy=Tide.DeltagW(deltag)
del deltag
gamma1,gamma2=Tide.CalGamma(delta_gx,delta_gy)
del delta_gx
del delta_gy
kappa_3dx=Tide.CalKappa(gamma1,gamma2)
del gamma1
del gamma2
#######################################save data#########################################
Tide.SaveDataHdf5(kappa_3dx,Outputfilename+'0.000halo00_wkappa3d_x.hdf5')
Inputfilename='/home/zhm/ptides/data/den1024z0.000.dat'
delta_x=Tide.LoadData(filename=Inputfilename)
delta_k=np.fft.fftn(delta_x)
delta_k=delta_k/window_k
kappa_3dk=np.fft.fftn(kappa_3dx)
Pk_delta=L**3/N**6*np.abs(delta_k)**2
Pk_kappa=L**3/N**6*np.abs(kappa_3dk)**2
Pk_delta_kappa=(L**3/N**6*(delta_k.conjugate()*kappa_3dk+kappa_3dk.conjugate()*delta_k)/2).real

Tide.SaveDataHdf5(Pk_kappa,Outputfilename+'0.000halo00_Pk_kappa.hdf5')
Tide.SaveDataHdf5(Pk_delta,Outputfilename+'0.000halo00_Pk_delta.hdf5')
Tide.SaveDataHdf5(Pk_delta_kappa,Outputfilename+'0.000halo00_Pk_delta_kappa.hdf5')


