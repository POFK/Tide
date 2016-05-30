#!/usr/bin/env python
# coding=utf-8
from parameter import *
import matplotlib.pyplot as plt
DD=np.loadtxt(PathPlot1+'DD')
DK=np.loadtxt(PathPlot1+'DK')
KK=np.loadtxt(PathPlot1+'KK')
DH=np.loadtxt(PathPlot1+'DH')
HH=np.loadtxt(PathPlot1+'HH')
HK=np.loadtxt(PathPlot1+'HK')
r=DK[:,1]/np.sqrt(DD[:,1]*KK[:,1])
kbin=DD[:,0]
#========================================
plt.figure('correlation coefficient')
plt.title('correlation coefficient')
plt.semilogx(kbin,r,'r.-',label=dir)
plt.xlabel('k $(h/\mathrm{Mpc})$')
plt.ylabel('r')
plt.legend()
plt.savefig(ResultDir+'CC.png')
plt.clf()
#========================================
plt.figure('Power spectrum')
plt.title('PS')
plt.loglog(kbin,DD[:,1],'.-',label='$P_{\delta \delta}$')
plt.loglog(kbin,DK[:,1],'.-',label='$P_{\delta \kappa}$')
plt.loglog(kbin,KK[:,1],'.-',label='$P_{\kappa \kappa}$')
plt.loglog(kbin,DH[:,1],'.-',label='$P_{\delta h}$')
plt.loglog(kbin,HH[:,1],'.-',label='$P_{hh}$')
plt.loglog(kbin,HK[:,1],'.-',label='$P_{h\kappa}$')
plt.xlabel('k $(h/\mathrm{Mpc})$')
plt.ylabel('P(k) $(Mpc^{3}/h^{3})$')
plt.legend()
plt.savefig(ResultDir+'PS.png')
plt.clf()
#========================================
