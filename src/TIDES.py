#!/usr/bin/env python
# coding=utf-8
import struct
import numpy as np
import matplotlib.pyplot as plt
####################################################
N = 1024
L = 1.2 * 10**3  # Mpc
H = L / 1024.
####################################################


class Tide():

    @classmethod
    def LoadData(self, filename='/home/mtx/data/tide/0.000den00.bin'):
        f = open(filename, 'rb')
        data = f.read()
        f.close()
        data = struct.unpack('1073741824f', data)
        data = np.array(data, dtype=np.float16)
        data = data.reshape((1024, 1024, 1024), order='F')
        return data

    @classmethod
    def GetX(self):
        x = np.arange(1024)
        for i in np.arange(1, 1024 / 2 + 1):
            x[1024 - i] = x[i]
        return x
    @classmethod
    def Get_Alpha_Beta(self):
        '''return alpha,beta'''
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
        ################## Dsigma(a) ##################
        
        Dsigma=-H(a0)*integrate.quad(lambda x: D(x)**3/x**2/H(x)/(2.5*Omgm*H0**2),0,a0)[0]+integrate.quad(lambda y:(D(y)/D(1))**2/y**2/(2.5*Omgm*H0**2),0,a0)[0]
        #########################alpha beta #############################
        alpha=-Dsigma+F
        beta=F
        return (alpha,beta)
