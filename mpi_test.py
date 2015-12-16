#!/usr/bin/env python
# coding=utf-8
from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
if rank==0:
    data=np.arange(size*10)
    data=data.reshape(size,-1)
else :
    data=[]
a=comm.scatter(data,root=0)

combine_data = comm.gather(a,root=0)
if rank==0:
#   combine_data=np.array(combine_data).reshape(-1)
    print combine_data
    print np.array(combine_data).reshape(size,-1)
