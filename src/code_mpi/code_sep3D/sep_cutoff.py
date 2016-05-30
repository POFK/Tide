#!/usr/bin/env python
# coding=utf-8
import numpy as np
import fftw3 as fftw
from parameter import *
print '=='*40
print 'cut off with k = %f' % CutOff
deltax=Tide.LoadDataOfhdf5(PathCutoff)   # input halo field
deltak=np.empty((N,N,N/2+1),dtype=np.complex128)
fft=fftw.Plan(inarray=deltax,outarray=deltak,direction='forward',nthreads=nthreads)
fftw.execute(fft)
fftw.destroy_plan(fft)
k=(fn[:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)**0.5
deltak[k<CutOff]=0+0j
ifft=fftw.Plan(inarray=deltak,outarray=deltax,direction='backward',nthreads=nthreads)
fftw.execute(ifft)
fftw.destroy_plan(ifft)
deltax/=N**3 
Tide.SaveDataHdf5(deltax,PathCutoffOut)


