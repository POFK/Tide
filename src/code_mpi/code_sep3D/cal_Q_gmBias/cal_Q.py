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
x=np.linspace(np.log10(data[:,0].min()),np.log10(data[:,0].max()),1000)
Pk=interpolate.interp1d(data[:,0],data[:,1],kind=3)
Pkg=interpolate.interp1d(np.log10(data[:,0]),np.log10(data[:,1]),kind=3)
dPkg=np.gradient(Pkg(x),x[1]-x[0])
fdPkg=interpolate.interp1d(x,dPkg,kind=3)
def fk(k):
    s=2*alpha-beta*fdPkg(np.log10(k))
    return s
#==mode1=================================
kmax=2*np.pi/1200*512.
kmin=2.*np.pi/1200.
#N=10000
#k=np.linspace(kmin,kmax,N+1,endpoint=True)
#dk=(kmax-kmin)/N
#Q1=np.sum(2*k*k/(15*np.pi**2)*dk*fk(k)**2)
#print 'Q1:',Q1
#==mode2=================================
def smooth(k):
    sigma=1.25
    smooth_K=np.exp(-k**2*sigma**2/2.)
    return smooth_K

def Q(x):
    return 2*x**2/(15*np.pi**2)*fk(x)**2*smooth(x)**2
#   return 2*x**2/(15*np.pi**2)*fk(x)**2*Pk(x)**2/(Pk(x)+806.314231603)**2
Q2, err = integrate.quad(Q, kmin,kmax)
print 'Q2:',Q2
print 'error',err

