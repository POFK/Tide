#!/usr/bin/env python
# coding=utf-8
import scipy.integrate as integrate
import scipy.interpolate as interpolate
import numpy as np
import matplotlib.pyplot as plt
################## par  ##################
a0 = 1.
H0 = 67.8 # km/s/MPc
Omgm = 0.049+0.259
Omgla = 0.692
################## H(a),D(a) ##################
H = lambda a: H0 * (Omgm / a**3 + Omgla)**0.5
D0= lambda a: 1./(a*H(a)/H0)**3
D1= lambda a: 2.5*Omgm*H(a)/H0*integrate.quad(D0,0,a)[0]
D= lambda a: D1(a)/D1(a0)
################## F(a) ##################
F0=lambda x: 1./x**2/H(x)*D(x)
F1=lambda a: 1./a**3/H(a)*integrate.quad(F0,0,a)[0]
F=integrate.quad(F1,0,a0)[0]
################## Dsigma(a) ##################

Dsigma=-H(a0)*integrate.quad(lambda x: D(x)**3/x**2/H(x)/(2.5*Omgm*H0**2),0,a0)[0]+integrate.quad(lambda y:(D(y)/D(1))**2/y**2/(2.5*Omgm*H0**2),0,a0)[0]
#########################alpha beta #############################
alpha=-Dsigma+F
beta=F
######################## interpolate ###############################
data=np.loadtxt('lcdm_pk.dat')
a=np.linspace(np.log10(data[:,0].min()),np.log10(data[:,0].max()),1000)

from TIDES import *
Pk,Pkg=Tide.Get_fk()
dPkg=np.gradient(Pkg(a),a[1]-a[0])
fdPkg=interpolate.interp1d(a,dPkg,kind=3)
def fk(k):
    s=2*alpha-beta*fdPkg(np.log10(k))
    return s
print alpha
print beta

