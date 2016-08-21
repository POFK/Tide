#!/usr/bin/env python
# coding=utf-8
'''
plot 2D bias
'''
import numpy as np
import matplotlib.pyplot as plt
bias=np.zeros((10,10))
DIR=['tides10','tides11','tides12','tides13','tides14','tides15','tides16','tides17','tides18','tides19']
Num=0.0024
bias_factor={  #  the factor of 1/(b0^2*Q)
        '0.0048': 1./(0.838964**2*1.262303),
        '0.0036': 1./(0.889876**2*0.963644),
        '0.0024': 1./(0.964854**2*0.649769),
        '0.0012': 1./(1.110380**2*0.325127),
        }

for d in DIR:
    path='/project/mtx/output/'+d+'/CIC_0.0024_3D_NoGau_s1.0_Wiener/result_b'
    bias+=np.loadtxt(path)
bias/=10
bias*=bias_factor[str(Num)]
bin=np.loadtxt('/project/mtx/output/'+d+'/CIC_0.0024_3D_NoGau_s1.0_Wiener/k_bin')
bin[0]=1
bin*=np.pi*2/1200
kx=bin[:8]
ky=bin[:8]
cmap = plt.get_cmap('Blues')
im = plt.pcolormesh(kx,ky,bias[:7,:7],cmap=cmap,vmax=.125,vmin=0.04)
#im = plt.pcolormesh(kx,ky,bias[:7,:7],cmap=cmap)#,vmax=.13,vmin=0.04)
#plt.colorbar(ticks=[0.0,0.025,0.075,0.10,0.125])
plt.colorbar()
plt.axis([kx.min(), kx.max(), ky.min(), ky.max()])
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$\mathbf{k}_{\perp}\ [h/\mathrm{Mpc}]$',fontsize='large')
plt.ylabel('$\mathbf{k}_{\parallel}\ [h/\mathrm{Mpc}]$',fontsize='large')
#plt.grid(True)
#plt.title('bias',fontsize='large')
OUTDIR='/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/eps/'
plt.savefig(OUTDIR+'recon_bias_2D.eps')
#plt.show()

