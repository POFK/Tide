#!/usr/bin/env python
# coding=utf-8
import numpy as np
from TIDES import *
from mpi4py import MPI
#############################################
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
#############################################
if rank == 0:
    kx=Tide.Get_kx()
    data=Tide.LoadData(filename='/home/mtx/data/tide/0.000den00.bin')

