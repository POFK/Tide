#!/usr/bin/env python
# coding=utf-8
'To compare the effect of wiener filter and smooth kernel.'

import numpy as np
import matplotlib.pyplot as plt

dir=[
'../result/tides10/'+'0.0012_3D_NoGau_Wiener_noSmooth',
'../result/tides10/'+'0.0024_3D_NoGau_Wiener_noSmooth',
'../result/tides10/'+'0.0048_3D_NoGau_Wiener_noSmooth',
'../result/tides10/'+'0.0012_3D_NoGau_s1.25_NoWiener',
'../result/tides10/'+'0.0024_3D_NoGau_s1.25_NoWiener',
'../result/tides10/'+'0.0048_3D_NoGau_s1.25_NoWiener']
filename='/Pk_smooth_wiener_1d.txt'

def plot_Pk(path='',fmt='',label='',linewidth=None):
    data=np.loadtxt(path)[:-1,:]
    k=data[:,0]
    pk=data[:,1]
    plt.loglog(k,pk,fmt,label=label,linewidth=linewidth)

plt.figure('compare_wiener_smooth.eps')
plot_Pk(path='../result/tides10/'+'PK_DD',fmt='k.-',label='Pk_DD',linewidth=2)
plot_Pk(path=dir[0]+filename,fmt='b.-',label=dir[0],linewidth=1)
plot_Pk(path=dir[1]+filename,fmt='r.-',label=dir[1],linewidth=1)
plot_Pk(path=dir[2]+filename,fmt='g.-',label=dir[2],linewidth=1)
plot_Pk(path=dir[3]+filename,fmt='b.--',label=dir[3],linewidth=1)
plot_Pk(path=dir[4]+filename,fmt='r.--',label=dir[4],linewidth=1)
plot_Pk(path=dir[5]+filename,fmt='g.--',label=dir[5],linewidth=1)

plot_Pk(path='../result/tides10/'+'0.0012_PK_HH',fmt='b.-',label='Pk_halo 0.0012',linewidth=2)
plot_Pk(path='../result/tides10/'+'0.0024_PK_HH',fmt='r.-',label='Pk_halo 0.0024',linewidth=2)
plot_Pk(path='../result/tides10/'+'0.0048_PK_HH',fmt='g.-',label='Pk_halo 0.0048',linewidth=2)

plt.axhline(1./(1.2*10**-3),color='blue',linestyle='-.')
plt.axhline(1./(2.4*10**-3),color='red',linestyle='-.')
plt.axhline(1./(4.8*10**-3),color='green',linestyle='-.')
plt.legend(loc='lower left')
plt.show()

