#!/usr/bin/env python
# coding=utf-8
import numpy as np
#gamma1=
#gamma2=
N=1024
L=1.2*10**3
nk=np.fft.fftfreq(N,1./N)
k=2*np.py/L*nk
kgamma1=np.fft.fftn(gamma1)
kgamma2=np.fft.fftn(gamma2)

