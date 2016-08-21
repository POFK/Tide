#!/usr/bin/env python
# coding=utf-8
'''plot P_h-b^2*P_d with errorbar'''
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
file1='Pk_DH'
file2='Pk_DD'
file3='Pk_HH'
bias_cut=6
#============================================================
k=np.loadtxt(PATH+DIR[0]+NAME1+file1)[:,0]
n=np.loadtxt(PATH+DIR[0]+NAME1+file1)[:,2]
num_den=['0.0048','0.0036','0.0024','0.0012']
def f(NAME='',mode=0,color='',label='',disP=1.,shotnoise=None):
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
        b=(bias*n)[:bias_cut].sum()/n[:bias_cut].sum()

        if mode==1:
            Pn=(Phh-b**2*Pdd)/(b**2*Pdd)
        if mode==2:
            Pn=(Phh-bias**2*Pdd)/(bias**2*Pdd)
        if mode==3:
            Pn=(Phh-bias**2*Pdd)
        data_Pn.append(Pn)

#       data_dh.append(Pdh)
#       data_dd.append(Pdd)
#       data_hh.append(Phh)

    data_Pn=np.array(data_Pn)
#******************************
    Pn_mean=data_Pn.mean(axis=0)
    random_sampling=np.array(np.random.rand(2000)*10/1,dtype=np.int)
    random_Pn=[]
    for S in random_sampling:
        random_Pn.append(data_Pn[S])
    random_Pn=np.array(random_Pn)
    Pn_std=random_Pn.std(axis=0)
#============================================================
    plt.errorbar(k*disP,Pn_mean,yerr=Pn_std,ecolor=color[0],fmt=None)
    plt.plot(k*disP,Pn_mean,color,label=label)
    if shotnoise!=None:
        plt.axhline(y=shotnoise,color=color[0],linestyle='-.')
    return Pn_mean.min(),Pn_mean.max()
#========== plot ============================================
plt.figure('noise')
min,max=f(NAME=NAME4,mode=3,color='rv-',label='$0.0048\ (h/\mathrm{MPc})^{3}$',disP=1.00,shotnoise=1./0.0048)
min,max=f(NAME=NAME3,mode=3,color='g>-',label='$0.0036\ (h/\mathrm{MPc})^{3}$',disP=1.02,shotnoise=1./0.0036)
min,max=f(NAME=NAME2,mode=3,color='b<-',label='$0.0024\ (h/\mathrm{MPc})^{3}$',disP=0.98,shotnoise=1./0.0024)
min,max=f(NAME=NAME1,mode=3,color='m^-',label='$0.0012\ (h/\mathrm{MPc})^{3}$',disP=1.00,shotnoise=1./0.0012)
#========== set =============================================
plt.xlabel('$k\ [h/\mathrm{Mpc}]$',fontsize=18)
#plt.ylabel('$(P_h-b^2P_{\delta})/b^2P_{\delta}$',fontsize=18)   # mode2
plt.ylabel('$P_h-b^2P_{\delta}$',fontsize=18)   # mode3
#plt.ylim([10**-2,10])
plt.xlim([k[0]*0.9,k[-1]*1.1])
#plt.xlim([k[0]*0.9,1.1])
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='upper left',frameon=False)

plt.savefig(OUTDIR+'SimPnErrorbar.eps')
#plt.show()
