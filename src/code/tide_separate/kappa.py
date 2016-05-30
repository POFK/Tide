#!/usr/bin/env python
# coding=utf-8
from TIDES import Tide
import numpy as np
from par import *

k1=Kf*(fn[:,None,None]+np.zeros_like(fn)[None,:,None]+np.zeros_like(fnc)[None,None,:])
k2=Kf*(np.zeros_like(fn)[:,None,None]+fn[None,:,None]+np.zeros_like(fnc)[None,None,:])
k3=Kf*(np.zeros_like(fn)[:,None,None]+np.zeros_like(fn)[None,:,None]+fnc[None,None,:])

def kappa3d(g1,g2,gx,gy,gz,k):
    g1k=Tide.fft3d(g1,n=nthreads)
    g2k=Tide.fft3d(g2,n=nthreads)
    gxk=Tide.fft3d(gx,n=nthreads)
    gyk=Tide.fft3d(gy,n=nthreads)
    gzk=Tide.fft3d(gz,n=nthreads)
    k*=Kf
    kappak=1./(k**2)*((k1**2-k2**2)*g1k+2*k1*k2*g2k+2*k1*k3*gxk+2*k2*k3*gyk+(2*k3**2-k1**2-k2**2)*gzk)
    kappax=Tide.ifft3d(kappak,n=nthreads)
    return kappax
def kappa2d(g1,g2,k):
    g1k=Tide.fft3d(g1,n=nthreads)
    g2k=Tide.fft3d(g2,n=nthreads)
    k*=Kf
    kappak=2*k**2
    kappak/=3*(k1**2+k2**2)
    kappak*=((k1**2-k2**2)*g1k+2*k1*k2*g2k)
    kappax=Tide.ifft3d(kappak,n=nthreads)
    return kappax
#def wkkappa():
