#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
#from parameter import Outfile
name='test'
def loaddata(filename):
    dd=np.loadtxt(filename+'PS_DD')
    dk=np.loadtxt(filename+'PS_DK')
    kk=np.loadtxt(filename+'PS_KK')
    r=dk[:,1]/np.sqrt(dd[:,1]*kk[:,1])
    return dd,dk,kk,r
def Pl(Outfile,line='-.',label=''):
    dd=np.loadtxt(Outfile+'PS_DD')
    dk=np.loadtxt(Outfile+'PS_DK')
    kk=np.loadtxt(Outfile+'PS_KK')
    halo=np.loadtxt('/home/mtx/data/tide/outdata/test/PS_haloDD')
    #plt.figure('Power Spectrum')
    #n=np.ones_like(kk[:,1])
    #plt.loglog(dd[:,0],dd[:,1],'b.-',label='P_DD')
    #plt.loglog(halo[:,0],halo[:,1],'m.-',label='P_halo')
    #plt.loglog(dk[:,0],dk[:,1],'g.-',label='P_DK')
    #plt.loglog(kk[:,0],kk[:,1],'r.-',label='P_KK')
    #plt.loglog(kk[:,0],n*noise3,'k-.',alpha=0.8,label='noise')
    #plt.title('Power Spectrum')
    #plt.xlabel('k $(h/Mpc)$')
    #plt.ylabel('P(k) $(Mpc^{3}/h^{3})$')
    #plt.legend()
    #plt.ylim(10**1,6*10**4)
    #plt.xlim([9*10**-3,1])
    ##plt.savefig(name+'PS.eps')
    
    plt.figure('correlation coefficient')
    plt.title('correlation coefficient')
    plt.semilogx(kk[:,0],dk[:,1]/np.sqrt(dd[:,1]*kk[:,1]),line,label=label)
    plt.xlabel('k $(h/Mpc)$')
    plt.ylabel('r')
#    plt.xlim([9*10**-3,1])
    #plt.savefig(name+'CC.eps')
    #plt.show()
    #print dk[:,1]/np.sqrt(dd[:,1]*kk[:,1])

#Pl(Outfile='/home/mtx/data/tide/haloes/outdata/halo_0024/',line='-',label='H0')
#Pl(Outfile='/home/mtx/data/tide/haloes/outdata/halo_0024_L/',line='-',label='L0')

#Pl(Outfile='/project/mtx/output/tides10/highmass2_0.0012_1.0/',line='.-.',label='r1')
#Pl(Outfile='/project/mtx/output/tides11/highmass2_0.0012_1.0/',line='.-.',label='r2')
#Pl(Outfile='/project/mtx/output/tides12/highmass2_0.0012_1.0/',line='.-.',label='r3')
#Pl(Outfile='/project/mtx/output/tides13/highmass2_0.0012_1.0/',line='.-.',label='r4')
#Pl(Outfile='/project/mtx/output/tides14/highmass2_0.0012_1.0/',line='.-.',label='r5')
#Pl(Outfile='/project/mtx/output/tides15/highmass2_0.0012_1.0/',line='.-.',label='r6')
#================================================================================
def result(f1,f2,f3,f4,f5,f6,fmt):
    dd1,dk1,kk1,r1=loaddata(filename=f1)
    dd2,dk2,kk2,r2=loaddata(filename=f2)
    dd3,dk3,kk3,r3=loaddata(filename=f3)
    dd4,dk4,kk4,r4=loaddata(filename=f4)
    dd5,dk5,kk5,r5=loaddata(filename=f5)
    dd6,dk6,kk6,r6=loaddata(filename=f6)
    def get_mean_std(*args):
        x1,x2,x3,x4,x5,x6=args
        num=len(args)
        data=np.hstack([x1,x2,x3,x4,x5,x6])[:,1::3]
        mean=np.array([i.mean() for i in data])
        return mean
    ddmean=get_mean_std(dd1,dd2,dd3,dd4,dd5,dd6)
    dkmean=get_mean_std(dk1,dk2,dk3,dk4,dk5,dk6)
    kkmean=get_mean_std(kk1,kk2,kk3,kk4,kk5,kk6)
    
    #random=np.array(np.random.rand(1000)*6/1,dtype=np.int)
    random=np.arange(6)
    cc=[r1,r2,r3,r4,r5,r6]
    s=cc[random[0]]
    for i in random[1:]:
        s=np.c_[s,cc[i]]
    std=np.array([j.std() for j in s])
    ################################################################################
    k=dd1[:,0]
    r=dkmean/np.sqrt(ddmean*kkmean)
    #delta_r=r*(dkstd/dkmean*np.sqrt(1./(1+ddstd/ddmean+kkstd/kkmean)))
    delta_r=std
    plt.figure('correlation coefficient')
    plt.title('correlation coefficient')
    #plt.semilogx(k,r,'.-.',label='1')
    print delta_r
    plt.errorbar(k,r,yerr=delta_r,fmt=fmt,alpha=0.6)
    plt.xlabel('k $(h/Mpc)$')
    plt.ylabel('r')
    plt.xscale('log')
    ################################################################################
    
    plt.yticks(np.linspace(0,1,11))
    #plt.ylim([0,1.0])
    #plt.xlim([0.004,1])
    #plt.legend()
f1='/project/mtx/output/tides10/halo_0.0012_1.25/'
f2='/project/mtx/output/tides11/halo_0.0012_1.25/'
f3='/project/mtx/output/tides12/halo_0.0012_1.25/'
f4='/project/mtx/output/tides13/halo_0.0012_1.25/'
f5='/project/mtx/output/tides14/halo_0.0012_1.25/'
f6='/project/mtx/output/tides15/halo_0.0012_1.25/'
result(f1,f2,f3,f4,f5,f6,'r.-')
#
#f1='/project/mtx/output/tides10/highmass3_0.0012_1.25/'
#f2='/project/mtx/output/tides11/highmass3_0.0012_1.25/'
#f3='/project/mtx/output/tides12/highmass3_0.0012_1.25/'
#f4='/project/mtx/output/tides13/highmass3_0.0012_1.25/'
#f5='/project/mtx/output/tides14/highmass3_0.0012_1.25/'
#f6='/project/mtx/output/tides15/highmass3_0.0012_1.25/'
#result(f1,f2,f3,f4,f5,f6,'b.-')
#
#f1='/project/mtx/output/tides10/highmass2_0.0012_1.25/'
#f2='/project/mtx/output/tides11/highmass2_0.0012_1.25/'
#f3='/project/mtx/output/tides12/highmass2_0.0012_1.25/'
#f4='/project/mtx/output/tides13/highmass2_0.0012_1.25/'
#f5='/project/mtx/output/tides14/highmass2_0.0012_1.25/'
#f6='/project/mtx/output/tides15/highmass2_0.0012_1.25/'
#result(f1,f2,f3,f4,f5,f6,'g.-')
#
#
#f1='/project/mtx/output/tides10/halo_0.0012_1.25/'
#f2='/project/mtx/output/tides11/halo_0.0012_1.25/'
#f3='/project/mtx/output/tides12/halo_0.0012_1.25/'
#f4='/project/mtx/output/tides13/halo_0.0012_1.25/'
#f5='/project/mtx/output/tides14/halo_0.0012_1.25/'
#f6='/project/mtx/output/tides15/halo_0.0012_1.25/'
#result(f1,f2,f3,f4,f5,f6,'y.-')
#
plt.ylim([0,1.1])
plt.xlim([0.0045,1])
plt.grid(axis='y')
plt.show()
##plt.savefig('./png/6sim_CC')
#
