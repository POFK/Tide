#!/usr/bin/env python
# coding=utf-8
'''plot bias with errorbar'''
#============================================================
import numpy as np
import matplotlib.pyplot as plt
OUTDIR='/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/all_simulation/'
PATH='/project/mtx/output/'
DIR=['tides10/']#,'tides11/','tides12/','tides13/','tides14/','tides15/','tides16/','tides17/','tides18/','tides19/']
NAME1='New_CIC_0.0048_3D_NoGau_s1.25_NoWiener/'
NAME2='New_CIC_0.0036_3D_NoGau_s1.25_NoWiener/'
NAME3='New_CIC_0.0024_3D_NoGau_s1.25_NoWiener/'
NAME4='New_CIC_0.0012_3D_NoGau_s1.25_NoWiener/'
file1='Pk_DD'
file2='Pk_DH'
file3='Pk_HH'
bias_cut=9
#============================================================
k=np.loadtxt(PATH+DIR[0]+NAME1+file1)[:,0]
n=np.loadtxt(PATH+DIR[0]+NAME1+file1)[:,2]
num_den=['0.0048','0.0036','0.0024','0.0012']
def f(NAME='',color='',label='',disP=1.,noise=0.):
#******************************
    pdd=np.loadtxt(PATH+'tides10/'+NAME+file1)[:,1]
    pdh=np.loadtxt(PATH+'tides10/'+NAME+file2)[:,1]
    phh=np.loadtxt(PATH+'tides10/'+NAME+file3)[:,1]

    bias=pdh/pdd
    b=(bias*n)[:bias_cut].sum()/n[:bias_cut].sum()
    wiener=b**2*pdd/phh
#   wiener=bias**2*pdd/phh
    w=(wiener*n)[:bias_cut].sum()/n[:bias_cut].sum()
#******************************
    plt.figure('wiener')
    plt.plot(k*disP,wiener,'%s'%color,label=label)
    plt.axhline(y=w,linestyle='-.')
    plt.text(k[8],w,'$b=%.6f$'%w)
    return wiener.min(),wiener.max()
#========== plot ============================================
min,max=f(NAME=NAME1,color='r.-',label='$0.0048\ (h/\mathrm{MPc})^{3}$',disP=1.00)
min,max=f(NAME=NAME2,color='g.-',label='$0.0036\ (h/\mathrm{MPc})^{3}$',disP=1.02)
min,max=f(NAME=NAME3,color='b.-',label='$0.0024\ (h/\mathrm{MPc})^{3}$',disP=0.98)
min,max=f(NAME=NAME4,color='m.-',label='$0.0012\ (h/\mathrm{MPc})^{3}$',disP=1.00)
#========== set =============================================
plt.xlim([k[0]*0.9,k[-1]*1.1])
plt.xscale('log')
plt.xlabel('$k\ [h/\mathrm{Mpc}]$',fontsize=18)
plt.ylabel('$\mathrm{wiener}$',fontsize=18)
plt.legend(loc='lower left',frameon=False)
#plt.savefig(OUTDIR+'wiener.eps')
plt.show()
