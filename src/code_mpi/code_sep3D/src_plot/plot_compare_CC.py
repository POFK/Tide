#!/usr/bin/env python
# coding=utf-8
'''
compare correlation cofficient in different directory
'''
import matplotlib.pyplot as plt
import numpy as np
import sys
DIRPATH=sys.argv[1:]
N=len(DIRPATH)
#========================================
for i in np.arange(N):
    print 'path',DIRPATH[i]
    r=np.loadtxt('../result/'+DIRPATH[i]+'r.txt')
    kbin=np.loadtxt('../result/'+DIRPATH[i]+'kbin.txt')
    #========================================
    plt.figure('correlation coefficient')
    plt.title('correlation coefficient')
    plt.semilogx(kbin,r,'.-',label=DIRPATH[i])
    plt.xlabel('$\mathrm{k}\ (h/\mathrm{Mpc})$')
    plt.ylabel('$\mathrm{r}$')
plt.legend(loc='lower left')
plt.xlim([0.005,0.37])
plt.grid(axis='y')
plt.yticks(np.linspace(0.1,1.0,10))
plt.show()
