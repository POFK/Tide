#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
##========================================
#plt.figure('correlation coefficient')
##plt.title('correlation coefficient')
#plt.semilogx(kbin,r,'r.-',label=dir[20:])
#plt.xlabel('$\mathrm{k}\ [h/\mathrm{Mpc}]$')
#plt.ylabel('$\mathrm{r}$')
#plt.legend(loc='lower left')
#plt.xlim([0.005,0.37])
#plt.ylim([0.,1.])
#plt.grid(axis='y')
#plt.yticks(np.linspace(0.,1.0,11))
##plt.show()
##plt.savefig(ResultDir+'CC.png')
#plt.savefig(ResultDir+'CC.eps')
#plt.clf()
#plt.cla()
##========================================
PK=np.loadtxt('/home/mtx/github/Tide/src/lcdm_pk.dat')
path1='/project/mtx/output/tides10/0.0048_3D_NoGau_Wiener_Smooth0.10/'
path2='/project/mtx/output/tides10/test/'
DD=np.loadtxt(path1+'Pk_DD')
DH=np.loadtxt(path1+'Pk_DH')
HH=np.loadtxt(path1+'Pk_HH')
kbin=DD[:,0]
NOISE=1./(4.8*10**-3)
plt.figure('Power spectrum ngp')
#plt.title('PS')
plt.loglog(PK[:,0],PK[:,1],'m-',label='th')
plt.loglog(kbin,DD[:,1],'.-',label='$P_{\delta \delta}$')
#plt.loglog(kbin,DK[:,1],'.-.',label='$P_{\delta \kappa}$')
#plt.loglog(kbin,KK[:,1],'.-.',label='$P_{\kappa \kappa}$')
plt.loglog(kbin,DH[:,1],'.-',label='$P_{\delta h}$')
plt.loglog(kbin,HH[:,1]-NOISE,'.-',label='$P_{hh}$')
#plt.loglog(kbin,HK[:,1],'.-.',label='$P_{h\kappa}$')
plt.xlabel('$\mathrm{k}\ [h/\mathrm{Mpc}]$')
plt.ylabel('$\mathrm{P(k)}\ [\mathrm{Mpc}^{3}/h^{3}]$')
ymax=np.max([np.max(DD[:,1]),np.max(DH[:,1]),np.max(HH[:,1])])*1.1
plt.xlim([0.005,2.8])
plt.ylim([10,ymax])
plt.axhline(NOISE,color='black',linestyle='-.')
plt.legend(loc='lower left')
#plt.show()
#plt.savefig(ResultDir+'PS.png')
#plt.savefig(ResultDir+'PS.eps')
##========================================
DD=np.loadtxt(path2+'Pk_DD')
DH=np.loadtxt(path2+'Pk_DH')
HH=np.loadtxt(path2+'Pk_HH')
plt.figure('Power spectrum cic')
#plt.title('PS')
plt.loglog(kbin,DD[:,1],'.-',label='$P_{\delta \delta}$')
plt.loglog(PK[:,0],PK[:,1],'m-',label='th')
#plt.loglog(kbin,DK[:,1],'.-.',label='$P_{\delta \kappa}$')
#plt.loglog(kbin,KK[:,1],'.-.',label='$P_{\kappa \kappa}$')
plt.loglog(kbin,DH[:,1],'.-',label='$P_{\delta h}$')
plt.loglog(kbin,HH[:,1]-NOISE,'.-',label='$P_{hh}$')
#plt.loglog(kbin,HK[:,1],'.-.',label='$P_{h\kappa}$')
plt.xlabel('$\mathrm{k}\ [h/\mathrm{Mpc}]$')
plt.ylabel('$\mathrm{P(k)}\ [\mathrm{Mpc}^{3}/h^{3}]$')
ymax=np.max([np.max(DD[:,1]),np.max(DH[:,1]),np.max(HH[:,1])])*1.1
plt.axhline(NOISE,color='black',linestyle='-.')
plt.xlim([0.005,2.8])
plt.ylim([10,ymax])
plt.legend(loc='lower left')
plt.show()
#plt.savefig(ResultDir+'PS.png')
#plt.savefig(ResultDir+'PS.eps')
