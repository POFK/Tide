#!/usr/bin/env python
# coding=utf-8
'''
Plot CC, PS with errorbar from all six simulations
'''
import numpy as np
from bootstrap import bootstrap
import matplotlib.pyplot as plt
#============================================================
OUTDIR='/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/eps/'
PATH='/project/mtx/output/'
DIR=['tides10/','tides11/','tides12/','tides13/','tides14/','tides15/','tides16/','tides17/','tides18/','tides19/']
NAME='CIC_0.0012_3D_NoGau_s1.0_Wiener/'
file='Pk_HH'
noise=1./(4.8*10**-3)
#============================================================
bias_cut=6
k=np.loadtxt(PATH+DIR[0]+NAME+file)[:,0]
color='g'
#============================================================

def file_name(NAME=''):
#   NAME='CIC_0.0012_3D_NoGau_s1.0_Wiener/'
    PATH='/project/mtx/output/'
    DIR=['tides10/','tides11/','tides12/','tides13/','tides14/','tides15/','tides16/','tides17/','tides18/','tides19/']
    path=[PATH+i+NAME for i in DIR]
    return path

def plot_error_bootstrap_DD(NAME='',disP=1.,noise=0.,color='r--',label='',lw=2.,bootN=2000,n=10):
    path=file_name(NAME)
    data_dd,data_dh,data_hh,rand_dd,rand_dh,rand_hh=bootstrap(path=path,file=['Pk_DD','Pk_DH','Pk_HH'],n=n,N=bootN)
    bias=data_dh/data_dd
    Pn=data_hh/bias**2-data_dd
    Pd=data_dd

    Pd_mean=Pd.mean(axis=0)
    std=rand_dd.std(axis=0)

    plt.errorbar(k*disP,Pd_mean,yerr=std,ecolor=color[0],fmt=None)
    plt.plot(k*disP,Pd_mean,color,label=label,linewidth=lw)

def plot_error_bootstrap_HH(NAME='',disP=1.,noise=noise,color='r--',label='',lw=2.,bootN=2000,n=10):
    path=file_name(NAME)
    data_dd,data_dh,data_hh,rand_dd,rand_dh,rand_hh=bootstrap(path=path,file=['Pk_DD','Pk_DH','Pk_HH'],n=n,N=bootN)
    bias=data_dh/data_dd
    Pn=data_hh/bias**2-data_dd
#   Ph=data_hh-noise
#   Ph_mean=Ph.mean(axis=0)/bias.mean(axis=0)**2
    Ph=(data_hh-noise)/bias**2
    Ph_mean=Ph.mean(axis=0)

    std=rand_hh.std(axis=0)
    plt.errorbar(k*disP,Ph_mean,yerr=std,ecolor=color[0],fmt=None)
    plt.plot(k*disP,Ph_mean,color,label=label,linewidth=lw)

def plot_error_bootstrap_bias(NAME='',bias_cut=bias_cut,disP=1.,noise=noise,color='r--',label='',lw=2.,bootN=2000,n=10):
    path=file_name(NAME)
    data_dd,data_dh,data_hh,rand_dd,rand_dh,rand_hh=bootstrap(path=path,file=['Pk_DD','Pk_DH','Pk_HH'],n=n,N=bootN)
    bias=data_dh/data_dd
    Pn=data_hh/bias**2-data_dd

    bias_mean=bias.mean(axis=0)
    std=(rand_dh/rand_dd).std(axis=0)

    b=(bias_mean[:bias_cut].mean())
    plt.axhline(y=b,color=color[0],linestyle='-')
    plt.text(k[7],b,'$b=%.2f$'%b)
    plt.errorbar(k*disP,bias_mean,yerr=std,ecolor=color[0],fmt=None)
    plt.plot(k*disP,bias_mean,color,label=label,linewidth=lw)


def plot_error_bootstrap_Pn(NAME='',bias_cut=bias_cut,disP=1.,noise=noise,color='r--',label='',lw=2.,bootN=2000,n=10):
    path=file_name(NAME)
    data_dd,data_dh,data_hh,rand_dd,rand_dh,rand_hh=bootstrap(path=path,file=['Pk_DD','Pk_DH','Pk_HH'],n=n,N=bootN)
    bias=data_dh/data_dd
    Pn=data_hh/bias**2-data_dd

    Pn_mean=Pn.mean(axis=0)
    shotN=(noise/bias**2).mean(axis=0)
    std=(rand_hh/(rand_hh/rand_dd)**2-rand_dd).std(axis=0)

    plt.errorbar(k*disP,Pn_mean,yerr=std,ecolor=color[0],fmt=None)
    plt.plot(k*disP,Pn_mean,color,label=label,linewidth=lw)
    plt.plot(k*disP,shotN,color[0],linewidth=lw-1.5)


#================================================================================
plt.figure('PS')
plot_error_bootstrap_DD(NAME='CIC_0.0048_3D_NoGau_s1.0_Wiener/',color='k-',noise=0,label='$P_{\delta \delta}$')
plot_error_bootstrap_HH(NAME='CIC_0.0012_3D_NoGau_s1.0_Wiener/',color='r--',noise=1./(1.2*10**-3),label='$0.0012\ h^{3}\mathrm{Mpc}^{-3}$')
plot_error_bootstrap_HH(NAME='CIC_0.0024_3D_NoGau_s1.0_Wiener/',color='g-.',noise=1./(2.4*10**-3),label='$0.0024\ h^{3}\mathrm{Mpc}^{-3}$')
plot_error_bootstrap_HH(NAME='CIC_0.0048_3D_NoGau_s1.0_Wiener/',color='b:', noise=1./(4.8*10**-3),label='$0.0048\ h^{3}\mathrm{Mpc}^{-3}$')
#********************
plt.figure('bias')
plot_error_bootstrap_bias(NAME='CIC_0.0012_3D_NoGau_s1.0_Wiener/',color='r--',noise=1./(1.2*10**-3),label='$0.0012\ h^{3}\mathrm{Mpc}^{-3}$')
plot_error_bootstrap_bias(NAME='CIC_0.0024_3D_NoGau_s1.0_Wiener/',color='g-.',noise=1./(2.4*10**-3),label='$0.0024\ h^{3}\mathrm{Mpc}^{-3}$')
plot_error_bootstrap_bias(NAME='CIC_0.0048_3D_NoGau_s1.0_Wiener/',color='b:', noise=1./(4.8*10**-3),label='$0.0048\ h^{3}\mathrm{Mpc}^{-3}$')
#********************
plt.figure('Pn')
plot_error_bootstrap_DD(NAME='CIC_0.0048_3D_NoGau_s1.0_Wiener/',color='k-',noise=0,label='$P_{\delta \delta}$')
plot_error_bootstrap_Pn(NAME='CIC_0.0012_3D_NoGau_s1.0_Wiener/',color='r--',noise=1./(1.2*10**-3),label='$0.0012\ h^{3}\mathrm{Mpc}^{-3}$',disP=0.98)
plot_error_bootstrap_Pn(NAME='CIC_0.0024_3D_NoGau_s1.0_Wiener/',color='g-.',noise=1./(2.4*10**-3),label='$0.0024\ h^{3}\mathrm{Mpc}^{-3}$',disP=1.00)
plot_error_bootstrap_Pn(NAME='CIC_0.0048_3D_NoGau_s1.0_Wiener/',color='b:', noise=1./(4.8*10**-3),label='$0.0048\ h^{3}\mathrm{Mpc}^{-3}$',disP=1.02)
#================================================================================
##===================== set ==================================
plt.figure('PS')
plt.xlabel('$k\ [h/\mathrm{Mpc}]$')#,fontsize=18)
plt.ylabel('$P_{hh}(k)/b^2(k)$   [$h^{-3}\mathrm{Mpc}^{3}$]')#,fontsize=18)
plt.xscale('log')
plt.yscale('log')
plt.xlim([k.min()*0.95,0.6])
plt.ylim([800.,25000.])
plt.xticks([10**-2,10**-1],[r'${10^{-2}}$',r'$10^{-1}$'])
plt.yticks([10**3,10**4],[r'$10^{3}$',r'$10^{4}$'])
plt.legend(frameon=False)
plt.savefig(OUTDIR+'Sim_halo_property_PS.eps')
#********************
plt.figure('bias')
plt.xlabel('$k\ [h/\mathrm{Mpc}]$')#,fontsize=18)
plt.ylabel('$\mathrm{bias}$')
plt.xscale('log')
plt.xlim([k.min()*0.95,0.6])
plt.ylim([0.6,1.2])
plt.xticks([10**-2,10**-1],[r'$10^{-2}$',r'$10^{-1}$'])
plt.yticks(np.linspace(0.6,1.2,7),
##['$0.2$','$0.4$','$0.6$','$0.8$','$1.0$','$1.2$','$1.4$','$1.6$','$1.8$','$2.0$'])
['$0.6$','$0.7$','$0.8$','$0.9$','$1.0$','$1.1$','$1.2$'])
plt.legend(frameon=False,loc='lower left')
plt.savefig(OUTDIR+'Sim_halo_property_bias.eps')
#********************
plt.figure('Pn')
plt.xlabel('$k\ [h/\mathrm{Mpc}]$')#,fontsize=18)
plt.ylabel('$P_{n}/b^2(k)$   [$h^{-3}\mathrm{Mpc}^{3}$]')#,fontsize=18)
plt.xscale('log')
plt.yscale('log',nonposy='clip')
plt.xlim([k.min()*0.95,0.6])
plt.ylim([200.,25000.])
plt.xticks([10**-2,10**-1],[r'${10^{-2}}$',r'$10^{-1}$'])
plt.yticks([10**3,10**4],[r'$10^{3}$',r'$10^{4}$'])
plt.legend(frameon=False)
plt.savefig(OUTDIR+'Sim_halo_property_Pn.eps')
##============================================================
#plt.show()
##plt.savefig(OUTDIR+'Sim_halo_property.eps')
##============================================================
