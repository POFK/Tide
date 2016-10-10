#!/usr/bin/env python
# coding=utf-8
'''plot bias with errorbar'''
#============================================================
import numpy as np
import matplotlib.pyplot as plt
OUTDIR='/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/eps/'
PATH='/project/mtx/output/'
DIR=['tides10/','tides11/','tides12/','tides13/','tides14/','tides15/','tides16/','tides17/','tides18/','tides19/']
NAME1='CIC_0.0012_3D_NoGau_s1.0_Wiener/'
NAME2='CIC_0.0024_3D_NoGau_s1.0_Wiener/'
NAME3='CIC_0.0036_3D_NoGau_s1.0_Wiener/'
NAME4='CIC_0.0048_3D_NoGau_s1.0_Wiener/'
#file1='Pk_DH'
file1='Pk_DKnoWf.txt'
file2='Pk_DD'
bias_cut=6
#============================================================
k=np.loadtxt(PATH+DIR[0]+NAME1+file1)[:,0]
n=np.loadtxt(PATH+DIR[0]+NAME1+file1)[:,2]
num_den=['0.0048','0.0036','0.0024','0.0012']
bias_factor={  #  the factor of 1/(b0^2*Q)
        NAME4: 1./(0.845633720084**2*0.205828),  #0.0048
        NAME3: 1./(0.898634053874**2*0.166597),  #0.0036
        NAME2: 1./(0.970430855221**2*0.121419),  #0.0024
        NAME1: 1./(1.11371021548**2*0.069234),  #0.0012
        }
def f(NAME='',color='',label='',disP=1.):
#******************************
    data_dh=[]
    data_dd=[]
    print NAME
    print bias_factor[NAME]
    for i in DIR:
        data_dh.append(np.loadtxt(PATH+i+NAME+file1)[:,1]*bias_factor[NAME])
#       data_dh.append(np.loadtxt(PATH+i+NAME+file1)[:,1])
        data_dd.append(np.loadtxt(PATH+i+NAME+file2)[:,1])
#   data_dh=np.array(data_dh)*bias_factor[NAME]
    data_dd=np.array(data_dd)
    bias=data_dh/data_dd
    bias_mean=bias.mean(axis=0)
    random_sampling=np.array(np.random.rand(2000)*10/1,dtype=np.int)
    random_bias=[]
    for S in random_sampling:
        random_bias.append(bias[S])
    random_bias=np.array(random_bias)
    bias_std=random_bias.std(axis=0)
#   print 'bias_std:',bias_std
    b=(bias_mean[:bias_cut].mean())
#******************************
    plt.figure('bias')
    plt.errorbar(k*disP,bias_mean,yerr=bias_std,ecolor=color[0],fmt=None)
    plt.plot(k*disP,bias_mean,color,label=label)
    plt.axhline(y=b,color=color[0],linestyle='-.')
#   plt.text(k[6],b,'$b=%.4f$'%b)
    print b
    return bias_mean.min(),bias_mean.max()
#========== plot ============================================
min,max=f(NAME=NAME4,color='rv-',label='$0.0048\ (h/\mathrm{Mpc})^{3}$',disP=1.00)
min,max=f(NAME=NAME3,color='g>-',label='$0.0036\ (h/\mathrm{Mpc})^{3}$',disP=1.02)
min,max=f(NAME=NAME2,color='b<-',label='$0.0024\ (h/\mathrm{Mpc})^{3}$',disP=0.98)
min,max=f(NAME=NAME1,color='m^-',label='$0.0012\ (h/\mathrm{Mpc})^{3}$',disP=1.00)
#========== set =============================================
#plt.xlim([k[0]*0.9,k[-1]*1.1])
plt.xlim([k[0]*0.9,1])
plt.ylim([0,1])
plt.yticks(np.linspace(0.1,1.0,10))
plt.xscale('log')
plt.xlabel('$k\ [h/\mathrm{Mpc}]$')#,fontsize=18)
plt.ylabel('$\mathrm{bias}$')#,fontsize=18)
plt.legend(loc='lower left',frameon=False)#,frameon=False)
#plt.savefig(OUTDIR+'recon_bias_errorbar.eps')
plt.show()
