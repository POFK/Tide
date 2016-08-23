#!/usr/bin/env python
# coding=utf-8
'''plot P_n with errorbar'''
#============================================================
import numpy as np
import matplotlib.pyplot as plt
OUTDIR='/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/eps/'
PATH='/project/mtx/output/'
DIR=['tides10/','tides11/','tides12/','tides13/','tides14/','tides15/','tides16/','tides17/','tides18/','tides19/']
NAME1='CIC_0.0048_3D_NoGau_s1.0_Wiener/'
NAME2='CIC_0.0036_3D_NoGau_s1.0_Wiener/'
NAME3='CIC_0.0024_3D_NoGau_s1.0_Wiener/'
NAME4='CIC_0.0012_3D_NoGau_s1.0_Wiener/'
#NAME1='massbin4biasWeight_halo_cic_0.0012_1.hdf5/'
#NAME2='massbin4biasWeight_halo_cic_0.0012_2.hdf5/'
#NAME3='New_CIC_0.0024_3D_NoGau_s1.25_NoWiener/'

file1='Pk_DKnoWf.txt'
file2='Pk_DD'
file3='Pk_KKnoWf.txt'
bias_cut=6
#============================================================
k=np.loadtxt(PATH+DIR[0]+NAME1+file1)[:,0]
n=np.loadtxt(PATH+DIR[0]+NAME1+file1)[:,2]
num_den=['0.0048','0.0036','0.0024','0.0012']
def f(NAME='',mode=0,color='',label='',disP=1.,shotnoise=None,cut=None):
#******************************
    data_dh=[]
    data_dd=[]
    data_hh=[]
    data_Pn=[]
    for i in DIR:
        Pdh=np.loadtxt(PATH+i+NAME+file1)[:,1]
        Pdd=np.loadtxt(PATH+i+NAME+file2)[:,1]
        Phh=np.loadtxt(PATH+i+NAME+file3)[:,1]
        bias=Pdh/Pdd
        b=bias[:bias_cut].mean()

        if mode==1:
            Pn=(Phh-b**2*Pdd)/(b**2*Pdd)
        if mode==2:
            Pn=(Phh-bias**2*Pdd)/(bias**2)
            plt.ylabel('$(\hat{P_{\kappa}}-b^2P_\delta)/b^2$')#,fontsize=18)
        if mode==3:
            Pn=(Phh-bias**2*Pdd)
#           plt.axhline(y=shotnoise,color=color[0],linestyle='-.')
            plt.ylabel('$\hat{P_{\kappa}}-b^2P_\delta$',fontsize=18)
        data_Pn.append(Pn)

#       data_dh.append(Pdh)
#       data_dd.append(Pdd)
#       data_hh.append(Phh)

    data_Pn=np.array(data_Pn)
#   data_dh=np.array(data_dh)
#   data_dd=np.array(data_dd)
#   data_hh=np.array(data_hh)
#******************************
    Pn_mean=data_Pn.mean(axis=0)
    random_sampling=np.array(np.random.rand(2000)*10/1,dtype=np.int)
    random_Pn=[]
    for S in random_sampling:
        random_Pn.append(data_Pn[S])
    random_Pn=np.array(random_Pn)
    Pn_std=random_Pn.std(axis=0)
#============================================================
    if cut!=None:
        k_cut=k[:cut]
        Pn_mean=Pn_mean[:cut]
        Pn_std=Pn_std[:cut]
    else:
        k_cut=k
    plt.errorbar(k_cut*disP,Pn_mean,yerr=Pn_std,ecolor=color[0],fmt=None)
    plt.plot(k_cut*disP,Pn_mean,color,label=label)
    return Pn_mean.min(),Pn_mean.max()
#========== plot ============================================
plt.figure('noise')
min,max=f(NAME=NAME1,mode=2,color='rv-',label='$0.0048\ (h/\mathrm{Mpc})^{3}$',disP=1.00,shotnoise=1./0.0048,cut=16)
min,max=f(NAME=NAME2,mode=2,color='g>-',label='$0.0036\ (h/\mathrm{Mpc})^{3}$',disP=1.02,shotnoise=1./0.0036,cut=16)
min,max=f(NAME=NAME3,mode=2,color='b<-',label='$0.0024\ (h/\mathrm{Mpc})^{3}$',disP=0.98,shotnoise=1./0.0024,cut=16)
min,max=f(NAME=NAME4,mode=2,color='m^-',label='$0.0012\ (h/\mathrm{Mpc})^{3}$',disP=1.00,shotnoise=1./0.0012,cut=15)

#min,max=f(NAME=NAME1,mode=3,color='r.-',label='$0.0012\ bin1$',disP=1.00)
#min,max=f(NAME=NAME2,mode=3,color='g.-',label='$0.0012\ bin2$',disP=1.02)
#min,max=f(NAME=NAME3,mode=3,color='b.-',label='$0.0024$',disP=0.98)
#========== set =============================================
plt.xlabel('$k\ [h/\mathrm{Mpc}]$')#,fontsize=18)
#plt.ylabel('$\mathrm{noise}$',fontsize=18)
#plt.ylim([-0.1,0.5])
#plt.ylim([100,3*10**3])
plt.xlim([k[0]*0.9,0.8])
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='upper left',ncol=2,frameon=False)
#plt.savefig(OUTDIR+'recon_Pn_b2-1D.eps')
#plt.savefig(OUTDIR+'recon_Pn-1D.eps')
#plt.show()

