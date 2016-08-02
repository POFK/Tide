#!/usr/bin/env python
# coding=utf-8
from sep_wienerPh import WienerF
import matplotlib.pyplot as plt
import numpy as np
N=1024
L=1200
Kf=np.pi*2./L
fn=np.fft.fftfreq(N,1./N)  #x: 0,1,2,...,512,-511,-510,...,-2,-1
fnc=np.arange(N/2+1)
Wienerf,bias,k_min,k_max=WienerF('/project/mtx/output/tides10/test/',noise=208.172029)
k=(fn[:,None,None]**2.+fn[None,:,None]**2.+fnc[None,None,:]**2)**(1./2.)
logk=np.log10(Kf*k)
logk[(Kf*k)<k_min]=np.log10(k_min)
logk[(Kf*k)>k_max]=np.log10(k_max)
shape=logk.shape
Wiener=Wienerf(logk.reshape(-1))
Wiener=Wiener.reshape(shape)
Wiener[(Kf*k)<k_min]=Wienerf(np.log10(k_min))
Wiener[(Kf*k)>k_max]=Wienerf(np.log10(k_max))
bin=(np.linspace(0,np.log10(512),20,endpoint=False))
dbin=bin[1]-bin[0]
bin=np.hstack((bin,bin[-1]+dbin))
bin=10**bin
n=np.histogram(k,bins=bin)[0]
W=np.histogram(k,bins=bin,weights=Wiener)[0]/n
k_bin=Kf*np.histogram(k,bins=bin,weights=k)[0]/n
np.savetxt('./data/wiener.txt',np.c_[k_bin,W])
plt.semilogx(k_bin,W,'go-.',label='wiener')
plt.ylim([0,1])
plt.legend()
plt.show()

