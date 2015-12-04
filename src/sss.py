#!/usr/bin/env python
# coding=utf-8
import numpy as np
x=np.arange(0,513)
kn=np.sqrt(x[:,None,None]**2+x[None,:,None]**2+x[None,None,:]**2)
delta=np.log10(512)/20
kn_min=1
kn_max=512
x=np.linspace(np.log10(kn_min),np.log10(kn_max),20,endpoint=False)
i=0
bool=(kn>=(10**x[i]))*(kn<(10**x[i]+delta))
print kn[bool].shape
