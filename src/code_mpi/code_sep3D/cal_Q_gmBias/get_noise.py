#!/usr/bin/env python
# coding=utf-8
import sys
import numpy as np
import matplotlib.pyplot as plt
OUTDIR='/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/eps/'
bias_cut=6
path=[
##   'tides10/CIC_0.0048_3D_NoGau_s1.0_Wiener/',
##   'tides10/CIC_0.0036_3D_NoGau_s1.0_Wiener/',
##   'tides10/CIC_0.0024_3D_NoGau_s1.0_Wiener/',
##   'tides10/CIC_0.0012_3D_NoGau_s1.0_Wiener/',
     'tides10/test_0.000halo_0.0003_cic_wienerConst_s1.0/',
     'tides10/massbin10_0.0003_m1/',
     'tides10/massbin10_0.0003_m2/',
     'tides10/massbin10_0.0003_m3/',
     'tides10/massbin10_0.0003_m4/',
     'tides10/massbin10_0.0003_m5/',
     'tides10/massbin10_0.0003_m6/',
     'tides10/massbin10_0.0003_m7/',
     'tides10/massbin10_0.0003_m8/',
     'tides10/massbin10_0.0003_m9/',
     'tides10/massbin10_0.0003_m10/'
     ]

#path=[
#    'tides10/test_0.000halo_0.0003_cic_wienerConst_s1.0/',
#    'tides10/massbin10_0.0003_combine_wienerKindependent_bE0_noWiener/',
#    'tides10/massbin10_0.0003_combine_wienerKindependent_bE1_noWiener/',
#    'tides10/massbin10_0.0003_combine_wienerKindependent_bE2_noWiener/',
#    'tides10/massbin4_0.0003_combine_wienerKindependent_bE1_noWiener/',
#    'tides10/massbin4_0.0003_combine_wienerKindependent_bE1_noWiener2/'
#    ]

num=6
#num_den=['0.0048','0.0036','0.0024','0.0012']
num_den=['0.0003','bin1','bin2','bin3','bin4','bin5','bin6','bin7','bin8','bin9','bin10']
#num_den=path
Color=['k','r','g','b','m','y','r','g','b','m','y']
#Lsty=['.-','.-','.-','.-','.-','.-','.--','.--','.--','.--','.--']
Lsty=['.-','.-','.-','.-','.-','.-','.--','.--','.--','.--','.--']
def f(file_path,label,color,lsty):
    PATH='/project/mtx/output/'+file_path
    print PATH
    Phh=np.loadtxt(PATH+'Pk_HH')
    Pdh=np.loadtxt(PATH+'Pk_DH')
    Pdd=np.loadtxt(PATH+'Pk_DD')
    n=Pdh[:,2]
    bias=Pdh[:,1]/Pdd[:,1]
    b=(bias*n)[:bias_cut].sum()/n[:bias_cut].sum()
#   Pn=(Phh[:,1]-bias**2*Pdd[:,1])/(bias**2*Pdd[:,1])
    Pn=(Phh[:,1]-bias**2*Pdd[:,1])
    plt.plot(Pdh[:,0],Pn,'%s%s'%(color,lsty),label=label)
    return Pdh[:,0]

#plt.figure('noise')
#plt.title('noise')
for i in np.arange(len(path)):
    k=f(path[i],num_den[i],Color[i],Lsty[i])

plt.axhline(y=1./0.0003*10,linestyle='-.')
plt.axhline(y=1./0.0003,linestyle='-.')
plt.xlim([k[0]*0.9,k[-1]*1.1])
#plt.ylim([5*10**-2,2*10**2])
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='upper left',ncol=5)

#plt.subplot(2,1,2)
#for i in np.arange(len(path)):
#    k=f(path[i],num_den[i])
#
#plt.xlim([k[0]*0.9,k[-1]*1.1])
#plt.ylim([0.05,3])
#plt.ylabel('$(P_{h}-b^2P_{\delta})/b^2P_{\delta}$')
#plt.xlabel('$k$')
#plt.xscale('log')
#plt.yscale('log')
#plt.legend(loc='upper left',ncol=2)
#plt.grid()

plt.xlabel('$k\ [h/\mathrm{Mpc}]$',fontsize=18)
plt.ylabel('$P_{hh}-b^2P_{\delta\delta}$',fontsize=18)
#plt.ylabel('$(P_{hh}-b^2P_{\delta\delta})/b^2P_{\delta\delta}$',fontsize=18)
#plt.show()
#plt.savefig(OUTDIR+'bw_Sim_Noise_b2Pd_0.0003_10mbin.eps')
plt.savefig(OUTDIR+'bw_Sim_Noise_Pn_0.0003_10mbin.eps')
