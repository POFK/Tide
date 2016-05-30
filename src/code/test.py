#!/usr/bin/env python
# coding=utf-8
from tide_separate.par import *
@profile
def f():
    import numpy as np
    from TIDES import Tide
    import h5py
    import matplotlib.pyplot as plt
    import tide_separate.pk
    import tide_separate.wiener_sn
    import tide_separate.smooth
    import tide_separate.gw
    import tide_separate.kappa
    
    ############################### load data #######################################
    #f=h5py.File(path_halo,mode='r')
    #deltaxH=f['data'][:]
    #f.close()
    #f=h5py.File(path_delta,mode='r')
    #deltaxD=f['data'][:]
    #f.close()
    #################################### pk #########################################
    #shotnoise=L**3/deltaxH.sum()
    #deltaxH*=N**3/deltaxH.sum()
    #deltaxH=deltaxH.astype(np.float64)
    #print 'n bar:',1/shotnoise
    #Window_top = np.sinc(1./N*fn[:,None,None])*np.sinc(1./N*fn[None,:,None])*np.sinc(1./N*fnc[None,None,:])
    k=(fn[:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)**(1./2.)
    #pk_h=tide_separate.pk.pk(deltaxH,deltaxH,window=Window_top)
    #Tide.SaveDataHdf5(pk_h,path_out+'PK_Halo.hdf5')
    ############################### shot noise window ###############################
    #deltaxH=tide_separate.wiener_sn.WshotN(deltaxH,pk_h,shotnoise)
    #Tide.SaveDataHdf5(deltaxH,path_out+'HaloW.hdf5')
    #del pk_h
    ############################### smooth kernel ###################################
    #smoothx=tide_separate.smooth.smooth(deltaxH,k,Sigma=Sigma,window=Window_top)
    #Tide.SaveDataHdf5(smoothx,path_out+'smooth_%.2f.hdf5'%Sigma)
    #del deltaxH
    ###############################   dengW x y z ###################################
    f=h5py.File(path_out+'smooth_%.2f.hdf5'%Sigma,mode='r')
    smoothx=f['data'][...]
    smoothx=np.array(smoothx,dtype=np.float)
    f.close()
    dengw1,dengw2,dengw3=tide_separate.gw.gw(smoothx,k)
    Tide.SaveDataHdf5(dengw1,path_out+'dengw1.hdf5')
    Tide.SaveDataHdf5(dengw2,path_out+'dengw2.hdf5')
    Tide.SaveDataHdf5(dengw3,path_out+'dengw3.hdf5')
    del smoothx
    ############################## gamma 1 2 x y z #################################
    gamma1=dengw1*dengw1-dengw2*dengw2
    gamma2=2*dengw1*dengw2
    #gammax=2*dengw1*dengw3
    #gammay=2*dengw2*dengw3
    #gammaz=(2*dengw3*dengw3-dengw2*dengw2-dengw1*dengw1)/3
    
    Tide.SaveDataHdf5(gamma1,path_out+'gamma1.hdf5')
    Tide.SaveDataHdf5(gamma2,path_out+'gamma2.hdf5')
    #Tide.SaveDataHdf5(gammax,path_out+'gammax.hdf5')
    #Tide.SaveDataHdf5(gammay,path_out+'gammay.hdf5')
    #Tide.SaveDataHdf5(gammaz,path_out+'gammaz.hdf5')
    del dengw1
    del dengw2
    del dengw3
    ##############################   kappa unweitht ################################
    #========2d========
    k2d=tide_separate.kappa.kappa2d(gamma1,gamma2,k)
    #========3d========
    k3d=tide_separate.kappa.kappa3d(gamma1,gamma2,gammax,gammay,gammaz,k)
    
    Tide.SaveDataHdf5(k2d,path_out+'kappa2d.hdf5')
    
f()
