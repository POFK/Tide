#!/usr/bin/env python
# coding=utf-8
import sys
import numpy as np
import matplotlib.pyplot as plt
bias_cut=6
OUTDIR='/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/eps/'
path=[
#   'tides10/massbin4_0.0048_m1/',
#   'tides10/massbin4_0.0048_m2/',
#   'tides10/massbin4_0.0048_m3/',
#   'tides10/massbin4_0.0048_m4/'
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
#num_den=['0.0048','0.0036','0.0024','0.0012']
#num_den=['0.0024','b1','b2','b-1','0.0003']
num_den=['0.0003','bin1','bin2','bin3','bin4','bin5','bin6','bin7','bin8','bin9','bin10']
Color=['k','r','g','b','m','y','r','g','b','m','y']
Lsty=['.-','.-','.-','.-','.-','.-','.--','.--','.--','.--','.--']
#Lsty=['.-','.-','.-','.-','.-','.-','.-','.-','.-','.-','.-']
#num_den=['0.0024','0.0012','massbin1','massbin2']
def f(file_path,label,color,lsty):
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
    plt.plot(Pdh[:,0],bias,'%s%s'%(color,lsty),label=label)
    plt.axhline(y=b,linestyle='-.',color='k')
#   plt.text(Pdh[bias_cut,0],b,'$b=%.6f$'%b)
    return Pdh[:,0]

for i in np.arange(len(path)):
    k=f(path[i],num_den[i],Color[i],Lsty[i])

#plt.title('bias')
plt.xlim([k[0]*0.9,k[-1]*1.1])
plt.ylim([0,6])
plt.xscale('log')
plt.xlabel('$k\ [h/\mathrm{Mpc}]$',fontsize=18)
plt.ylabel('$\mathrm{bias}$',fontsize=18)
plt.legend(loc='upper left',ncol=3)
plt.savefig(OUTDIR+'bw_Sim_bias_0.0003_10mbin.eps')
#plt.savefig('../result/all_simulation/massbin_0.0003_m10_forCombine/bias_massbin.eps')
#plt.show()
