#!/usr/bin/env python
# coding=utf-8
'''
Plot CC, PS with errorbar from all six simulations
'''
import numpy as np
import matplotlib.pyplot as plt
#============================================================
PATH='/project/mtx/output/'
OUTDIR='/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/eps/'
DIR=['tides10/','tides11/','tides12/','tides13/','tides14/','tides15/','tides16/','tides17/','tides18/','tides19/']
NAME='CIC_0.0012_3D_NoGau_s1.0_Wiener/'
#file1='Pk_HH'
#file2='Pk_DH'
#file3='Pk_DD'
file1='Pk_KK'
file2='Pk_DK'
file3='Pk_DD'
#============================================================
noise=1./(4.8*10**-3)
#============================================================
k=np.loadtxt(PATH+DIR[0]+NAME+file1)[:,0]
color='g'
def plot_error_one(noise=noise,color=color,label='$P_{\delta}$',disP=1,cut=None):
    data_hh=[]
    data_dh=[]
    data_dd=[]
    for i in DIR:
        data_hh.append(np.loadtxt(PATH+i+NAME+file1)[:,1])
        data_dh.append(np.loadtxt(PATH+i+NAME+file2)[:,1])
        data_dd.append(np.loadtxt(PATH+i+NAME+file3)[:,1])
    data_hh=np.array(data_hh)
    data_dh=np.array(data_dh)
    data_dd=np.array(data_dd)
    CC=data_dh/(data_dd*data_hh)**0.5
    CC_mean=CC.mean(axis=0)
    random_sampling=np.array(np.random.rand(2000)*10/1,dtype=np.int)
    random_CC=[]
    for S in random_sampling:
        random_CC.append(CC[S])
    random_CC=np.array(random_CC)
    CC_std=random_CC.std(axis=0)
    #====================
    if cut!=None:
        k_cut=k[:cut]
        CC_mean=CC_mean[:cut]
        CC_std=CC_std[:cut]
    elif cut== None:
        k_cut=k
    plt.figure('CC')
    plt.errorbar(k_cut*disP,CC_mean,yerr=CC_std,ecolor=color[0],fmt=None)
    plt.plot(k_cut*disP,CC_mean,color,label=label,linewidth=1.3)
    return CC_mean.min(),CC_mean.max()
#===================== plot =================================
NAME='CIC_0.0048_3D_NoGau_s1.0_Wiener/'
min,max=plot_error_one(noise=noise,color='rv-',label='$0.0048\ (h/\mathrm{Mpc})^{3}$',disP=1.00)
NAME='CIC_0.0036_3D_NoGau_s1.0_Wiener/'
min,max=plot_error_one(noise=noise,color='g>-',label='$0.0036\ (h/\mathrm{Mpc})^{3}$',disP=1.02)
NAME='CIC_0.0024_3D_NoGau_s1.0_Wiener/'
min,max=plot_error_one(noise=noise,color='b<-',label='$0.0024\ (h/\mathrm{Mpc})^{3}$',disP=0.98)
NAME='CIC_0.0012_3D_NoGau_s1.0_Wiener/'
min,max=plot_error_one(noise=noise,color='m^-',label='$0.0012\ (h/\mathrm{Mpc})^{3}$',disP=1.00)
NAME='CIC_0.0003_3D_NoGau_s1.0_Wiener/'
min,max=plot_error_one(noise=noise,color='k.-',label='$0.0003\ (h/\mathrm{Mpc})^{3}$',disP=1.02,cut=14)
#===================== set ==================================
#plt.title('$r_{\mathrm{h}\delta}$')
plt.xlabel('$\mathrm{k}\ [h/\mathrm{Mpc}]$',fontsize=20)
plt.ylabel('$\mathrm{Correlation\ Coefficient}$',fontsize=20)
plt.xscale('log')
#plt.yscale('log')
plt.ylim([0.1,1.])
#plt.xlim([k.min()*0.9,k.max()*1.1])
plt.xlim([k.min()*0.9,0.6])
#==============set ticks =================
#plt.title('$r_{\mathrm{h}\delta}$')
plt.xticks([10**-2,10**-1],[r'$10^{-2}$',r'$10^{-1}$'])
plt.yticks(np.linspace(0.1,1.0,10),
['$0.1$','$0.2$','$0.3$','$0.4$','$0.5$','$0.6$','$0.7$','$0.8$','$0.9$','$1.0$'])

plt.grid(axis='y')
plt.legend(loc='lower left',ncol=2,frameon=False)#,fontsize=14)
plt.show()
#plt.savefig(OUTDIR+'CC_ND_S1.0.eps')
#============================================================
