#!/usr/bin/env python
# coding=utf-8
from parameter import *
import matplotlib.pyplot as plt
#======  load inf =======================
f=open(PathOfINF,'r')
INF=f.readlines()
for i in INF:
    if '#' in i:
        continue
    if 'NOISE' in i:
        NOISE = np.float(i.split('=')[1])
        print NOISE
    if 'nbar' in i:
        nbar = np.float(i.split('=')[1])
        print nbar
#========================================

DD=np.loadtxt(PathPlot1+'DD')
DK=np.loadtxt(PathPlot1+'DK')
KK=np.loadtxt(PathPlot1+'KK')
#DH=np.loadtxt(PathPlot1+'DH')
#HH=np.loadtxt(PathPlot1+'HH')
#HK=np.loadtxt(PathPlot1+'HK')
r=DK[:,1]/np.sqrt(DD[:,1]*KK[:,1])
print 'CC',r
kbin=DD[:,0]
np.savetxt(ResultDir+'kbin.txt',kbin)
np.savetxt(ResultDir+'r.txt',r)
#========================================
plt.figure('correlation coefficient')
#plt.title('correlation coefficient')
plt.semilogx(kbin,r,'r.-',label=dir[20:])
plt.xlabel('$\mathrm{k}\ [h/\mathrm{Mpc}]$')
plt.ylabel('$\mathrm{r}$')
plt.legend(loc='lower left')
#plt.xlim([0.005,0.37])
plt.xlim([0.005,DD[:,0].max()])
plt.ylim([0.,1.])
plt.grid(axis='y')
plt.yticks(np.linspace(0.,1.0,11))
#plt.show()
#plt.savefig(ResultDir+'CC.png')
plt.savefig(ResultDir+'CC.eps')
plt.clf()
plt.cla()
#========================================
plt.figure('Power spectrum')
#plt.title('PS')
plt.loglog(kbin,DD[:,1],'.-',label='$P_{\delta \delta}$')
plt.loglog(kbin,DK[:,1],'.-.',label='$P_{\delta \kappa}$')
plt.loglog(kbin,KK[:,1],'.-.',label='$P_{\kappa \kappa}$')
#plt.loglog(kbin,DH[:,1],'.-',label='$P_{\delta h}$')
#plt.loglog(kbin,HH[:,1]-NOISE,'.-',label='$P_{hh}$')
#plt.loglog(kbin,HK[:,1],'.-.',label='$P_{h\kappa}$')
plt.xlabel('$\mathrm{k}\ [h/\mathrm{Mpc}]$')
plt.ylabel('$\mathrm{P(k)}\ [\mathrm{Mpc}^{3}/h^{3}]$')
ymax=np.max([np.max(DD[:,1]),np.max(DK[:,1]),np.max(KK[:,1]),np.max(DH[:,1]),np.max(HH[:,1]),np.max(HK[:,1])])*1.1
plt.xlim([0.005,0.37])
plt.ylim([3,ymax])
plt.legend(loc='lower left')
#plt.show()
#plt.savefig(ResultDir+'PS.png')
plt.savefig(ResultDir+'PS.eps')
plt.clf()
plt.cla()
#========================================
plt.figure('Power spectrum in all range')
#plt.title('PS')
plt.loglog(kbin,DD[:,1],'.-',label='$P_{\delta \delta}$')
plt.loglog(kbin,DK[:,1],'.-.',label='$P_{\delta \kappa}$')
plt.loglog(kbin,KK[:,1],'.-.',label='$P_{\kappa \kappa}$')
#plt.loglog(kbin,DH[:,1],'.-',label='$P_{\delta h}$')
#plt.loglog(kbin,HH[:,1]-NOISE,'.-',label='$P_{hh}$')
#plt.loglog(kbin,HK[:,1],'.-.',label='$P_{h\kappa}$')
plt.xlabel('$\mathrm{k}\ [h/\mathrm{Mpc}]$')
plt.ylabel('$\mathrm{P(k)}\ [\mathrm{Mpc}^{3}/h^{3}]$')
plt.axhline(NOISE,color='red',linestyle='-.')
ymax=np.max([np.max(DD[:,1]),np.max(DK[:,1]),np.max(KK[:,1]),np.max(DH[:,1]),np.max(HH[:,1]),np.max(HK[:,1])])*1.1
plt.xlim([0.005,DD[:,0].max()])
plt.ylim([1,ymax])
plt.legend(loc='lower left')
#plt.show()
#plt.savefig(ResultDir+'PS.png')
plt.savefig(ResultDir+'PS_allK.eps')
plt.clf()
plt.cla()

