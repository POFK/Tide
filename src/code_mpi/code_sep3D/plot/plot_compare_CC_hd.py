#!/usr/bin/env python
# coding=utf-8
'''
compare correlation cofficient in different directory
'''
import matplotlib.pyplot as plt
import numpy as np
OUTDIR='/home/mtx/github/Tide/src/code_mpi/code_sep3D/result/all_simulation/'

DIRPATH='/project/mtx/output/tides10/'
path=[
        ''
        ]
color=['r',
        'b',
        'g',
        'm']
N=4
#========================================
for i in np.arange(N):
    file=DIRPATH+path[i]
    print file
    DD=np.loadtxt(file+'/Pk_DD')
    DH=np.loadtxt(file+'/Pk_DH')
    HH=np.loadtxt(file+'/Pk_HH')
#   r=DH[:,1]/np.sqrt(DD[:,1]*HH[:,1])
    r=DH[:,1]/np.sqrt(DD[:,1]*(HH[:,1]-1./np.float(path[i][4:10])))
    kbin=DD[:,0]
    #========================================
    plt.figure('sdf')
    plt.plot(kbin,DH[:,1],'%s.-'%color[i],label='Pdh$%.4f$'%np.float(path[i][4:10]))
    plt.xscale('log')
    plt.yscale('log')
    print  DH[:,1]
    plt.figure('PS')
    plt.plot(kbin,DD[:,1],'%s.-'%color[i],label='P_d')
    plt.plot(kbin,HH[:,1]-(1./np.float(path[i][4:10])),'%s.-'%color[i],label='$%.4f$'%np.float(path[i][4:10]))
    plt.axhline(y=(1./np.float(path[i][4:10])),color='k',linestyle=":")
    noise=(1./np.float(path[i][4:10]))
    plt.text(DD[0,0],noise,'%.2f'%noise)
    #========================================
    plt.figure('CC')
    plt.plot(kbin,r,'%s.-'%color[i],label='$%.4f$'%np.float(path[i][4:10]))
    plt.figure('Pn')
    bias_cut=9
    n=DH[:,2]
    bias=DH[:,1]/DD[:,1]
    b1=bias
    b2=(bias*n)[:bias_cut].sum()/n[:bias_cut].sum()
    Pn1=(HH[:,1]-b1**2*DD[:,1])/(b1**2*DD[:,1])
    Pn2=(HH[:,1]-b2**2*DD[:,1])/(b2**2*DD[:,1])

    plt.plot(DH[:,0],Pn1,'%s.--'%color[i],label=path[i][4:10]+' real bias')
    plt.plot(DH[:,0],Pn2,'%s.-'%color[i],label=path[i][4:10]+' constant bias')

plt.figure('CC')
plt.grid(axis='y')
plt.xlabel('$\mathrm{k}\ (h/\mathrm{Mpc})$')
plt.ylabel('r')
plt.xlim([kbin[0]*0.9,kbin[-1]*1.1])
plt.ylim([0.35,1])
plt.xscale('log')
plt.legend()
#plt.savefig('CC.eps')


plt.figure('PS')
plt.xlim([kbin[0]*0.9,kbin[-1]*1.1])
plt.ylim([20,5*10**4])
plt.xlabel('$\mathrm{k}\ (h/\mathrm{Mpc})$')
plt.ylabel('Power Spectra [$(\mathrm{Mpc}/h)^{3}$]')
plt.xscale('log')
plt.yscale('log')
plt.legend()
#plt.savefig('Ph.eps')

plt.figure('Pn')
plt.xlabel('$\mathrm{k}\ (h/\mathrm{Mpc})$')
plt.ylabel('$\mathrm{P_{noise}}$')
plt.legend(loc='upper left')
plt.xlim([kbin[0]*0.9,kbin[-1]*1.1])
plt.ylim([-0.5,6.5])
plt.xscale('log')
plt.grid(axis='y')
#plt.savefig('Pn.eps')

plt.figure('sdf')
plt.xlabel('$\mathrm{k}\ (h/\mathrm{Mpc})$')
plt.legend(loc='upper left')
plt.xlim([kbin[0]*0.9,kbin[-1]*1.1])
#plt.ylim([-0.5,6.5])
plt.xscale('log')
plt.grid(axis='y')

plt.show()
