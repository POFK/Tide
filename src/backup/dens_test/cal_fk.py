#!/usr/bin/env python
# coding=utf-8
import scipy.integrate as integrate
import scipy.interpolate as interpolate
import numpy as np
import matplotlib.pyplot as plt
from TIDES import *
################## par  ##################
a0 =1.
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
alpha=(-Dsigma+F)*H0**2
beta=(F)*H0**2
print alpha,beta
######################## interpolate ###############################
data=np.loadtxt('lcdm_pk.dat')
a=np.linspace(np.log10(data[:,0].min()),np.log10(data[:,0].max()),1000)
Pk=interpolate.interp1d(data[:,0],data[:,1],kind=3)
Pkg=interpolate.interp1d(np.log10(data[:,0]),np.log10(data[:,1]),kind=3)
dPkg=np.gradient(Pkg(a),a[1]-a[0])
#print a[1]-a[0]
fdPkg=interpolate.interp1d(a,dPkg,kind=3)
def fk(k):
    s=2*alpha-beta*fdPkg(np.log10(k))
    return s
#def wk(k):
#    return (fk(k)/Pk(k))**0.5/k
wk=Tide.Get_wk()
ss=np.loadtxt('./coeffz0.dat')
plt.loglog(ss[:,0],ss[:,1],'r')
plt.loglog(ss[:,0],wk(ss[:,0]))
print wk(ss[:,0])/ss[:,1]
plt.show()
plt.loglog(data[:,0],data[:,1],'ro')
plt.loglog(10**a,Pk(10**a))
plt.show()
