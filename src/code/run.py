#!/usr/bin/env python
# coding=utf-8
import numpy as np
import h5py
import matplotlib.pyplot as plt
from par import *
from tide_separate import *
from pk import pk
from wiener_sn import WshotN as Ws
from smooth import smooth
from gw import gw

############################## load data #######################################
f=h5py.File(filename1,mode='r')
deltaxH=f['data'][:]
f.close()
f=h5py.File(filename2,mode='r')
deltaxD=f['data'][:]
f.close()
################################### pk #########################################
shotnoise=L**3/deltaxH.sum()
print 'n bar:',1/shotnoise
Window_top = np.sinc(1./N*fn[:,None,None])*np.sinc(1./N*fn[None,:,None])*np.sinc(1./N*fnc[None,None,:])
k=(fn[:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)**(1./2.)
pk_h=pk.pk(deltaxH,deltaxH)
############################## shot noise window ###############################
deltaxH=wiener_sn.WshotN(deltaxH,pk_h,shotnoise)
############################## smooth kernel ###################################
smoothx=smooth.smooth(deltaxH,k,Sigma=Sigma,window=Window_top)
##############################   dengW x y z ###################################
dengw1,dengw2,dengw3=gw.gw(smoothx,k)
############################## gamma 1 2 x y z #################################
gamma1=dengw1*dengw1-dengw2*dengw2
gamma2=2*dengw1*dengw2
gammax=2*dengw1*dengw3
gammay=2*dengw2*dengw3
gammaz=(2*dengw3*dengw3-dengw2*dengw2-dengw1*dengw1)/3
##############################   kappa 3d   ####################################
#========2d========

#========3d========

