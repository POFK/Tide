#!/usr/bin/env python
# coding=utf-8
'''bootstrap'''
import numpy as np
def bootstrap(path=[],file=[],n=10,N=2000):
    print 'number of bootstrap samples:', N
    data_dd=[]
    data_dk=[]
    data_kk=[]

    for i in np.arange(n):
        data_dd.append(np.loadtxt(path[i]+file[0])[:,1])
        data_dk.append(np.loadtxt(path[i]+file[1])[:,1])
        data_kk.append(np.loadtxt(path[i]+file[2])[:,1])

    data_dd=np.array(data_dd)
    data_dk=np.array(data_dk)
    data_kk=np.array(data_kk)
#   data_dd_mean=data_dd.mean(axis=0)
#   data_dk_mean=data_dk.mean(axis=0)
#   data_kk_mean=data_kk.mean(axis=0)

    random_sampling=np.array(np.random.rand(N)*n/1,dtype=np.int)
    random_split=np.array(np.array_split(random_sampling,N/n))

    rand_dd=np.array([data_dd[random_split[i]].mean(axis=0) for i in np.arange(N/n)])
    rand_dk=np.array([data_dk[random_split[i]].mean(axis=0) for i in np.arange(N/n)])
    rand_kk=np.array([data_kk[random_split[i]].mean(axis=0) for i in np.arange(N/n)])

    return [data_dd,data_dk,data_kk,rand_dd,rand_dk,rand_kk]

if __name__=='__main__':
    PATH='/project/mtx/output/'
    DIR=['tides10/','tides11/','tides12/','tides13/','tides14/','tides15/','tides16/','tides17/','tides18/','tides19/']
    NAME='CIC_0.0012_3D_NoGau_s1.0_Wiener/'
    File=['Pk_DD','Pk_DK','Pk_KK']
    path=[PATH+i+NAME for i in DIR]

    ddm,dkm,kkm,ddr,dkr,kkr=bootstrap(path=path,file=File,n=10,N=5000)
    ddm=ddm.mean(axis=0)
    dkm=dkm.mean(axis=0)
    kkm=kkm.mean(axis=0)

    import matplotlib.pyplot as plt
    k=np.loadtxt(path[0]+File[0])[:,0]
    plt.errorbar(k,ddm,yerr=ddr.std(axis=0),label='dd')
    plt.errorbar(k,dkm,yerr=dkr.std(axis=0),label='dk')
    plt.errorbar(k,kkm,yerr=kkr.std(axis=0),label='kk')

    plt.xscale('log')
    plt.yscale('log')
    plt.xlim([k.min()*0.9,k.max()*1.1])
    plt.ylim([kkm.min()*0.9,ddm.max()*1.1])
    plt.legend()
    plt.show()
