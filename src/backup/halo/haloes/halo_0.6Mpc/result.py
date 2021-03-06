#!/usr/bin/env python
# coding=utf-8
import numpy as np
from Gau import Gau
from TIDES import *
import sys
sigma=1.25
#Inputfilename='/home/zhm/tides20/0.000halo.bin'
Inputfilename='/home/zhm/tides20/0.000halo_rsd3.bin'
Outputfilename='/home/mtx/data/tide/halo_new/outdata/'
print Inputfilename
print Outputfilename
########################################load data########################################
halo_x=Tide.LoadData(filename=Inputfilename)
#####################add later of wiener filter and smooth######################
Kf=2*np.pi/(L)
x = np.fft.fftfreq(N,1./N)  # x: 0,1,2,...,512,-511,...,-2,-1
sum=halo_x.sum()
print sum
halo_x=(N**3)/sum*halo_x
halo_k=np.fft.fftn(halo_x)
#********************************************************************************
k=(x[:,None,None]**2.+x[None,:,None]**2.+x[None,None,:]**2.)**(1./2.)
window_k = np.sinc( 1./N* x[:,None,None]) * np.sinc( 1./N * x[None,:,None]) * np.sinc( 1./N * x[None,None,:])

Ph=L**3/N**6*np.abs(halo_k)**2
Tide.SaveDataHdf5(Ph,Outputfilename+'0.000halo00_Pk_halo.hdf5')
Ph=Ph*(np.exp(-0.5*(Kf*Kf)*k*k*sigma**2)/window_k)**2
W=Ph/(Ph+(L**3)/sum)  #wiener filter
#********************************************************************************
del halo_x
halo_k=halo_k*W
########################## smooth and window function###########################
#k=(x[:,None,None]**2.+x[None,:,None]**2.+x[None,None,:]**2.)**(1./2.)
#window_k = np.sinc( 1./N* x[:,None,None]) * np.sinc( 1./N * x[None,:,None]) * np.sinc( 1./N * x[None,None,:])

halo_k=halo_k*(np.exp(-0.5*(Kf*Kf)*k*k*sigma**2))/window_k
deltag=np.fft.ifftn(halo_k).real
#Tide.SaveDataHdf5(deltag,Outputfilename+'0.000halo00_s1.25.hdf5')

del k
################################################################################
del halo_k
################################################################################
#deltag=(deltag-1)*bias+1
#deltag[deltag>0]=np.log(deltag[deltag>0])
deltag=Gau(data=deltag,output=Outputfilename+'halo_Gau.hdf5')
print 'Gau... ok'
delta_gx,delta_gy=Tide.DeltagW(deltag)
#Tide.SaveDataHdf5(delta_gx,Outputfilename+'0.000halo00_dgx1.25.hdf5')
del deltag
gamma1,gamma2=Tide.CalGamma(delta_gx,delta_gy)
#Tide.SaveDataHdf5(gamma1,Outputfilename+'0.000halo00_gamma11.25.hdf5')
del delta_gx
del delta_gy
kappa_3dx=Tide.CalKappa(gamma1,gamma2)
del gamma1
del gamma2
#######################################save data#########################################
Tide.SaveDataHdf5(kappa_3dx,Outputfilename+'0.000halo00_wkappa3d_x.hdf5')
Inputfilename='/home/zhm/tides20/0.000delta.bin'
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
