#!/usr/bin/env python
# coding=utf-8
'''
plot Wiener filter
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
def smooth(sigma):
    smooth_K=np.exp(-k**2*sigma**2/2.)**2
    return smooth_K
#========================================
def Plot_CC_Onebyone(path='',color='',linestyle='',label=''):
    k=np.loadtxt(path+'Pk_DD')[:,0]
    Pdd=np.loadtxt(path+'Pk_DD')[:,1]
    Phh=np.loadtxt(path+'Pk_HH')[:,1]
    Pw=np.loadtxt(path+'wiener_1d.txt')[:,1]
    wiener=Pw
    wiener*=smooth(1.0)
    #========================================
    plt.figure('wienerS')
    plt.plot(k,wiener,'%s%s'%(color,linestyle),label=label)

#======== plot ==========================
Plot_CC_Onebyone(path=PATH+DIRPATH[0],color='g',linestyle='.-',label='$W_f=b^{2}P_{\\delta}/(P_h+\\frac{1}{\\bar{n}}),\mathrm{\ scale-independent\ bias},\mathrm{smooth}\ 1.0$')
Plot_CC_Onebyone(path=PATH+DIRPATH[1],color='r',linestyle='.-',label='$W_f=b^{2}P_{\\delta}/(P_h+\\frac{1}{\\bar{n}}),\mathrm{\ scale-dependent\ bias},\mathrm{smooth}\ 1.0$')
Plot_CC_Onebyone(path=PATH+DIRPATH[2],color='b',linestyle='.-',label='$W_f=P_{h}/(P_h+\\frac{1}{\\bar{n}}),\mathrm{smooth}\ 1.0$')

plt.plot(k,smooth(1.0),'m-',label='smooth 1.0')  # smooth
plt.plot(k,smooth(1.25),'m--',label='smooth 1.25')  # smooth

#======== set ===========================
plt.legend(loc='lower left')
plt.xlabel('$k\ [h/\mathrm{Mpc}]$')
plt.ylabel('$\mathrm{Wiener\ filter}$')
plt.xlim([k.min()*0.9,k.max()*1.1])
plt.ylim([0.0,1.1])
plt.grid(axis='y')
plt.xscale('log')
plt.yticks(np.linspace(0,1.0,11))
#plt.show()
plt.savefig('/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/all_simulation/test_Wiener_bias_effect/wienerF_smooth_1.00.eps')
#plt.savefig('/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/all_simulation/test_Wiener_bias_effect/wienerF.eps')
