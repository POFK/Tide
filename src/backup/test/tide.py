#!/usr/bin/env python
# coding=utf-8
import struct
import numpy as np
import matplotlib.pyplot as plt
####################################################
N = 1024
L = 1.2 * 10**3  # Mpc
H = L / 1024.
####################################################


class Tide():

    @classmethod
    def LoadData(self, filename='/home/mtx/data/tide/0.000den00.bin'):
        f = open(filename, 'rb')
        data = f.read()
        f.close()
        data = struct.unpack('1073741824f', data)
        data = np.array(data, dtype=np.float16)
        data = data.reshape((1024, 1024, 1024), order='F')
        return data

    @classmethod
    def GetX(self):
        x = np.arange(1024)
        for i in np.arange(1, 1024 / 2 + 1):
            x[1024 - i] = x[i]
        return x
#########################################################################
data = Tide.LoadData(filename='/home/zhm/tides01/0.000den00.bin')
x = np.fft.fftfreq(N,1./N)  # x: 0,1,2,...,512,511,...,2,1
delta_k = np.fft.fftn(data)
del data
window_k = np.sinc(1. / N * x[:,None,None]) * np.sinc(1. / N * x[None,:,None]) * np.sinc(1. / N * x[None,None,:])
Pk = (np.abs(delta_k) / window_k)**2
del window_k
del delta_k
# Pk=np.abs(delta_k)**2.
#########################################################################
kn = ((x**2)[:, None, None] +
      (x**2)[None, :, None] +
      (x**2)[None, None, :])**(1. / 2.)
kn_max = 512
kn_min = 1
x = np.linspace(np.log10(kn_min), np.log10(kn_max), 20, endpoint=False)
dx = x[1] - x[0]
P = []
k = []
Ln = []
for i in range(20):
    bool = ((10**x[i]) <= kn) * (kn < (10**(x[i] + dx)))
    P.append(Pk[bool].sum() / float(len(kn[bool])))
    k.append(kn[bool].sum() / float(len(kn[bool])))
    Ln.append(len(kn[bool]))
P = L**3. / (1024.**6) * np.array(P)
k = np.array(k) * 2 * np.pi / L
######### save data with no log###############
np.savetxt('PS_data', np.c_[k, P, Ln])
