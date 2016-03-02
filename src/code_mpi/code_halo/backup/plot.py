#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from parameter import Outfile
name='halo1.25_rsd'
noise3=(0.6*10**3)**3/1000000.
print noise3
dd=np.loadtxt(Outfile+'PS_DD')
dk=np.loadtxt(Outfile+'PS_DK')
kk=np.loadtxt(Outfile+'PS_KK')
#halo=np.loadtxt('/home/mtx/data/tide/haloes2/outdata/halo_0024_r1/PS_haloDD')
halo=np.loadtxt(Outfile+'PS_haloDD')
plt.figure('Power Spectrum')
n=np.ones_like(kk[:,1])
plt.loglog(dd[:,0],dd[:,1],'b.-',label='P_DD')
plt.loglog(halo[:,0],halo[:,1],'m.-',label='P_halo')
plt.loglog(dk[:,0],dk[:,1],'g.-',label='P_DK')
plt.loglog(kk[:,0],kk[:,1],'r.-',label='P_KK')
plt.loglog(kk[:,0],n*noise3,'k-.',alpha=0.8,label='noise')
plt.title('Power Spectrum')
plt.xlabel('k $(h/Mpc)$')
plt.ylabel('P(k) $(Mpc^{3}/h^{3})$')
plt.legend()
plt.ylim(10**1,6*10**4)
#plt.xlim([9*10**-3,1])
plt.savefig(name+'PS.eps')

plt.figure('correlation coefficient')
plt.title('correlation coefficient')
plt.semilogx(kk[:,0],dk[:,1]/np.sqrt(dd[:,1]*kk[:,1]),'.-')
plt.xlabel('k $(h/Mpc)$')
plt.ylabel('r')
##plt.xlim([9*10**-3,1])
plt.yticks(np.linspace(0,1,11))
plt.ylim([0,1.0])
plt.grid(axis='y')
#plt.savefig(name+'CC.eps')
plt.show()
print dk[:,1]/np.sqrt(dd[:,1]*kk[:,1])
