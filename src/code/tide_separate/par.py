#!/usr/bin/env python
# coding=utf-8

filename1=''
filename2=''

N=1024
L=1.2*10**3
H=L/N
Kf=2*np.pi/L
fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
fnc=np.arange(N/2+1)
Sigma=1.25
nthreads=8

