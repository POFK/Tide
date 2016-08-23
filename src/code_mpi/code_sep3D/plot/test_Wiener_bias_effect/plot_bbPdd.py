#!/usr/bin/env python
# coding=utf-8
'''
plot b^2*Pdd
'''
import matplotlib.pyplot as plt
import numpy as np
import sys

#========================================
PATH='/project/mtx/output/tides10/'
DIRPATH=['test_4.8_s1.25_Wpd_biasConstant/',
         'test_4.8_s1.25_Wpd_biasVariable/',
         'test_4.8_s1.25_Wph_biasConstant/']
N=len(DIRPATH)
k=np.loadtxt(PATH+DIRPATH[0]+'Pk_DD')[:,0]
n=np.loadtxt(PATH+DIRPATH[0]+'Pk_DD')[:,2]
bias_cut=9
#========================================
def Plot_wiener(path='',color='',linestyle='',label=''):
    k=np.loadtxt(path+'Pk_DD')[:,0]
    Pdd=np.loadtxt(path+'Pk_DD')[:,1]
    Phh=np.loadtxt(path+'Pk_HH')[:,1]
    Pdh=np.loadtxt(path+'Pk_DH')[:,1]
    bias=Pdh/Pdd
    b=(bias*n)[:bias_cut].sum()/n[:bias_cut].sum()
    wiener=b**2*Pdd/(Phh)
    bPdd=b**2*Pdd
    biasPdd=bias**2*Pdd
    #========================================
    plt.figure('wiener')
#   plt.plot(k,wiener,'%s%s'%(color,linestyle),label=label)
#   plt.plot(k,bias,'%s%s'%(color,linestyle),label=label)
    plt.plot(k,Pdd,'%s%s'%('r',linestyle),label='$P_{\delta \delta}$')
    plt.plot(k,Pdh,'%s%s'%('g',linestyle),label='$P_{\delta h}$')
    plt.plot(k,Phh-1./(4.8*10**-3),'%s%s'%('b',linestyle),label='$P_{hh}$')
    plt.plot(k,bPdd,'%s%s'%('k','.--'),label='$b_c^2P_{\delta \delta}$')
    plt.plot(k,biasPdd,'%s%s'%('k','.-.'),label='$b^2P_{\delta \delta}$')

#======== plot ==========================
Plot_wiener(path=PATH+DIRPATH[0],color='g',linestyle='.-',label='$W_f=b^{2}P_{\\delta}/(P_h+\\frac{1}{\\bar{n}}),\mathrm{with\ scale-independent\ bias}$')
#Plot_wiener(path=PATH+DIRPATH[1],color='r',linestyle='.-',label='$W_f=b^{2}P_{\\delta}/(P_h+\\frac{1}{\\bar{n}}),\mathrm{with\ scale-dependent\ bias}$')
#Plot_wiener(path=PATH+DIRPATH[2],color='b',linestyle='.-',label='$W_f=P_{h}/(P_h+\\frac{1}{\\bar{n}})$')

#======== set ===========================
plt.axhline(y=1./(4.8*10**-3),color='k',linestyle=":")
plt.legend(loc='lower left')
plt.xlabel('$k\ [h/\mathrm{Mpc}]$')
plt.ylabel('$\mathrm{Power\ Spectra}$ [$(\mathrm{Mpc}/h)^{3}$]',fontsize=18)
plt.xlim([k.min()*0.9,k.max()*1.1])
plt.ylim([20,3*10**4])
#plt.grid(axis='y')
plt.xscale('log')
plt.yscale('log')
#plt.yticks(np.linspace(0,1.0,11))
plt.show()
#plt.savefig('/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/all_simulation/test_Wiener_bias_effect/biasPdd.eps')
