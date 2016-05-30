#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
def get_bias(dir='',color='',label='',cut_off=20):
    pk_cro=np.loadtxt(dir+'PS_DH')
    pk_auto=np.loadtxt(dir+'PS_DD')
    bias=pk_cro[:,1]/pk_auto[:,1]
    n=pk_cro[:,2]
    b=(bias*n)[:cut_off].sum()/n[:cut_off].sum()
    plt.figure('bias')
    plt.semilogx(pk_cro[:,0],bias,color,label=label)
    plt.axhline(y=b,color=color[0],linestyle='-.')
    plt.text(pk_cro[8,0],b,'$b=%.2f$'%b)
    return b

