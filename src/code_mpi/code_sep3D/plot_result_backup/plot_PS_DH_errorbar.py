#!/usr/bin/env python
# coding=utf-8
'''
Plot CC, PS with errorbar from all six simulations
'''
import numpy as np
import matplotlib.pyplot as plt
#============================================================
OUTDIR='/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/eps/'
PATH='/project/mtx/output/'
DIR=['tides10/','tides11/','tides12/','tides13/','tides14/','tides15/','tides16/','tides17/','tides18/','tides19/']
NAME='New_CIC_0.0048_3D_NoGau_s1.25_NoWiener/'
file='Pk_DH'
noise=1./(4.8*10**-3)
#============================================================
k=np.loadtxt(PATH+DIR[0]+NAME+file)[:,0]
color='g'
def plot_error_one(file=file,NAME=NAME,disP=1.,noise=noise,color=color,label='$P_{\delta}$'):
    data=[]
    for i in DIR:
        path=PATH+i+NAME+file
        data.append(np.loadtxt(path)[:,1]-noise)
    s=np.array(data)
    mean=s.mean(axis=0)
    std=s.std(axis=0)
    plt.figure('PS')
    plt.errorbar(k*disP,mean,yerr=std,ecolor=color[0],fmt=None)
    plt.plot(k*disP,mean,color,label=label)
    return mean.min(),mean.max()
#===================== plot =================================
range=[]
#========= DH HH DD ===========
#range.append(plot_error_one(file='Pk_DH',NAME=NAME,noise=0,color='g.-',label='$P_{\delta h}$'))
#range.append(plot_error_one(file='Pk_DD',NAME=NAME,noise=0,color='b.-',label='$P_{\delta}$'))
#range.append(plot_error_one(file='Pk_HH',NAME=NAME,noise=noise,color='r.-',label='$P_{h}$'))
#=====1.2 2.4 3.6 4.8==========
range.append(plot_error_one(file='Pk_DD',NAME='New_CIC_0.0048_3D_NoGau_s1.25_NoWiener/',disP=1.0,noise=0,color='k.-',label='$P_{\delta}$'))
range.append(plot_error_one(file='Pk_DH',NAME='New_CIC_0.0048_3D_NoGau_s1.25_NoWiener/',disP=1.02,noise=0,color='r.-',label='$0.0048\ (h/\mathrm{MPc})^{3}$'))
range.append(plot_error_one(file='Pk_DH',NAME='New_CIC_0.0036_3D_NoGau_s1.25_NoWiener/',disP=1.04,noise=0,color='g.-',label='$0.0036\ (h/\mathrm{MPc})^{3}$'))
range.append(plot_error_one(file='Pk_DH',NAME='New_CIC_0.0024_3D_NoGau_s1.25_NoWiener/',disP=1.06,noise=0,color='b.-',label='$0.0024\ (h/\mathrm{MPc})^{3}$'))
range.append(plot_error_one(file='Pk_DH',NAME='New_CIC_0.0012_3D_NoGau_s1.25_NoWiener/',disP=1.08,noise=0,color='m.-',label='$0.0012\ (h/\mathrm{MPc})^{3}$'))
#===================== set ==================================
range=np.array(range)
min=range[:,0].min()
max=range[:,1].max()
#plt.axhline(y=1./(4.8*10**-3),color='k',linestyle="-.")
plt.xlabel('$k\ [h/\mathrm{Mpc}]$',fontsize=18)
plt.ylabel('$\mathrm{Power\ Spectra}$ [$(\mathrm{Mpc}/h)^{3}$]',fontsize=18)
plt.xscale('log')
plt.yscale('log')
#plt.ylim([25,4.*10**4])
plt.ylim([min*0.8,max*1.2])
plt.xlim([k.min()*0.9,k.max()*1.1])
plt.legend(frameon=False)
plt.show()
#plt.savefig(OUTDIR+'PS_DH_errorbar.eps')
#============================================================
