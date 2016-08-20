#!/usr/bin/env python
# coding=utf-8
from parameter import *
from subprocess import call
import time
if not os.path.exists(dir):
    os.mkdir(dir)
call('cp ./parameter.py %s'%dir,shell=True)
print '='*100
print '%s'%dir
#========save information of data=========
INF=open(PathOfINF,'w')
INF.writelines('# Information of data\n')
INF.writelines('# Time: %s\n'%(time.ctime()))
INF.writelines('# PATH of data: %s\n'%Input)
INF.writelines('# PATH of output: %s\n'%dir)
INF.writelines('#===============================================================================\n')
INF.writelines('N=%f\n'% (N))
INF.writelines('L=%f\n'% (L))
INF.writelines('Sigma=%f\n'% (Sigma))
INF.writelines('CutOff=%s\n'% str(CutOff))
INF.writelines('Gaussian=%s\n'% str(Gaussian))
INF.writelines('SmoothWienerOfShotnoise=%s\n'% str(SmoothWienerOfShotnoise))
INF.writelines('DIR=%s\n'% dir)
INF.close()
