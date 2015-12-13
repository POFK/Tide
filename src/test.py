#!/usr/bin/env python
# coding=utf-8
import numpy as np
a=np.arange(1024)
x=a[:,None,None]+a[None,:,None]+a[None,None,:]
#np.multiply(x,x,x)
#x=x*x*x*(x+np.sin(x))
np.add(x,np.sin(x),y)
np.multiply(y,x,y)
np.multiply(y,x,y)
np.multiply(y,x,y)

