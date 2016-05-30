#!/usr/bin/env python
# coding=utf-8
'''
calculate power spectrum
'''
from TIDES import Tide
from par import *

def pk(deltax1,deltax2,window=None):
    deltak1=Tide.fft3d(deltax1,nthreads)
    deltak2=Tide.fft3d(deltax2,nthreads)
    if window!=None:
        deltak1/=window
        deltak2/=window
        print 'pk is added a sinc window'
    Pk=((deltak1.conjugate()*deltak2+deltak2.conjugate()*deltak1)/2.).real
    Pk*=(L**3/N**6)
    return Pk
