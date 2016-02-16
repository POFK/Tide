#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import *
import sys
name=sys.argv[1]
name2=sys.argv[2]
sigma=3.0
Inputfilename='/home/zhm/'+name+'/0.000halo00.bin'
Outputfilename='/home/mtx/data/tide/outdata/'+name+'/halo/'+name2+'/'
print Inputfilename
print Outputfilename
########################################load data########################################
delta_x=Tide.LoadData(filename=Inputfilename)
#####################add later of wiener filter and smooth######################
Kf=2*np.pi/(1.2*10**3)
x = np.fft.fftfreq(N,1./N)  # x: 0,1,2,...,512,-511,...,-2,-1
halo_k=np.fft.fftn(delta_x)
Ph=L**3/N**6*np.abs(halo_k)**2
Ph=Ph/(Ph+3.3*10**3)
k=(x[:,None,None]**2.+x[None,:,None]**2.+x[None,None,:]**2.)**(1./2.)
window_k = np.sinc( 1./N* x[:,None,None]) * np.sinc( 1./N * x[None,:,None]) * np.sinc( 1./N * x[None,None,:])
Ph_k=Ph*((np.exp(-0.5*(Kf*Kf)*k*k*sigma**2))/window_k)**2
deltag=np.fft.ifftn(Ph_k).real

################################################################################
Tide.SaveDataHdf5(Ph_k,Outputfilename+'0.000halo00_Pk_halo.hdf5')
################################################################################
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
#Pk_delta=L**3/N**6*Tide.AutoPowerSpectrum(data=delta_x,window=True)
#Pk_kappa=L**3/N**6*Tide.AutoPowerSpectrum(data=kappa_3dx,window=False)
#Pk_delta_kappa=L**3/N**6*Tide.CrossPowerSpectrum(data1=delta_x,data2=kappa_3dx)
#
#Tide.SaveDataHdf5(Pk_kappa,Outputfilename+'0.000halo00_Pk_kappa.hdf5')
#Tide.SaveDataHdf5(Pk_delta,Outputfilename+'0.000halo00_Pk_delta.hdf5')
#Tide.SaveDataHdf5(Pk_delta_kappa,Outputfilename+'0.000halo00_Pk_delta_kappa.hdf5')

Inputfilename='/home/zhm/'+name+'/0.000den00.bin'
delta_x=Tide.LoadData(filename=Inputfilename)
Pk_delta=L**3/N**6*Tide.AutoPowerSpectrum(data=delta_x,window=True)
Pk_kappa=L**3/N**6*Tide.AutoPowerSpectrum(data=kappa_3dx,window=False)
Pk_delta_kappa=L**3/N**6*Tide.CrossPowerSpectrum(data1=delta_x,data2=kappa_3dx)

Tide.SaveDataHdf5(Pk_kappa,Outputfilename+'0.000halo00_Pk_kappa.hdf5')
Tide.SaveDataHdf5(Pk_delta,Outputfilename+'0.000halo00_Pk_delta.hdf5')
Tide.SaveDataHdf5(Pk_delta_kappa,Outputfilename+'0.000halo00_Pk_delta_kappa.hdf5')


