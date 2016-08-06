#!/usr/bin/env python
# coding=utf-8
import sys
import numpy as np
import matplotlib.pyplot as plt
bias_cut=9
path=[
#   'tides10/CIC_0.0048_3D_NoGau_s1.0_Wiener/',
#   'tides10/CIC_0.0036_3D_NoGau_s1.0_Wiener/',
    'tides10/CIC_0.0024_3D_NoGau_s1.0_Wiener/',
#   'tides10/CIC_0.0012_3D_NoGau_s1.0_Wiener/',
    'tides10/massbin4biasWeight_halo_cic_0.0012_1/',
    'tides10/massbin4biasWeight_halo_cic_0.0012_2/',
    'tides10/massbin4biasWeight_halo_cic_0.0012_2massbin_m1/',
    'tides10/massbin4biasWeight_halo_cic_0.0012_2massbin_m2/',
    'tides10/massbin4biasWeight_halo_cic_0.0012_2massbin_m3/'
    ]
#num_den=['0.0048','0.0036','0.0024','0.0012']
num_den=['0.0024','massbin1','massbin2','com1','com2','com3']
#num_den=['0.0024','0.0012','massbin1','massbin2']
def f(file_path,label):
    PATH='/project/mtx/output/'+file_path
    print PATH
    Pdh=np.loadtxt(PATH+'Pk_DH')
#   Pdh=np.loadtxt(PATH+'Pk_DKnoWf.txt')
    Pdd=np.loadtxt(PATH+'Pk_DD')
    n=Pdh[:,2]
    bias=Pdh[:,1]/Pdd[:,1]
    b=(bias*n)[:bias_cut].sum()/n[:bias_cut].sum()
    print b
#   bias/=b
    plt.figure('bias')
    plt.plot(Pdh[:,0],bias,'.-',label=label)
    plt.axhline(y=b,linestyle='-.')
    plt.text(Pdh[8,0],b,'$b=%.6f$'%b)
    return Pdh[:,0]

for i in np.arange(len(path)):
    k=f(path[i],num_den[i])

#plt.title('bias')
plt.xlim([k[0]*0.9,k[-1]*1.1])
plt.xscale('log')
plt.xlabel('$\mathrm{k}\ [h/\mathrm{Mpc}]$',fontsize='large')
plt.ylabel('bias')
plt.legend(loc='lower left')
#plt.savefig('../result/all_simulation/bias_weight/bias_CWiener.eps')
plt.show()
