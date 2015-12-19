#!/usr/bin/env python
# coding=utf-8

import struct
import numpy as np
import scipy.integrate as integrate
import scipy.interpolate as interpolate
####################################################
N = 1024
L = 1.2 * 10**3  # Mpc
H = L / 1024.
####################################################


class Tide():

    @classmethod
    def LoadData(self, filename='/home/mtx/data/tide/0.000den00.bin'):
        '''read bin data'''
        print 'Loading data.................'
        f = open(filename, 'rb')
        data = f.read()
        f.close()
        data = struct.unpack('1073741824f', data)
        data = np.array(data, dtype=np.float16)
        data = data.reshape((1024, 1024, 1024), order='F')
        return data

    @classmethod
    def SaveDataHdf5(self,data,filename):
        print 'Save data....................'
        dtype=np.dtype([('data','f4')])
        f=h5py.File(filename,mode='w')
        f.create_dataset(name='data',data=data)
        f.close()

    @classmethod
    def LoadDataOfhdf5(self,filename):
        f=h5py.File(filename)
        data=np.array(f['data'].value,dtype=np.float)
        f.close()
        return data

    @classmethod
    def Get_Alpha_Beta(self):
        '''return alpha,beta'''
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

    @classmethod
    def AutoPowerSpectrum(self,data,window=True):
        x = np.fft.fftfreq(N,1./N)  # x: 0,1,2,...,512,-511,...,-2,-1
        delta_k = np.fft.fftn(data)
        window_k = np.sinc(1. / N * x[:,None,None]) * np.sinc(1. / N * x[None,:,None]) * np.sinc(1. / N * x[None,None,:])
        if window==True:
            Pk = (np.abs(delta_k) / window_k)**2
        else :
            Pk=np.abs(delta_k)**2
        return Pk

    @classmethod
    def CrossPowerSpectrum(self,data1,data2):
        x = np.fft.fftfreq(N,1./N)  # x: 0,1,2,...,512,-511,...,-2,-1
        delta_k1 = np.fft.fftn(data1)
        delta_k2 = np.fft.fftn(data2)
        Pk=(delta_k1.conjugate()*delta_k2+delta_k2.conjugate()*delta_k1)/2
        return Pk.real

    @classmethod
    def Get_wk(self):
        '''par:
        H0 = 67.8 # km/s/MPc
        Omgm = 0.049+0.259
        Omgla = 0.692'''
        H0=67.8
        Q=0.1681732
        alpha=0.000211210262094*H0**2
        beta=0.000470867426204*H0**2
        data=np.loadtxt('lcdm_pk.dat')
        x=np.linspace(np.log10(data[:,0].min()),np.log10(data[:,0].max()),1000)
        Pk=interpolate.interp1d(data[:,0],data[:,1],kind=3)
        Pkg=interpolate.interp1d(np.log10(data[:,0]),np.log10(data[:,1]),kind=3)
        dPkg=np.gradient(Pkg(x),x[1]-x[0])
        fdPkg=interpolate.interp1d(x,dPkg,kind=3)
        def fk(k):
            s=2*alpha-beta*fdPkg(np.log10(k))
            return s
        def wk(k):
#           return (fk(k)/Pk(k))**0.5/k
            return (fk(k)/Pk(k)/Q)**0.5/k
        return wk

    @classmethod
    def Smooth(self,data,sigma=1.25,log=True):

        print 'Smoothing....................'
        Kf=2*np.pi/(1.2*10**3)
        x = np.fft.fftfreq(N,1./N)  # x: 0,1,2,...,512,-511,...,-2,-1
        delta_k=np.fft.fftn(data)
        k=(x[:,None,None]**2.+x[None,:,None]**2.+x[None,None,:]**2.)**(1./2.)
        window_k = np.sinc( 1./N* x[:,None,None]) * np.sinc( 1./N * x[None,:,None]) * np.sinc( 1./N * x[None,None,:])
        smoothed_k=(delta_k*np.exp(-0.5*(Kf*Kf)*k*k*sigma**2))/window_k
        smoothed_x=np.fft.ifftn(smoothed_k)
        print 'Smoothing..................OK'
        if log==True:
            return np.log(np.abs(smoothed_x))
        if log==False:
            return smoothed_x.real

    @classmethod
    def DeltagW(self,data):
        '''return (deltagx,deltagy)'''
        print 'calculating deltaW...........'

        wk=Tide.Get_wk()
        nx=np.fft.fftfreq(N,1./N)
        Kx=2*np.pi/L*nx
        zero=np.zeros_like(Kx)
        K=np.sqrt(Kx[:,None,None]**2+Kx[None,:,None]**2+Kx[None,None,:]**2)
        K[0,0,0]=10**(-4)
        delta_gk=np.fft.fftn(data)
        del data
        W=wk(K)
        W[0,0,0]=0
        delta_gk_wx=delta_gk*W*1j*(Kx[:,None,None]+zero[None,:,None]+zero[None,None,:])
        del K
        result_x=np.array(np.fft.ifftn(delta_gk_wx).real)
        del delta_gk_wx
        print 'deltagx is ok'
############################## delta_g^wy #############################
        delta_gk_wy=delta_gk*W*1j*(Kx[None,:,None]+zero[:,None,None]+zero[None,None,:])
        result_y=np.array(np.fft.ifftn(delta_gk_wy).real)
        del delta_gk_wy
        print 'deltagy is ok'
        return (result_x,result_y)

    @classmethod
    def CalGamma(self,delta_gx,delta_gy):
        '''cal gammax gammay'''
        print 'calculating gamma............'
        gamma1=delta_gx*delta_gx-delta_gy*delta_gy
        gamma2=2*delta_gx*delta_gy
        return (gamma1,gamma2)

    @classmethod
    def CalKappa(self,gamma1,gamma2):
        print 'calculating kappa_3dx........'
        gamma1_k=np.fft.fftn(gamma1)
        gamma2_k=np.fft.fftn(gamma2)
        nx=np.fft.fftfreq(N,1./N)
        Kx=2*np.pi/L*nx
        zero=np.zeros_like(Kx)
        k1=Kx[:,None,None]+zero[None,:,None]+zero[None,None,:]
        k2=Kx[None,:,None]+zero[:,None,None]+zero[None,None,:]
        S=k1**2+k2**2

        S[0,0,:]=np.ones_like(S[0,0,:])
        kappa_3dk=2*(Kx[:,None,None]**2+Kx[None,:,None]**2+Kx[None,None,:]**2)/(S**2)*((k1**2-k2**2)*gamma1_k+2*k1*k2*gamma2_k)
        del S
        kappa_3dx=np.fft.ifftn(kappa_3dk).real
        print 'calculating kappa_3dx......OK'
        return kappa_3dx
        
