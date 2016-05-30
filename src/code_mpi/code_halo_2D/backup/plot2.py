#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
#from parameter import Outfile
name='test'
noise3=(0.6*10**3)**3/1000000.
print noise3
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

#Pl(Outfile='/home/mtx/data/tide/haloes2/outdata/halo_0024/',line='--',label='H')
#Pl(Outfile='/home/mtx/data/tide/haloes2/outdata/halo_0024_L/',line='--',label='L')
#Pl(Outfile='/home/mtx/data/tide/haloes2/outdata/halo_0024_r1/',line='-.',label='r1')
#Pl(Outfile='/home/mtx/data/tide/haloes2/outdata/halo_0024_r2/',line='-.',label='r2')
#Pl(Outfile='/home/mtx/data/tide/haloes2/outdata/halo_0024_r3/',line='-.',label='r3')
#Pl(Outfile='/home/mtx/data/tide/haloes2/outdata/halo_0024_r4/',line='-.',label='r4')
#Pl(Outfile='/home/mtx/data/tide/haloes2/outdata/halo_0024_r5/',line='-.',label='r5')
#Pl(Outfile='/home/mtx/data/tide/haloes2/outdata/halo_0024_r6/',line='-.',label='r6')
#Pl(Outfile='/home/mtx/data/tide/haloes2/outdata/halo_0024_r7/',line='-.',label='r7')
#Pl(Outfile='/home/mtx/data/tide/haloes2/outdata/halo_0024_r8/',line='-.',label='r8')
#Pl(Outfile='/home/mtx/data/tide/haloes2/outdata/halo_0024_r9/',line='-.',label='r9')

#Pl(Outfile='/project/mtx/data/tide/data_halo/data/hm1/',line='--',label='h1')
#Pl(Outfile='/project/mtx/data/tide/data_halo/data/hm2/',line='--',label='h2')
#Pl(Outfile='/project/mtx/data/tide/data_halo/data/hm3/',line='--',label='h3')
#Pl(Outfile='/project/mtx/data/tide/data_halo/data/hm4/',line='--',label='h4')

#Pl(Outfile='/home/mtx/data/tide/haloes/outdata/halo_0048rsd/',line='-.',label='rsd')
#Pl(Outfile='/home/mtx/data/tide/haloes/outdata/halo_0048/',line='-.',label='1.25')
#Pl(Outfile='/home/mtx/data/tide/haloes2/outdata/halo_0048rsd/',line='-.',label='rsd2')
#Pl(Outfile='/home/mtx/data/tide/haloes2/outdata/halo_0048/',line='-.',label='1.252')

#Pl(Outfile='/project/mtx/data/tide/haloes1/test_halo/',line='-.',label='1.25')
#Pl(Outfile='/project/mtx/data/tide/haloes1/test_halorsd/',line='-.',label='rsd')

Pl(Outfile='/project/mtx/data/tide/haloes2/halo_0048/',line='-.',label='1.25')
Pl(Outfile='/project/mtx/data/tide/haloes2/halo_0048_rsd/',line='-.',label='rsd')
Pl(Outfile='/project/mtx/data/tide/haloes2/halo_0048_rsd_dealtest/',line='.--',label='rsd_d')

#Pl(Outfile='/home/mtx/data/tide/haloes/outdata/halo_0048_s2.5/',line='-.',label='2.5')
#Pl(Outfile='/home/mtx/data/tide/haloes/outdata/halo_0048_s5.0/',line='-.',label='5')
#Pl(Outfile='/home/mtx/data/tide/haloes/outdata/halo_0048_s8.0/',line='-.',label='8')
#Pl(Outfile='/home/mtx/data/tide/haloes/outdata/halo_0048_s10.0/',line='-.',label='10')
#Pl(Outfile='/home/mtx/data/tide/haloes/outdata/halo_0048_s12.5/',line='-.',label='12.5')

################################################################################
plt.yticks(np.linspace(0,1,11))
plt.ylim([0,1.0])
plt.xlim([10**-2,1])
plt.grid(axis='y')
plt.legend()
plt.show()
#plt.savefig('compare_rsd')
