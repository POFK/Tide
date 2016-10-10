#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
import scipy.interpolate as interpolate
from scipy import integrate as integrate_Q
import h5py
import fftw3 as fftw
H0=67.8
Q=0.1681732
alpha=0.000211210262094*H0**2
beta=0.000470867426204*H0**2
data=np.loadtxt('/home/mtx/github/Tide/src/lcdm_pk.dat')
#========
dir = ['tides10','tides11','tides12','tides13','tides14','tides15','tides16','tides17','tides18','tides19']
Pd=[]
Ph=[]
NumberD=0.0024
print NumberD
bias={'0.0012':1.110380,
        '0.0024':0.964854,
        '0.0036':0.889867,
        '0.0048':0.838964}
b=bias[str(NumberD)]
#b=0.838964
#b=0.889867
#b=0.964854
#b=1.110380

for d in dir:
    Pd.append(np.loadtxt('/project/mtx/output/'+d+'/CIC_'+str(NumberD)+'_3D_NoGau_s1.0_Wiener/Pk_DD')[:,1])
    Ph.append(np.loadtxt('/project/mtx/output/'+d+'/CIC_'+str(NumberD)+'_3D_NoGau_s1.0_Wiener/Pk_HH')[:,1])
Pd=np.array(Pd)
Ph=np.array(Ph)
dataD=Pd.mean(axis=0)
dataH=Ph.mean(axis=0)
k=np.loadtxt('/project/mtx/output/tides11/CIC_0.0012_3D_NoGau_s1.0_Wiener/Pk_HH')[:,0]
kmax=2*np.pi/1200*512.
kmin=2.*np.pi/1200.
#========
x=np.linspace(np.log10(data[:,0].min()),np.log10(data[:,0].max()),1000)
#xx=np.linspace(np.log10(kmin),np.log10(kmax),1000)
xx=np.linspace(kmin,kmax,1000)
Pk=interpolate.interp1d(data[:,0],data[:,1],kind=3)
Pkg=interpolate.interp1d(np.log10(data[:,0]),np.log10(data[:,1]),kind=3)
dPkg=np.gradient(Pkg(x),x[1]-x[0])
fdPkg=interpolate.interp1d(x,dPkg,kind=3)
def smooth(k):
    sigma=5.0
    smooth_K=np.exp(-k**2*sigma**2/2.)
    return smooth_K
def fk(k):
    s=2*alpha-beta*fdPkg(np.log10(k))
    return s
#==mode1=================================
Pk_h=interpolate.UnivariateSpline(k, dataH, s=0)
Pk_d=interpolate.UnivariateSpline(k, dataD, s=0)
def Q(x):
#   return 2*x**2/(15*np.pi**2)*fk(x)**2
#   return 2*x**2/(15*np.pi**2)*fk(x)**2*b**4*Pk_d(x)**2/(Pk_h(x))**2    # no smoothing kernal's effect
    return 2*x**2/(15*np.pi**2)*fk(x)**2*b**4*Pk_d(x)**2/(Pk_h(x))**2*smooth(x)**2
Q2, err = integrate.quad(Q, kmin,kmax)
print 'Q2:',Q2
print 'error',err

