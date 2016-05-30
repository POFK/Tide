#!/usr/bin/env python
# coding=utf-8
delta = '/project/mtx/data/tides10/0.000delta_s8.0.hdf5'
kappa = '/project/mtx/data/tides10/kappa_1.25_s8.0.hdf5'
import matplotlib.pyplot as plt
#from My_matplotlib_par import *
import numpy as np
import h5py


cmap=plt.get_cmap('Blues')
#cmap=plt.get_cmap('PuBu')
#cmap=None
min=-0.45
max= 0.45
sigma=3
#min=None
#max=None

plt.subplot(121)
plt.title('$log(1+\delta)$')
f=h5py.File(delta)
data=np.log10(f['data'][:,:,1])
#data=f['data'][:,1,:]
f.close()

#min=data.mean()-sigma*data.std()
#max=data.mean()+sigma*data.std()

plt.imshow(data,norm=None,origin='lower',extent=(1,1200,1,1200),cmap=cmap,vmin=min,vmax=max)
#plt.pcolormesh(data,cmap=cmap,vmin=min,vmax=max)
plt.colorbar(shrink=0.67)
plt.xlabel('$\mathbf{x}\ [Mpc/h]$')
plt.ylabel('$\mathbf{y}\ [Mpc/h]$')



plt.subplot(122)
plt.title('$log(1+\kappa)$')
g=h5py.File(kappa)
datak=np.log10(g['data'][:,:,1])
#datak=g['data'][:,1,:]
g.close()

#min=datak.mean()-sigma*datak.std()
#max=datak.mean()+sigma*datak.std()

plt.imshow(datak,norm=None,origin='lower',extent=(1,1200,1,1200),cmap=cmap,vmin=min,vmax=max)
#plt.pcolormesh(datak,cmap=cmap,vmin=min,vmax=max)
plt.colorbar(shrink=0.67)
plt.xlabel('$\mathbf{x}\ [Mpc/h]$')
plt.ylabel('$\mathbf{y}\ [Mpc/h]$')



#plt.xlim([0,1024])
#plt.ylim([0,1024])
plt.show()
#plt.savefig('x_y.eps')
