#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import My_matplotlib_par 
#from parameter import Outfile
name='test'
bias=np.ones(20)
def loaddata(filename):
    dd=np.loadtxt(filename+'PS_DD')
    dk=np.loadtxt(filename+'PS_DK')
    kk=np.loadtxt(filename+'PS_KK')
    hh=np.loadtxt(filename+'PS_haloDD')
    r=dk[:,1]/np.sqrt(dd[:,1]*kk[:,1])
    return dd,dk,kk,r,hh
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
#Pl(Outfile='/project/mtx/output/tides13/highmass4_0.0012_1.25/',line='.-.',label='r6')
#plt.show()
#================================================================================
def result(f1,f2,f3,f4,f5,f6,fmt,mode='',label=''):
    dd1,dk1,kk1,r1,h1=loaddata(filename=f1)
    dd2,dk2,kk2,r2,h2=loaddata(filename=f2)
    dd3,dk3,kk3,r3,h3=loaddata(filename=f3)
    dd4,dk4,kk4,r4,h4=loaddata(filename=f4)
    dd5,dk5,kk5,r5,h5=loaddata(filename=f5)
    dd6,dk6,kk6,r6,h6=loaddata(filename=f6)
    def get_mean_std(*args):
        x1,x2,x3,x4,x5,x6=args
        num=len(args)
        data=np.hstack([x1,x2,x3,x4,x5,x6])[:,1::3]
        mean=np.array([i.mean() for i in data])
        std=np.array([i.std() for i in data])
        return mean,std
    ddmean,ddstd=get_mean_std(dd1,dd2,dd3,dd4,dd5,dd6)
    dkmean,dkstd=get_mean_std(dk1,dk2,dk3,dk4,dk5,dk6)
    kkmean,kkstd=get_mean_std(kk1,kk2,kk3,kk4,kk5,kk6)
    hhmean,hhstd=get_mean_std(h1,h2,h3,h4,h5,h6)
    

    random=np.array(np.random.rand(2000)*6/1,dtype=np.int)
    #random=np.arange(6)
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
#   plt.figure('correlation coefficient')
#   plt.title('correlation coefficient')
#   #plt.semilogx(k,r,'.-.',label='1')
#   print delta_r
#   plt.errorbar(k,r,yerr=delta_r,fmt=fmt,label=label)
#   plt.xlabel('k $(h/Mpc)$')
#   plt.ylabel('r')
#   plt.xscale('log')
#   plt.ylim([0,1.1])
#   plt.xlim([0.0045,1])
#   plt.grid(axis='y')
#   plt.yticks(np.linspace(0,1,11))
#   plt.savefig('/home/mtx/eps/CC_0048_1.25.eps')
    ################################################################################
    
    if mode=='PS':
        plt.figure('PS')
#       plt.title('PS')
        plt.errorbar(k,ddmean,yerr=ddstd,ms=5,fmt='ro-',label='$P_{\delta}$')
        plt.errorbar(k,hhmean,yerr=hhstd,ms=5,fmt='mv-',label='$P_{h}$')
        plt.errorbar(k+10**-4,dkmean,yerr=dkstd,ms=5,fmt='g.-.',label='$P_{\delta\kappa}$')
        plt.errorbar(k+2*10**-4,kkmean,yerr=kkstd,ms=5,fmt='bx--',label='$P_{\kappa}$')
#       plt.grid(axis='y')
        plt.axhline(y=1./(4.8*10**-3),color='black',linestyle="-.")
        plt.xlabel('$\mathrm{k}\ [h/\mathrm{Mpc}]$',fontsize='large')
        plt.ylabel('Power Spectra [$(\mathrm{Mpc}/h)^{3}$]',fontsize='large')
        plt.xscale('log')
        plt.yscale('log')
        plt.ylim([1*10**2,4*10**4])
        plt.xlim([4.5*10**-3,0.5])
        plt.legend()
#       plt.savefig('/home/mtx/eps/PS_0048_1.25.eps')
    return k,r,delta_r


    #plt.ylim([0,1.0])
    #plt.xlim([0.004,1])
    #plt.legend()
#######################smooth scale#############################################

#f1='/project/mtx/output/tides10/halo_0.0048_1.0/'
#f2='/project/mtx/output/tides11/halo_0.0048_1.0/'
#f3='/project/mtx/output/tides12/halo_0.0048_1.0/'
#f4='/project/mtx/output/tides13/halo_0.0048_1.0/'
#f5='/project/mtx/output/tides14/halo_0.0048_1.0/'
#f6='/project/mtx/output/tides15/halo_0.0048_1.0/'
##result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
#k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'g.-.',label='$1.25\ Mpc/h$')
#plt.figure('Paper')
#plt.errorbar(k[1:15],r[1:15],yerr=delta_r[1:15],fmt='.-.',label='$1.25\ Mpc/h$')

#f1='/project/mtx/output/tides10/halo_0.0048_test_noGau/'
#f2='/project/mtx/output/tides11/halo_0.0048_test_noGau/'
#f3='/project/mtx/output/tides12/halo_0.0048_test_noGau/'
#f4='/project/mtx/output/tides13/halo_0.0048_test_noGau/'
#f5='/project/mtx/output/tides14/halo_0.0048_test_noGau/'
#f6='/project/mtx/output/tides15/halo_0.0048_test_noGau/'
##result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
#k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'g.-.',label='no Gaussianization')
#plt.figure('Paper')
#plt.errorbar(k[1:15]*bias[1:15]*0.985,r[1:15],yerr=delta_r[1:15],fmt='.-.',label='$\mathrm{no\ Gaussianization}$')


#f1='/project/mtx/output/tides10/halo_0.0048/'
#f2='/project/mtx/output/tides11/halo_0.0048/'
#f3='/project/mtx/output/tides12/halo_0.0048/'
#f4='/project/mtx/output/tides13/halo_0.0048/'
#f5='/project/mtx/output/tides14/halo_0.0048/'
#f6='/project/mtx/output/tides15/halo_0.0048/'
##result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
#k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'g.-.',label='$1.25\ Mpc/h$')
#plt.figure('Paper')
#plt.errorbar(k[1:15],r[1:15],yerr=delta_r[1:15],fmt='^-',label='$1.25\ \mathrm{Mpc}/h$')
##
#
#f1='/project/mtx/output/tides10/halo_0.0048_2.5/'
#f2='/project/mtx/output/tides11/halo_0.0048_2.5/'
#f3='/project/mtx/output/tides12/halo_0.0048_2.5/'
#f4='/project/mtx/output/tides13/halo_0.0048_2.5/'
#f5='/project/mtx/output/tides14/halo_0.0048_2.5/'
#f6='/project/mtx/output/tides15/halo_0.0048_2.5/'
##result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
#k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'r.-.',label='$2.5\ Mpc/h$')
#plt.figure('Paper')
#plt.errorbar(k[1:13]*bias[1:13]*1.015,r[1:13],yerr=delta_r[1:13],fmt='v-',label='$2.5\ \ \ \mathrm{Mpc}/h$')
#
#
##f1='/project/mtx/output/tides10/halo_0.0048_3.5/'
##f2='/project/mtx/output/tides11/halo_0.0048_3.5/'
##f3='/project/mtx/output/tides12/halo_0.0048_3.5/'
##f4='/project/mtx/output/tides13/halo_0.0048_3.5/'
##f5='/project/mtx/output/tides14/halo_0.0048_3.5/'
##f6='/project/mtx/output/tides15/halo_0.0048_3.5/'
###result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
##result(f1,f2,f3,f4,f5,f6,'r1-.',label='$3.5\ Mpc/h$')
#
#
#f1='/project/mtx/output/tides10/halo_0.0048_5.0/'
#f2='/project/mtx/output/tides11/halo_0.0048_5.0/'
#f3='/project/mtx/output/tides12/halo_0.0048_5.0/'
#f4='/project/mtx/output/tides13/halo_0.0048_5.0/'
#f5='/project/mtx/output/tides14/halo_0.0048_5.0/'
#f6='/project/mtx/output/tides15/halo_0.0048_5.0/'
##result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
#k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'c2-.',label='$5.0\ Mpc/h$')
#plt.figure('Paper')
#plt.errorbar(k[1:11]*bias[1:11]*1.03,r[1:11],yerr=delta_r[1:11],fmt='>-',label='$5.0\ \ \ \mathrm{Mpc}/h$')
#
#
##
##f1='/project/mtx/output/tides10/halo_0.0048_8.0/'
##f2='/project/mtx/output/tides11/halo_0.0048_8.0/'
##f3='/project/mtx/output/tides12/halo_0.0048_8.0/'
##f4='/project/mtx/output/tides13/halo_0.0048_8.0/'
##f5='/project/mtx/output/tides14/halo_0.0048_8.0/'
##f6='/project/mtx/output/tides15/halo_0.0048_8.0/'
###result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
##result(f1,f2,f3,f4,f5,f6,'m--.',label='$8.0\ Mpc/h$')
#
#f1='/project/mtx/output/tides10/halo_0.0048_10.0/'
#f2='/project/mtx/output/tides11/halo_0.0048_10.0/'
#f3='/project/mtx/output/tides12/halo_0.0048_10.0/'
#f4='/project/mtx/output/tides13/halo_0.0048_10.0/'
#f5='/project/mtx/output/tides14/halo_0.0048_10.0/'
#f6='/project/mtx/output/tides15/halo_0.0048_10.0/'
##result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
#k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'k.-.',label='$10.0\ Mpc/h$')
#plt.figure('Paper')
#plt.errorbar(k[1:9]*bias[1:9]*1.0,r[1:9],yerr=delta_r[1:9],fmt='<-',label='$10.0\ \mathrm{Mpc}/h$')
##
#plt.xlabel('$\mathrm{k}\ [h/\mathrm{Mpc}]$',fontsize='large')
#plt.ylabel('Correlation Coefficient',fontsize='large')
#plt.xscale('log')
#plt.ylim([0.1,0.9])
#plt.xlim([0.007,0.33])
#plt.grid(axis='y')
#plt.yticks(np.linspace(0.1,0.9,9))

#############################  RSD   ############################################
#f1='/project/mtx/output/tides10/halo_0.0048_rsd_ori_1.25/'
#f2='/project/mtx/output/tides11/halo_0.0048_rsd_ori_1.25/'
#f3='/project/mtx/output/tides12/halo_0.0048_rsd_ori_1.25/'
#f4='/project/mtx/output/tides13/halo_0.0048_rsd_ori_1.25/'
#f5='/project/mtx/output/tides14/halo_0.0048_rsd_ori_1.25/'
#f6='/project/mtx/output/tides15/halo_0.0048_rsd_ori_1.25/'
#result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
#result(f1,f2,f3,f4,f5,f6,'b.-.',label='rsd')
#k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'k<-.',label='$\mathrm{With\ RSD}$')
#plt.figure('Paper')
#plt.errorbar(k[1:15]*bias[1:15]*1.015,r[1:15],yerr=delta_r[1:15],fmt='g<-',label='$\mathrm{with\ RSD}$')

#f1='/project/mtx/output/tides10/halo_0.0048/'
#f2='/project/mtx/output/tides11/halo_0.0048/'
#f3='/project/mtx/output/tides12/halo_0.0048/'
#f4='/project/mtx/output/tides13/halo_0.0048/'
#f5='/project/mtx/output/tides14/halo_0.0048/'
#f6='/project/mtx/output/tides15/halo_0.0048/'
#result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
##result(f1,f2,f3,f4,f5,f6,'r.-.',label='no rsd')
#k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'k^-.',label='$\mathrm{No\ RSD}$')
#plt.figure('Paper')
#plt.errorbar(k[1:15]*bias[1:15]*1.03,r[1:15],yerr=delta_r[1:15],fmt='b^-',label='$\mathrm{no\ RSD}$')
#
#f1='/project/mtx/output/tides10/halo_0.0048_1.25_rsd/'
#f2='/project/mtx/output/tides11/halo_0.0048_1.25_rsd/'
#f3='/project/mtx/output/tides12/halo_0.0048_1.25_rsd/'
#f4='/project/mtx/output/tides13/halo_0.0048_1.25_rsd/'
#f5='/project/mtx/output/tides14/halo_0.0048_1.25_rsd/'
#f6='/project/mtx/output/tides15/halo_0.0048_1.25_rsd/'
##result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
##result(f1,f2,f3,f4,f5,f6,'g.-.',label='deal rsd')
#k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'k>-.',label='$\mathrm{Remove\ RSD}$')
#plt.figure('Paper')
#plt.errorbar(k[1:15]*bias[1:15]*1.0,r[1:15],yerr=delta_r[1:15],fmt='r>-',label='$\mathrm{remove\ RSD}$')
#
#
#plt.xlabel('$\mathrm{k}\ [h/\mathrm{Mpc}]$',fontsize='large')
#plt.ylabel('Correlation Coefficient',fontsize='large')
#plt.xscale('log')
#plt.ylim([0.1,0.9])
#plt.xlim([0.007,0.33])
#plt.grid(axis='y')
#plt.yticks(np.linspace(0.1,0.9,9))


################  mass  ########################################################


#
#f1='/project/mtx/output/tides10/highmass4_0.0012_1.25/'
#f2='/project/mtx/output/tides11/highmass4_0.0012_1.25/'
#f3='/project/mtx/output/tides12/highmass4_0.0012_1.25/'
#f4='/project/mtx/output/tides13/highmass4_0.0012_1.25/'
#f5='/project/mtx/output/tides14/highmass4_0.0012_1.25/'
#f6='/project/mtx/output/tides15/highmass4_0.0012_1.25/'
##result(f1,f2,f3,f4,f5,f6,'r.-',label='4')
#k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'g.-.',label='$4.8\times 10^{-3}$')
#plt.figure('Paper')
#plt.errorbar(k[1:15]*1.00*bias[1:15],r[1:15],yerr=delta_r[1:15],fmt='.-.',label='4')
#
#
#f1='/project/mtx/output/tides10/highmass3_0.0012_1.25/'
#f2='/project/mtx/output/tides11/highmass3_0.0012_1.25/'
#f3='/project/mtx/output/tides12/highmass3_0.0012_1.25/'
#f4='/project/mtx/output/tides13/highmass3_0.0012_1.25/'
#f5='/project/mtx/output/tides14/highmass3_0.0012_1.25/'
#f6='/project/mtx/output/tides15/highmass3_0.0012_1.25/'
##result(f1,f2,f3,f4,f5,f6,'b.-',label='3')
#k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'g.-.',label='$4.8\times 10^{-3}$')
#plt.figure('Paper')
#plt.errorbar(k[1:15]*1.015*bias[1:15],r[1:15],yerr=delta_r[1:15],fmt='v-.',label='3')
#
#
#f1='/project/mtx/output/tides10/highmass2_0.0012_1.25/'
#f2='/project/mtx/output/tides11/highmass2_0.0012_1.25/'
#f3='/project/mtx/output/tides12/highmass2_0.0012_1.25/'
#f4='/project/mtx/output/tides13/highmass2_0.0012_1.25/'
#f5='/project/mtx/output/tides14/highmass2_0.0012_1.25/'
#f6='/project/mtx/output/tides15/highmass2_0.0012_1.25/'
##result(f1,f2,f3,f4,f5,f6,'g.-',label='2')
#k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'g.-.',label='$4.8\times 10^{-3}$')
#plt.figure('Paper')
#plt.errorbar(k[1:15]*1.03*bias[1:15],r[1:15],yerr=delta_r[1:15],fmt='<-.',label='2')
#
#
#f1='/project/mtx/output/tides10/halo_0.0012_1.25/'
#f2='/project/mtx/output/tides11/halo_0.0012_1.25/'
#f3='/project/mtx/output/tides12/halo_0.0012_1.25/'
#f4='/project/mtx/output/tides13/halo_0.0012_1.25/'
#f5='/project/mtx/output/tides14/halo_0.0012_1.25/'
#f6='/project/mtx/output/tides15/halo_0.0012_1.25/'
##result(f1,f2,f3,f4,f5,f6,'k.-',label='1')
#k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'g.-.',label='$4.8\times 10^{-3}$')
#plt.figure('Paper')
#plt.errorbar(k[1:15]*0.99*bias[1:15],r[1:15],yerr=delta_r[1:15],fmt='>-.',label='1')

#######################number density############################################
f1='/project/mtx/output/tides10/halo_0.0048/'
f2='/project/mtx/output/tides11/halo_0.0048/'
f3='/project/mtx/output/tides12/halo_0.0048/'
f4='/project/mtx/output/tides13/halo_0.0048/'
f5='/project/mtx/output/tides14/halo_0.0048/'
f6='/project/mtx/output/tides15/halo_0.0048/'
#result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'g.-.',label='$4.8\times 10^{-3}$')
plt.figure('Paper')
plt.errorbar(k[1:15]*1.00*bias[1:15],r[1:15],yerr=delta_r[1:15],fmt='^-',label='$4.8\\times 10^{-3}\ h^{3}/\mathrm{Mpc}^{3}$')

f1='/project/mtx/output/tides10/halo_0.0036_1.25/'
f2='/project/mtx/output/tides11/halo_0.0036_1.25/'
f3='/project/mtx/output/tides12/halo_0.0036_1.25/'
f4='/project/mtx/output/tides13/halo_0.0036_1.25/'
f5='/project/mtx/output/tides14/halo_0.0036_1.25/'
f6='/project/mtx/output/tides15/halo_0.0036_1.25/'
#result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'g.-.',label='$1.25\ Mpc/h$')
plt.figure('Paper')
plt.errorbar(k[1:15]*1.015*bias[1:15],r[1:15],yerr=delta_r[1:15],fmt='v-',label='$3.6\\times 10^{-3}\ h^{3}/\mathrm{Mpc}^{3}$')

f1='/project/mtx/output/tides10/halo_0.0024_1.25/'
f2='/project/mtx/output/tides11/halo_0.0024_1.25/'
f3='/project/mtx/output/tides12/halo_0.0024_1.25/'
f4='/project/mtx/output/tides13/halo_0.0024_1.25/'
f5='/project/mtx/output/tides14/halo_0.0024_1.25/'
f6='/project/mtx/output/tides15/halo_0.0024_1.25/'
#result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'g.-.',label='$1.25\ Mpc/h$')
plt.figure('Paper')
plt.errorbar(k[1:15]*1.030*bias[1:15],r[1:15],yerr=delta_r[1:15],fmt='>-',label='$2.4\\times 10^{-3}\ h^{3}/\mathrm{Mpc}^{3}$')

f1='/project/mtx/output/tides10/halo_0.0012_1.25/'
f2='/project/mtx/output/tides11/halo_0.0012_1.25/'
f3='/project/mtx/output/tides12/halo_0.0012_1.25/'
f4='/project/mtx/output/tides13/halo_0.0012_1.25/'
f5='/project/mtx/output/tides14/halo_0.0012_1.25/'
f6='/project/mtx/output/tides15/halo_0.0012_1.25/'
#result(f1,f2,f3,f4,f5,f6,'r.-',mode='PS')
k,r,delta_r=result(f1,f2,f3,f4,f5,f6,'g.-.',label='$1.25\ Mpc/h$')
plt.figure('Paper')
plt.errorbar(k[1:15]*1.00*bias[1:15],r[1:15],yerr=delta_r[1:15],fmt='<-',label='$1.2\\times 10^{-3}\ h^{3}/\mathrm{Mpc}^{3}$')

plt.xlabel('$\mathrm{k}\ [h/\mathrm{Mpc}]$',fontsize='large')
plt.ylabel('Correlation Coefficient',fontsize='large')
plt.xscale('log')
plt.ylim([0.0,0.7])
#plt.xlim([0.007,0.33])
plt.xlim([0.007,0.23])
plt.grid(axis='y')
plt.yticks(np.linspace(0.0,1.0,11))



################################################################################


plt.legend()
#plt.ylim([0,1.0])
##plt.xlim([0.0045,1])
#plt.xlim([5*10**-3,0.2])
#plt.grid(axis='y')
#plt.grid(axis='x')
#plt.savefig('/home/mtx/eps/PS_0048_1.25.eps')
#plt.savefig('/home/mtx/eps/RSD_PS_0048_1.25.eps')
#plt.savefig('/home/mtx/eps/number_density.eps')
#plt.savefig('/home/mtx/eps/mass.eps')
#plt.savefig('/home/mtx/eps/different_smooth_scale_noGau.eps')
#plt.savefig('/home/mtx/eps/different_smooth_scale.eps')
#plt.savefig('/home/mtx/eps/mass_0012.eps')
#plt.savefig('/home/mtx/eps/RSD_CC.eps')
plt.show()

