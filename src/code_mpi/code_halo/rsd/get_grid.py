#!/usr/bin/env python
# coding=utf-8
import numpy as np
from scipy.interpolate import griddata
L=2.     
N=2.     
H=L/N    
grid=np.zeros((N,N,N))
sample=np.array([[0.5,0.5,0.5],[0.5,1.5,1.5],[0.5,0.5,1.5],[0.5,0.5,0.6]])
edge=np.array([0,1,2])
x=sample[:,0]
y=sample[:,1]
z=sample[:,2]
zz=np.array([1,2,3,4])
#for i,j,k in sample/H :
#    print i,j,k
#    nx=int(i)
#    ny=int(j)
#    nz=int(k)
#    grid[nx,ny,nz]+=1
#print grid
grid_r=np.arange(N)
################################################################################
#zi=griddata(sample,zz,(grid_r[:,None,None],grid_r[None,:,None],grid_r[None,None,:]),method='nearest')
s,edges=np.histogramdd(sample=sample,bins=(edge,edge,edge),weights=zz)
print s
