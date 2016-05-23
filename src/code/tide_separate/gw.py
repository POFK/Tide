#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import Tide
from par import *
'''
calulate derivative of delta in x, y, z axis
'''
wk=Tide.Get_wk()
def gw(deltax,k):
    W=wk(k*Kf)
    deltak=Tide.fft3d(deltax,nthreads=nthreads)
    deltakw1=deltak*W*1j*Kf*(fn[:,None,None]+np.zeros_like(fn)[None,:,None]+np.zeros_like(fnc)[None,None,:])
    deltakw2=deltak*W*1j*Kf*(np.zeros_like(fn)[:,None,None]+fn[None,:,None]+np.zeros_like(fnc)[None,None,:])
    deltakw3=deltak*W*1j*Kf*(np.zeros_like(fn)[:,None,None]+np.zeros_like(fn)[None,:,None]+fnc[None,None,:])
    deltaxw1=Tide.ifft3d(deltakw1,nthreads=nthreads)
    deltaxw2=Tide.ifft3d(deltakw2,nthreads=nthreads)
    deltaxw3=Tide.ifft3d(deltakw3,nthreads=nthreads)
    deltaxw1/=N**3
    deltaxw2/=N**3
    deltaxw3/=N**3
    return deltaxw1,deltaxw2,deltaxw3

