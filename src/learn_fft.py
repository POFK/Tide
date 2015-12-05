#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt 
N=2000
L=3
a=np.linspace(0,L,N)
x=a
b=np.sin(156.25*x)  + 2*np.sin(234.375*x)
#freq=np.abs(freq)
b=b
freq=2*np.pi/L*np.fft.fftfreq(len(b),1./len(b))
fy=np.fft.fft(b)/len(b)
print fy[0]
P=np.abs(fy)**2
plt.plot(freq,P,'-o')
plt.show()
