#!/usr/bin/env python
# coding=utf-8
'''
compare correlation cofficient in different directory one by one
'''
import matplotlib.pyplot as plt
import numpy as np
import sys

#========================================
PATH='/project/mtx/output/tides10/'
#DIRPATH=['massbin4_0.0003_m1/',
#        'massbin4_0.0003_m2/',
#        'massbin4_0.0003_m3/',
#        'massbin4_0.0003_m4/']
#DIRPATH=[
#        'massbin10_0.0003_combine_wienerKindependent_bE1_noWiener/',
#        'test_0.000halo_0.0003_cic_wienerConst_s1.0/',
#        'massbin4_0.0024_combine_bE1/',
#        'CIC_0.0024_3D_NoGau_s1.0_Wiener/',
#        'massbin4_0.0003_combine_wienerKindependent_bE1_noWiener/'
#        ]
DIRPATH=[
        'test_0.000halo_0.0003_cic_wienerConst_s1.0/',
#       'massbin10_0.0003_combine_wienerKindependent_bE1_noWiener/',
#       'massbin4_0.0024_combine_bE1/',
#       'CIC_0.0024_3D_NoGau_s1.0_Wiener/',
#       'massbin4_0.0003_combine_wienerKindependent_bE1_noWiener/'
        'massbin2_0.0003_combine_diffW/',
        'massbin2_0.0003_combine_cross/',
        'massbin2_0.0003_m1/',
        'massbin2_0.0003_m2/'
        ]



N=len(DIRPATH)
k=np.loadtxt(PATH+DIRPATH[0]+'Pk_DD')[:,0]
noise=1./0.0003*4
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
Plot_CC_Onebyone(path=PATH+DIRPATH[0],color='r',linestyle='.-',label='$0.0003$')
Plot_CC_Onebyone(path=PATH+DIRPATH[1],color='k',linestyle='.-',label='$\kappa_a+\kappa_b+2\kappa_{ab}$')
Plot_CC_Onebyone(path=PATH+DIRPATH[2],color='b',linestyle='*--',label='$\kappa_{ab}$')
Plot_CC_Onebyone(path=PATH+DIRPATH[3],color='m',linestyle='.--',label='$\kappa_a$')
Plot_CC_Onebyone(path=PATH+DIRPATH[4],color='g',linestyle='.--',label='$\kappa_b$')

#======== set ===========================
plt.legend(loc='upper right')
plt.xlabel('$k\ [h/\mathrm{Mpc}]$')
plt.ylabel('$\mathrm{correlation\ coefficient}$')
#plt.xlim([k.min()*0.9,k.max()*1.1])
plt.xlim([k.min()*0.9,0.7])
plt.ylim([0.0,1.0])
plt.grid(axis='y')
plt.xscale('log')
plt.yticks(np.linspace(0,1.0,11))
#plt.show()
OUTDIR='/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/eps/'
plt.savefig(OUTDIR+'high_order.eps')

