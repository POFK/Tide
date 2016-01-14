#!/usr/bin/env python
# coding=utf-8
from TIDES import *
import scipy.integrate as integrate
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt
##********************************************************************************#
name='halorhobin1024m3z0.000.dat'
filename='/home/zhm/haloes/halorhobin1024m3z0.000.dat'
data=Tide.LoadData(filename)
data=Tide.Smooth(data=data,sigma=2.5)
#data=np.random.randn(1000000)
#data=data.reshape(-1)
#Tide.SaveDataHdf5(data,filename='/home/mtx/data/tide/haloes/halorhobin1024m3z0.000_SG.hdf5')
data=data.reshape(-1)
sum1=data.sum()
sort_data=data.argsort()
data2=data[sort_data]

###############################gauss...#########################################
n=1024
x=np.linspace(0,4,1000)
def gau(x):
    gau=np.exp(-0.5*x**2)
    return gau
y=[integrate.quad(gau,0,i)[0] for i in x]
f=interpolate.interp1d(y,x)

a=np.linspace(y[0],y[-1],n)
x=f(a)
################################################################################
hist=np.histogram(data2,bins=n)
sort_h=hist[0].argsort()[::-1]
index=[]

for i in hist[1][:-1]: 
    index.append(np.where(data2>i-10**-11)[0][0])
index.append(len(data))
index=np.array(index)

for j in np.arange(n):
    data2[index[sort_h[j]]:index[sort_h[j]+1]]=x[j]

data[sort_data]=data2

plt.subplot(2,1,1)
plt.plot(hist[1][:-1],hist[0],'b-',label='1')
plt.subplot(2,1,2)
hist2=np.histogram(data,bins=n)
plt.plot(hist2[1][:-1],hist2[0],'ro-',label='2')
#plt.xlim(0,4)
plt.legend()
plt.savefig('Gau.png')
################################################################################
sum2=data.sum()
result=(data*sum1/sum2).reshape(1024,1024,1024)
Tide.SaveDataHdf5(result,'/home/mtx/data/tide/haloes/'+name+'.hdf5')
