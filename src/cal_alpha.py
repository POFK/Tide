#!/usr/bin/env python
# coding=utf-8
import scipy.integrate as integrate
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
print F
################## Dsigma(a) ##################
Htao1 =lambda a: a**2*H(a)*(-3.*H0/(2.*a**4*(Omgm/a**3+Omgla)**0.5)) # partial H(t)
Dtao1=lambda a: a**2*H(a)*2.5*Omgm/H0*(
        -3.*H0/(2.*a**4*(Omgm/a**3+Omgla)**0.5)*integrate.quad(lambda x: 1./(x*H(x)/H0)**3,0,a)[0]+H(a)/(a*H(a)/H0)**3
        )/D1(1.)
Dsigma0= lambda a: 1./(a**2*H(a))*(H(a0)*D(a)-H(a)*D(a0))/(Htao1(a)*D(a)-H(a)*Dtao1(a))*(D(a)**2)/(a*D(a0))
Dsigma=integrate.quad(Dsigma0,0,a0)[0]
print Dsigma
