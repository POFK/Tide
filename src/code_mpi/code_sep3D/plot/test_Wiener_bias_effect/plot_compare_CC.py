#!/usr/bin/env python
# coding=utf-8
'''
compare correlation cofficient in different directory
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
#========================================
def Plot_CC_Onebyone(path='',color='',linestyle='',label=''):
    k=np.loadtxt(path+'Pk_DD')[:,0]
    Pdd=np.loadtxt(path+'Pk_DD')[:,1]
    Pkk=np.loadtxt(path+'Pk_KK')[:,1]
    Pdk=np.loadtxt(path+'Pk_DK')[:,1]
    r=Pdk/np.sqrt(Pdd*Pkk)
    #========================================
    plt.figure('correlation coefficient')
    plt.plot(k,r,'%s%s'%(color,linestyle),label=label)

#======== plot ==========================
Plot_CC_Onebyone(path=PATH+DIRPATH[0],color='g',linestyle='.-',label='$W_f=b^{2}P_{\\delta}/(P_h+\\frac{1}{\\bar{n}}),\mathrm{\ scale-independent\ bias}$')
Plot_CC_Onebyone(path=PATH+DIRPATH[1],color='r',linestyle='.-',label='$W_f=b^{2}P_{\\delta}/(P_h+\\frac{1}{\\bar{n}}),\mathrm{\ scale-dependent\ bias}$')
Plot_CC_Onebyone(path=PATH+DIRPATH[2],color='b',linestyle='.-',label='$W_f=P_{h}/(P_h+\\frac{1}{\\bar{n}})$')
#Plot_CC_Onebyone(path=PATH+'test_4.8_s0.8_Wpd_biasConstant/',color='g',linestyle='.--',label='$W_f=b^{2}P_{\\delta}/(P_h+\\frac{1}{\\bar{n}}),\mathrm{\ scale-independent\ bias}\_0.8$')
#Plot_CC_Onebyone(path=PATH+'test_4.8_s0.8_Wpd_biasVariable/',color='r',linestyle='.--',label='$W_f=b^{2}P_{\\delta}/(P_h+\\frac{1}{\\bar{n}}),\mathrm{\ scale-dependent\ bias}\_0.8$')
#Plot_CC_Onebyone(path=PATH+'test_4.8_s0.8_Wph_biasConstant/',color='b',linestyle='.--',label='$W_f=b^{2}P_{\\delta}/(P_h+\\frac{1}{\\bar{n}}),0.8$')
#Plot_CC_Onebyone(path=PATH+'test_4.8_s1.0_Wpd_biasConstant/',color='m',linestyle='.-',label='$W_f=b^{2}P_{\\delta}/(P_h+\\frac{1}{\\bar{n}}),\mathrm{\ scale-independent\ bias}\_1.0$')
#======== set ===========================
plt.legend(loc='lower left')
plt.xlabel('$k\ [h/\mathrm{Mpc}]$')
plt.ylabel('$\mathrm{correlation\ coefficient}$')
plt.xlim([k.min()*0.9,0.7])
plt.ylim([0.0,1.0])
plt.grid(axis='y')
plt.xscale('log')
plt.yticks(np.linspace(0,1.0,11))
plt.show()
#plt.savefig('/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/all_simulation/test_Wiener_bias_effect/CC_onebyone.eps')
