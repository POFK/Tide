#!/usr/bin/env python
# coding=utf-8
'''for calulate the wiener of shot noise
W=P_h/(P_h+1/n_bar)
'''
from TIDES import Tide
from par import *
def WshotN(deltax,pk,n):
    '''n is shot noise '''
    deltak=Tide.fft3d(deltax,n=nthreads)
    window=pk/(pk+n)
    deltak*=window
    deltax=Tide.ifft3d(deltak,n=nthreads)
    deltax/=N**3
    return deltax
