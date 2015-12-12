#!/usr/bin/env python
# coding=utf-8
from TIDES import *
import matplotlib.pyplot as plt
data=Tide.LoadData()    
f=Tide.Get_fk()
Pk=Tide.PowerSpectrum(data)
x=np.fft.fftfreq(N,1./N)
k=np.sqrt(x[:,None,None]**2+x[None,:,None]**2+x[None,None,:]**2)
w=(f(k)/Pk)**0.5
print w.shape
plt.loglog(k,)

