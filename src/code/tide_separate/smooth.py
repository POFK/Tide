#!/usr/bin/env python
# coding=utf-8
'''smoothing kernel with a Gaussian function'''
from TIDES import Tide
from par import *

def smooth(deltax,k,Sigma=Sigma,window==None):
    deltak=Tide.fft3d(deltax,nthreads=nthreads)
    smooth_k=deltak*np.exp(-0.5*Kf*Kf*k*k*Sigma**2)
    if window!= None:
        deltak/=window
    deltak*=smooth_k
    deltax=Tide.ifft3d(deltak,nthreads=nthreads)
    deltax/=N**3
    return deltax
